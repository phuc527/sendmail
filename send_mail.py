import smtplib


message = input("Muon noi gi voi t: ;v ")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('phucbo755@gmail.com','phuc01682193798')
server.sendmail('phucbo755@gmail.com','phucbo755@gmail.com',message)