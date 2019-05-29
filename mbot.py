#!/usr/bin/python

import sys
import os
import smtplib
import getpass

smtp_server = raw_input('SMTP server: ')
port = raw_input('Server port: ')
user = raw_input('SMTP user: ')
passwd = getpass.getpass('Password: ')
subject = raw_input('Subject mails: ') 

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.login(user,passwd)
    
    lines = open('emails.txt').read().splitlines()
    body = open('text_mail.txt').read()
    
    for i in lines:
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,i,msg)
        print "Email sent to: " + i
        sys.stdout.flush()
        
    server.quit()
    
    print '\n Done!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] Wrong login or password.'
    sys.exit()
