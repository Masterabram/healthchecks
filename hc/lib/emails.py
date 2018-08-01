import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

def login_gmail(gamil_user, gmail_user_password):

    try:
        server.ehlo()
        server.login(gamil_user, gmail_user_password)
        return server
    except:
        return "Invalid credentials"



def send(name, to, body):
    sent_from = "abramogol@gmail.com"
    login_gmail(sent_from, "Mcogol12.")
    server.sendmail(sent_from, to, body)


def login(to, ctx):
    send("login", to, ctx)


def set_password(to, ctx):
    send("set-password", to, ctx)


def alert(to, ctx):
    send("alert", to, ctx)


def verify_email(to, ctx):
    send("verify-email", to, ctx)


def report(to, ctx):
    send("report", to, ctx)
