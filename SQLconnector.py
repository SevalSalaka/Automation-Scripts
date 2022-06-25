import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = ""
)

mycursor = mydb.cursor()

tabela = ("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR (225), password VARCHAR(225))")
korisnici = "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)"
val = [
    (1,"Samira Mehmedovic", "bosna"),
    (2,"Selma Obralic", "sarajevo"),
    (3,"Ana Buljan", "hercegovina"),
    (4,"Amer Kiselica", "tuzla"),
    (5,"Atif Becirbasic", "mostar")
]
#mycursor.executemany(korisnici, val)
#mydb.commit()

registracija_login = input(str("Registracija ili login: "))
registracija = "registracija"
login = "login"

username = input(str("Unesite username: "))
password = input(str("Unesite password: "))

 
provjera = f"SELECT username from users WHERE username='{username}' AND password = '{password}';"
mycursor.execute(provjera)

if registracija_login == login:
    if not mycursor.fetchone():  
       print("Žao nam je, Vaši podaci nisu ispravni, molimo pokušajte ponovo.")
    else:
       print("Dobrodošli na sistem.")
elif registracija_login == registracija:
    confirm_password = input("Potvrdite password: ")
    if password != confirm_password:  
       print("Žao nam je, Vaš password nije ispravan, molimo pokušajte ponovo.")
    elif not mycursor.fetchone():
        mycursor.execute ("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mydb.commit()
        print(mycursor.rowcount, "was inserted.") 
        print("Uspješno ste registrovani.")
    else:
        print("Postojite u sistemu.")
else:
    ("Neispravan unos.")