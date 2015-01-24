from bs4 import BeautifulSoup as bs
import urllib2 as ul

dictionary = {}

def getSource(url):
    page = ul.urlopen(url)
    source = page.read()
    return source

def getDefinition(page,keyword):
    print page
    source = getSource(page)
    dictionary[keyword]={}
    soup = bs(source)
    sourcedata = soup.findAll('div',{'class':'source-data'})[:1]
    soup = bs(str(sourcedata))
    sections = soup.findAll('section',{'class':'def-pbk'})[:3]

    for section in sections:
        soup = bs(str(section))
        wordtype = soup.find('span',{'class':'dbox-pg'})
        dictionary[keyword][str(wordtype.text)]=[]
        definitions = soup.findAll('div',{'class':'def-set'})[:5]
        for definition in definitions:
            soup = bs(str(definition))
            meaning = soup.find('div',{'class':'def-content'})  
            dictionary[keyword][str(wordtype.text)].append(str(meaning.text).strip().replace('.',''))

    print dictionary

while (True):
    word = raw_input('Enter the word:\t')
    try:
        getDefinition('http://dictionary.reference.com/browse/%s?s=t'%word,word)
    except:
        continue

        

        
        
