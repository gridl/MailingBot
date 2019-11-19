# Mailing Bot v0.5
# Web-Site: overnull.ru

Mailing Bot - python program for sending email messages from your smtp server.

# Run
$> python3 mbot.py --server smtp.smtp.ru --port 587 --user noreply@site.ru --mails emails.txt --text mail.txt --tls 0

--tls - 0 or 1, 1 - on encryption 
--mails - mails file, 1 line contains 1 mail
--text - mail text file


Short view:
$> python3 mbot.py -s smtp.smtp.ru -p 587 -u noreply@site.ru -m emails.txt -t mail.txt -e 0

