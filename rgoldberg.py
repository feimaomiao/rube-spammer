import smtplib, ssl
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
	context= ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		# infinite loop
		i = 0
		while True:
			i += 1
			server.sendmail(sender_email, receiver, message)
			print(f'{i} Email(s) sent')

