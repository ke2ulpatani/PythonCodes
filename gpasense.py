import os
import urllib2 as ul
#import MySQLdb
from bs4 import BeautifulSoup as bs

grades = {"A+":10,"A":9.5,"A-":9,"B+":8.5,"B":8,"B-":7.5,"C+":7,"C":6.5,"C-":6,"D+":5.5,"D":5,"D-":4.5,"E":4}

def getSource(url):
    opener = ul.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    source = opener.open(url)
    return source

def getUserInfo(source):
    soup = bs(source)
    infoTable = soup.findAll('table',{'class':'dynaColorTR2'})[0]
    soup = bs(str(infoTable))
    rows = soup.findAll('tr')
    userinfo = rows[:4]
    values = []
    for tr in userinfo:
        soup = bs(str(tr))
        row = soup.findAll('td')[1]
        values.append(str(row.text))
    query = "INSERT INTO `details` VALUES %s"%(str(tuple(values)))
    print 'getUserInfo'
    executeSQL(query)

def getUserMarks(source):
    soup = bs(source)
    marksTable = soup.findAll('table',{'id':'table1'})[0]
    soup = bs(str(marksTable))
    rows = soup.findAll('tr')
    rows.pop(0)
    values = []
    total = 0
    totalcredit = 0
    for row in rows:
        eachRow = bs(str(row))
        credit = eachRow.findAll('td')[4]
        grade = eachRow.findAll('td')[8]
        totalcredit = totalcredit + int(credit.text)
        total = total + ( float(grades[grade.text]) * int(credit.text))
    gpa = total/totalcredit
    print "Your GPA is %s"%str(gpa)
    os.system('say "Your GPA is %s"'%str(gpa))


def executeSQL(query):
    db = MySQLdb.connect('127.0.0.1','root','root','gpacal')
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    print 'Done!!'
    
#getUserInfo(getSource('http://evarsity.srmuniv.ac.in/srmwebonline/exam/onlineResultInner.jsp?registerno=1031210023&frmdate=%27or%27%27%3D%27&iden=1'))

userID = raw_input("Enter your College ID: ")

url = "http://evarsity.srmuniv.ac.in/srmwebonline/exam/onlineResultInner.jsp?registerno="+userID+"&frmdate='or''='&iden=1"
source = getSource(url)
#getUserInfo(source)
getUserMarks(source)
