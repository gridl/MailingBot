#!/usr/bin/python

"""
 overnull.ru
 github.com/eBind

 run:
  python3 mbot.py --server smtp.smtp.ru --port 587 --user noreply@site.ru --mails emails.txt --text mail.txt --tls 0
"""

import sys
import os
import smtplib
import getpass
import optparse

def cmd_clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def create_parser():
    parser = optparse.OptionParser()

    parser.add_option('-s', '--server', dest='server', type='string', help='SMTP Server')
    parser.add_option('-p', '--port', dest='port', default=587, type='int', help='SMTP Port')
    parser.add_option('-u', '--user', dest='user', type='string', help='SMTP Username')
    parser.add_option('-m', '--mails', dest='mails', type='string', help='Emails file path')
    parser.add_option('-t', '--text', dest='text', type='string', help='Text-mail file path')
    parser.add_option('-e', '--tls', dest='encrypt', default=0, type='int', help='TLS Encrypt, 1 or 0')

    (options, args) = parser.parse_args()

    return options

def sending_mail(data, subject, smtp_connect):
    mails = open(data.mails, 'r').read().splitlines()
    text = open(data.text, 'r').read()

    for mail in mails:
        smtp_connect.sendmail(data.user, mail, text)
        print("Mail sent to " + mail)

    print("[+] Done!")


def main():
    options = create_parser()

    if options.server and options.user and options.mails and options.text:
        try:
            passwd = getpass.getpass("Password: ")
            subject = input("Subject: ")

            connect = smtplib.SMTP(options.server, options.port)

            if options.encrypt == 1:
                connect.starttls()

            connect.login(options.user, passwd)
            sending_mail(options, subject, connect)
        except:
            print("[~] Fatal error!")
            sys.exit()
    else:
        print("[~] Using: mbot.py --server smtp.smtp.ru --port 587 --user noreply@site.ru --mails emails.txt --text mail.txt --tls 0")

main()