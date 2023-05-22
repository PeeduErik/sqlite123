import sqlite3

def lisa():
    yhendus = sqlite3.connect ("ppajo.db")
    a = yhendus.cursor()
    eesnimi = input("Sisesta nimi: ")
    perenimi = input("Sisesta perenimi: ")
    email = input("Sisesta email: ")
    car_make = input("Sisesta automark: ")
    car_model = input("Sisesta automudel: ")
    car_year = int(input("Sisesta auto aasta: "))
    car_price = float(input("Sisesta auto hind: "))
    a.execute('INSERT INTO tabel (eesnimi, perenimi, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)', (eesnimi, perenimi, email, car_make, car_model, car_year, car_price))
    yhendus.commit()
    yhendus.close()
def kuvaread():
    yhendus = sqlite3.connect ("ppajo.db")
    a = yhendus.cursor()
    a.execute("SELECT * FROM tabel WHERE car_year<2000 LIMIT 20")
    siuu = a.fetchall()
    for rida in siuu:
        print(rida)
    yhendus.close()
def kustuta():
    yhendus = sqlite3.connect ("ppajo.db")
    a = yhendus.cursor()
    k = input("Sisesta ID mille tahad kustutada: ")
    a.execute("DELETE FROM tabel WHERE id = ?", (k,))
    yhendus.commit()
    yhendus.close()
def kesk():
    yhendus = sqlite3.connect ("ppajo.db")
    a = yhendus.cursor()
    a.execute("SELECT AVG(car_year) FROM tabel")
    avg_aasta = a.fetchone()[0]
    print("Keskmine autode aasta:", avg_aasta)
    a.execute("SELECT MAX(car_price) FROM tabel")
    max_hind = a.fetchone()[0]
    print("Kõige kallim hind:", max_hind)
    yhendus.close()
def kallid_autod():
    yhendus = sqlite3.connect ("ppajo.db")
    a = yhendus.cursor()
    a.execute("SELECT * FROM tabel WHERE car_price>70000 LIMIT 5")
    mjau = a.fetchall()
    for rida in mjau:
        print(rida)
    yhendus.close()
    
def uusauto():
    yhendus = sqlite3.connect ("ppajo.db")
    a = yhendus.cursor()
    sql = "SELECT car_make, car_model FROM tabel ORDER BY car_year DESC LIMIT 5"
    a.execute(sql)
    results = a.fetchall()
    print("5 kõige uuemat automarki koos mudelitega: ")
    for row in results:
        print(row[0], row[1])
    yhendus.close()
   
    
    
def menu():
         while True:
                    print("Tee valik\n1. Asjade lisamin\n2. Kuva vanemad autod\n3. Kustutamine\n4. Keskmine ja kallis\n5. Kallid autod \n6. 5 kõige uuemat autot\n0. exit")
                    algus = int(input("Sisesta nr: "))
                    if algus == 1:
                        lisa()
                    elif algus == 2:
                        kuvaread()
                    elif algus == 3:
                        kustuta()
                    elif algus == 4:
                        kesk()
                    elif algus == 5:
                        kallid_autod()
                    elif algus == 6:
                        uusauto()
                        
                    
                        
                    
       
if __name__ == '__main__':
            menu()
     
