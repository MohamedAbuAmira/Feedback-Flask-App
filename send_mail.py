import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525 # from mailtrap, SMTP port 
    smtp_server = "smtp.mailtrap.io"
    username = "b9d7df5ea15835"
    password = "88f45f59ddeb24"
    message = f'<h3> New Feedback Submision</h3> \
    <ul> \
    <li> Customer: {customer}</li> \
    <li> Dealer: {dealer}</li> \
    <li> Rating: {rating}</li> \
    <li> Comments: {comments}</li> \
    </ul>'

    sender_email = "FROM@example.com"
    receiver_email = "TO@example.com"


    msg = MIMEText(message, 'html')
    msg["Subject"] = "lexus Feedback"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

