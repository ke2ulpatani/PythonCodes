import urllib2,cookielib,smtplib
import getpass,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

site= "http://in.bookmyshow.com/serv/getData/?cmd=GETSHOWTIMESBYEVENTANDVENUE&f=json&dc=20160129&vc=PRHN&ec=ET00038638"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib2.Request(site, headers=hdr)
username = "ke2ul.patani@gmail.com"#raw_input('Enter the id you want to use to send mail:\t')
password = #getpass.getpass('Enter the password for the above mentioned id:\t')
sender = username
receivers = ['ke2ul.patani@Gmail.com']

truth = 1

while (truth):
	try:
		page = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
		print e.fp.read()
		break
	
	content = str(page.read())
	
	if content != '{"BookMyShow":{"arrEvent":[],"arrVenue":[],"arrShows":[]}}':
		try:
			smtpObj = smtplib.SMTP('smtp.gmail.com:587')
			smtpObj.starttls()
			smtpObj.login(username,password)

			for i in range(0,len(receivers)):
				msg = MIMEMultipart('alternative')
				msg['Subject'] = "BookMyShow - DeadPool"
				msg['From'] = sender
				msg['To'] = receivers[i]
				text = "DeadPool movie is Available in PRHN"
				part1 = MIMEText(text, 'plain')
				msg.attach(part1)
				for k in range(0,5):
					smtpObj.sendmail(sender, receivers[i], msg.as_string())
					print "%s,%s"%(receivers[i],k)
			break
		except :
			print "Error: unable to send email"
	else:
	    print 'The show is still not Available'
	    time.sleep(300)