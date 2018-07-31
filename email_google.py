import smtplib, datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

date = datetime.date.today()

def send_email():
	
        to = []
        to = 'joshua.thomason@avx.com', 'infosec@avx.com'
	gmail_user = 'joshua.thomason@avx.com'
	ASP = open("ASP.txt", 'r')
	gmail_password = ASP.read()
        #, 'bill@gmail.com']
	subject = "AVX Weekly Production Report - TEST"

	msg = MIMEMultipart()

	msg['FROM'] = gmail_user
	msg['To'] = to
	msg['Subject'] = subject

	body = """
	Hello there ______!
        
        This is a friendly reminder to please fill out this week's report on your production numbers.

        Please find the link to your sheet here:

        _________________________________

	Thanks and have a great day!

        """

	msg.attach(MIMEText(body, 'plain'))

	#filename = file
	#attachment = open(file, 'rb')

	#part = MIMEBase('application', 'octet-stream')
	#part.set_payload((attachment).read())
	#encoders.encode_base64(part)
	#part.add_header('Content-Disposition', 'attachment; filename=%s' % filename)

	#msg.attach(part)

	#sent_from = gmail_user 

	#message = 'Subject: {}\n\n{}'.format(subject, body)
	#email_text = """\  
	#From: %s  
	#To: %s  
	#Subject: %s

	#%s
	#""" % (sent_from, ", ".join(to), subject, body)

	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		text = msg.as_string()
		server.sendmail(gmail_user, to, text)
		server.close()

		print 'Email sent!'
	except:  
		print 'Something went wrong...'
		
	return

send_email()
