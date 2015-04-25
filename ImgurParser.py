import urllib2 as ul
import urllib
import os

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
    endPage = '<div class="posts sub-gallery br10">\n                                    <div id="nomore" class="textbox">\n                    <a href=\'/\'>Discover more images.</a>\n                </div>\n            \n        \n        \n    </div>'
    if endPage == sourceCode:
        return 1
    else:
        return 0

def getAllImage(source):
    soup = bs(source)
    images = soup.findAll('img')
    for image in images:
        link = str(image['src'])[2:]
        fileName = find_between_r(link,"/",".jpg")+".jpg"
        urllib.urlretrieve(link,fileName)


def makeDir(celeb):
    directory = "./"+celeb
    if not os.path.exists(directory):
        os.makedirs(directory)
    #make a folder with celeb name

if __name__ == "__main__":
    celeb = raw_input('Enter the name of the celebrity:\t')
    celeb = celeb.replace(" ","")
    count = 1
    url = 'http://imgur.com/r/'+celeb+'/new/page/'+str(count)+'/hit?scrolled'
    makeDir(celeb)
    while 1:
        if checkEnd(str(getSourceCode(url))):
            print "No image"
            break
        else:
            try:
                getAllImage(url)
                print "Image No. "+str(count)+" Done"
                count = count + 1
            except:
                count = count + 1
                continue
