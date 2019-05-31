#!/usr/bin/python

import sys
import os
import smtplib
import getpass

datafile = open('data.txt')
data = datafile.read()
opendata = 'n'

if "saved" in data:
	opendata = raw_input('Open saved data? [Y/n]: ')

if opendata.lower() != 'y':
    smtp_server = raw_input('SMTP server: ')
    port = raw_input('Server port: ')
    user = raw_input('SMTP user: ')
    passwd = getpass.getpass('Password: ')
    saveinfo = raw_input('Save data? [Y/n]: ')
    if saveinfo.lower() == 'y':
    	datafile.close()
        datafile = open('data.txt', 'w+')
    	datafile.write(smtp_server + '\n' + port + '\n' + user + '\nsaved')
        print('\nData successfully saved!')
else:
	print('Opening...')
	lns = data.splitlines()
	smtp_server = lns[0]
	port = lns[1]
	user = lns[2]
	passwd = getpass.getpass('\nPassword from ' + user + ': ')
	
	
subject = raw_input('\nSubject mails: ') 
counts = raw_input('Count mails for one user(default: 1): ')
if counts == 0 or counts == '' or '-' in counts:
	counts = 1

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    
    lines = open('emails.txt').read().splitlines()
    body = open('text_mail.txt').read()
    
    for i in lines:
    	b = 0
    	while b < int(counts):
    	    b = b + 1
            msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
            server.sendmail(user,i,msg)
            print "Email sent to: " + i + " number " + str(b)
            sys.stdout.flush()
        
    server.quit()
    
    print '\nDone!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] Wrong login or password.'
    sys.exit()
