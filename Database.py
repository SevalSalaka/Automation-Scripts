import mysql.connector

mydb=mysql.connector.conect (
    host="localhost",
    user="root",
    password="",
    database="olx"
)

mycursor = mydb.cursor()

print("Dobrodosli na pik")
print("*"*80)
print("Odaberi te jednu od opcija")
print("1) Login")
print("2) Registar")
userodabir = int(input("Vas odabir je: "))
loginuser=0

if userodabir == 1:
    while True:
        username = input("Molimo unesi te vas username: ")
        password = input("Molimo unesi te vas password: ")

        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (username,password)

        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()

        if myresult:
            print("Dobrodosli u OLX sistem")
            loginuser=+1
            break
        else:
            print("Pogresan username ili password. Pokusaj te ponovo")


if userodabir == 2:
    while True:
        print("Postovani, molimo vas da popunite formu ispod")
        username = input("Molimo unesi te vas username: ")
        password = input("Molimo unesi te vas password: ")
        ime = input("Molimo unesi te vase ime: ")
        prezime = input("Molimo unesi te vase prezime: ")

        sql = "SELECT * FROM users WHERE username = %s"
        val = (username,)

        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()

        if myresult:
            print("Nazalost, username postoji u bazi podataka. Molimo pokusaj te sa drugim")
        else:
            sql = "INSERT INTO users (username,password,ime,prezime) VALUES (%s,%s,%s,%s)"
            val = (username,password,ime,prezime)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted")
            print(f"Cestitamo, upjesno ste registrovani na olx. Dobrodosli {ime} {prezime}")
            loginuser+1
            break



if loginuser==1:
    print("Molimo odaberi te opciju 1) ako prodajete artikal")
    print("Molimo odaberi te opciju 2) ako potrazuje te artikal")
    odabir=input(int("Vas odabir je: "))

    if odabir==1:
        print("Molimo vas popuni te sljedece formulare: ")
        ime_artikla=input("Ime artika: ")
        vrsta_artikla=input("Vrsta artika: ")
        cjena_artikla=int(input("Cjena artika: "))
        opis_artikla=print(input("Opis artika: "))

        sql1="INSERT INTO artikli (ime_artikla,vrsta_artikla,cjena_artikla,opis_artikla) VALUES (%s,%s,%s,%s)"
        val1= (ime_artikla,vrsta_artikla,cjena_artikla,opis_artikla)
        mycursor.execute(sql1,val1)
        print(f"Cestitamo, uspjesno ste postavili predment {ime_artikla} na prodaju")

    if odabir==2:
        trazena_rjec=input("Unesi te trazenu rjec: ")
        pretraga=mycursor.execute("SELECT * FROM customers")
        if trazena_rjec in pretraga:
            print(f"Ovo su rezultati od vase {trazena_rjec}")
            print(pretraga)



