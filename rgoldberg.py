import smtplib, ssl, os, time
"""
http://bit.ly/thrashergfr
Created by Matthew Lam
Used to make my phone vibrate in the rube-goldberg machine
"""
port = 465
smtp_server = "smtp.gmail.com"
sender_email = "lcpmatthew@gmail.com"
receiver = "lcpmatthew@gmail.com"
password = open('password.txt', 'r').read()
message= f'''\
From: {sender_email}
To: {receiver}
Subject: Test

This is a spamming email sent by myself with python3
'''

if __name__ == '__main__':
	os.system('say sending emails')
	time.sleep(2)
	context= ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		i = 0
		try:
			while True:
				i += 1
				server.sendmail(sender_email, receiver, message)
				print(f'{i} Email(s) sent')
		except KeyboardInterrupt:
			quit()
