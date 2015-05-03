from threading import Thread as T
import urllib2 as ul
import urllib
import os
from bs4 import BeautifulSoup as bs
from urllib2 import URLError, HTTPError

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

def getSourceCode(url):
    source = ul.urlopen(url)
    source = source.read()
    return source



def checkEnd(sourceCode):
    endPage = '<div class="posts sub-gallery br10">\n<div id="nomore" class="textbox">\n<a href=\'/\'>Discover more images.</a>\n</div>\n\n\n\n</div>'
    if endPage == sourceCode:
        return 1
    else:
        return 0

def getAllImage(source,celeb):
    soup = bs(source)

    images = soup.findAll('img')

    for image in images:
        link = str(image['src'])[2:]
        fileName = find_between_r(link,"/",".jpg")
        link = "http://" + link.replace(fileName,fileName[:-1])
        fileName = fileName + ".jpg"
        print link
        urllib.urlretrieve(link,"./"+celeb+"/"+fileName)
    if len(images) >0:
        return 1
    else:
        return 0

def makeDir(celeb):
    directory = "./"+celeb
    if not os.path.exists(directory):
        os.makedirs(directory)
        print 'dir made'


if __name__ == "__main__":
    celeb = raw_input('Enter the name of the celebrity:\t')

    celeb = celeb.replace(" ","")
    count = 1
    url = 'http://imgur.com/r/'+celeb+'/new/page/'+str(count)+'/hit?scrolled'
    print url
    makeDir(celeb)
    while 1:
        source = str(getSourceCode(url))
        if checkEnd(str(source)):
            print "No image"
            break
        else:
            try:
                if (getAllImage(str(source),celeb)):
                    print "Page No. "+str(count)+" Done"
                    count += 1
                else:
                    print "Page No. "+str(count)+" Not Done"
                    break
                    count +=1
            except:
                count += 1
                print 'Error'
                continue
