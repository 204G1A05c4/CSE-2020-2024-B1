msg = 'Dear Sir,'
m = 'We have captured a missing child face and the child id is '
dt = "Detected on "
tm = 'at '
im = "Kindly have a look on the attached photo and take necessary actions"
t = 'Regards,'
t1 = 'Missing Child Identification Center.'
mail_content = msg + ',' + '\n' + m + ' ' + str('cmd456') + '\n' + '\n' + t + '\n' + t1
sender_address = 'nagamchenchulakshmi@gmail.com'
sender_pass = 'ykdfxavwvpffwvwd'
receiver_address = 'nagamchenchulakshmi@gmail.com'
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Missing Child Recognition System'
message.attach(MIMEText(mail_content, 'plain'))
ses = smtplib.SMTP('smtp.gmail.com', 587)
ses.starttls()
ses.login(sender_address, sender_pass)
text = message.as_string()
ses.sendmail(sender_address, receiver_address, text)
ses.quit()

newMessage = EmailMessage()
newMessage['Subject'] = "Missing Child Recognition System"
newMessage['From'] = Sender_Email
newMessage['To'] = Reciever_Email
newMessage.set_content(
    'You have successfully been vaccinated with all the doses of COVID-19 vaccine. Download the attached certificate')

with open('pictures/vaccination.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name

newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, Password)
    smtp.send_message(newMessage)
noOfFile = len(os.listdir("ImagesUnknown")) + 1
