import smtplib as s
server=s.SMTP_SSL('smtp.gmail.com',465)
server.login('rakshitrahul77@gmail.com','12345678')

server.sendmail('rakshitrahul77@gmail.com', 'saikatrakshit10@gmail.com', 'Hello')
print('send mail')
server.quit()

# a.ehlo()
# a.starttls()
# c='Test'
# b='Hi, how are You'
# m='c:{}\n\n'.format(c,b)
