import smtplib
from email.mime.text import MIMEText

users = {"Ted Kaczynski" : "unab@omber.com",
         "Joe Biden" : "sleepy@joe.com",
         "Donald Trump" : "trump@gaming.com"}

print(users)

user1 = {"name": "Ted Kaczynski", "email": "unab@omber.com"}

print(users.get("Ted Kaczynski"))
print("=========================================")
print(user1.get("email"))

print(users.get("Ted"))
print(users.get("Ted", "invalid username"))

print(users["Ted Kaczynski"])

username = "ted"
if username in users:
    print(users[username])

username = "Ted Kaczynski"
if username in users:
    print(users[username])

for e in users:
    print(e)

for e in users.keys():
    print(e)

for e in users.values():
    print(e)

print(users.items())

for key, value, in users.items():
    print("Key " + str(key) + " value " + value)

user1 = {"name": "Ted Kaczynski", "email": "unab@omber.com"}

user1["password"] = "AFGAGAa134235"
print(user1)

if "password" in user1.keys():
    del user1["password"]
print(user1)

user1.update({"password": "%$2342"})
print(user1)

if "password" in user1.keys():
    print(user1.pop("password"))
print(user1)

user1 = {"name": "Ted Kaczynski", "email": "unab@omber.com"}
user2 = {"name": "barack", "email": "obamus@mail.com"}
user3 = {"name": "Josef", "email": "ilovemykids@mail.com"}
user4 = {"name": "andrzej", "email": "andrzela@mail.com"}

dict_list = []
dict_list.append(user1)
dict_list.append(user2)
dict_list.append(user3)
dict_list.append(user4)

print(len(user1))
print(len(dict_list))

for i in range(0, len(dict_list)):
    dict_list[i]["password"] = "@#dfssgf"

print(dict_list)
dict_list.append({"name": "Alice", "email": "alice@email.com"})

for i in range(0, len(dict_list)):
    if "password" not in dict_list[i].keys():
        dict_list[i]["password"] = "NOWE"
print(dict_list)

for i in range(0, len(dict_list)):
    dict_list[i]["adresy"] = ["Koszykowa86", "WalaNasNaKase69"]

print(dict_list)

for i in range (0, len(dict_list)):
    dict_list[i]["adresy"] = {"adres_domowy": "Koszykowa86", "adres_kor": "WalaNasNaKase69"}
print(dict_list)

filename = "students1.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

students = ["Alice", "Bob"]
filename = "studentsOut.txt"
with open(filename, "w") as file_object:
    for e in students:
        line = f"witaj {e}\n"
        file_object



def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = [", "].join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

    subject = "Email wysłany  zPython'a"
    body = "To jest wiadomosc wyslana za pomoca SMTP"
    sender = "test@gmail.com"
    recipients = ["test2@gmail.com"]
    password = "hsdfhsd"

    users = {
        "lukasz": 80,
        "joe": 90,
        "test": 60,
        "admin": 99
    }
    sorted_dict = {}
    for key in sorted(users):
        value = users[key]
        sorted_dict[key] = value

    print(sorted_dict)

    sorted_dict = {}

    print(dict(sorted(users.items())))

def get_value(item):
    return item[1]

print(dict(sorted(users.items(),key=get_value)))
print(dict(sorted(users.items(),key=get_value,reverse=True)))