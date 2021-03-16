"""
# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("e.vyji95@gmail.com", "een@du654")
# message to be sent
frm = 'e.vyji95@gmail.com'
to = 'e.vyji95@gmail.com'
subject = 'test py'
text = "Test py mail"
message = 'Subject: {}\n\n{}'.format(subject, text)


# sending the mail
s.sendmail(frm,to, message)

# terminating the session
s.quit()

"""

"""
# Python code to illustrate Sending mail from
# your Gmail account

#same as before code but added extra lines of code.. 
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
# the mail address and password
sender_address = 'e.vyji95@gmail.com'
sender_pass = 'een@du654'
receiver_address = 'arbmrec1@gmail.com'

# Authentication
s.login(sender_address, sender_pass)

# message to be sent
frm = sender_address
to = receiver_address
subject = ''
text = "Sample mail by using python code"
message = 'Subject: {}\n\n{}'.format(subject, text)


# sending the mail
s.sendmail(frm,to, message)

# terminating the session
s.quit()

"""
"""
##########    SENDING MAIL TO MULTIPLE USERS ########

import smtplib

li = ["arbmrec1@gmail.com" ,"e.vyji95@gmail.com" ,"pulisunilkumarreddy@gmail.com"]

for j in li:
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("e.vyji95@gmail.com","een@du654")
    subject = 'PyMail verification'
    message = "Testing Multiple users mail"
    s.sendmail("vishnuvardhan.eyunni@gmail.com", j,message)
    s.quit()
"""












