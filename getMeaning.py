from bs4 import BeautifulSoup as bs
import urllib2 as ul
import re
dictionary = {}

def properFormat(syn):
    syn = syn.strip()
    syn = syn[2:]
    syn = syn.split('.',1)
    syn = list(syn)[0]
    syn = syn.replace(' ','')
    syn = syn.replace(';',',')
    syn = syn.split(',')
    return syn
    
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

    antbox = soup.findAll('div',{'class':re.compile('tail-type-antonyms')})
    synbox = soup.findAll('div',{'class':re.compile('tail-type-synonyms')})

    soup = bs(str(synbox))
    synonyms = soup.find('div',{'class':re.compile('js-toggle-tail-blobs')})
    dictionary[keyword]['synonyms']=properFormat(str(synonyms.text).strip())

    soup = bs(str(antbox))
    antonyms = soup.find('div',{'class':re.compile('js-toggle-tail-blobs')})
    dictionary[keyword]['antonyms']=properFormat(str(antonyms.text).strip())

    
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
    dictionary.clear()
    try:
        getDefinition('http://dictionary.reference.com/browse/%s?s=t'%word,word)
    except Exception as x:
        print x
        continue
