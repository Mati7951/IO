import mysql.connector
from PyQt5.QtWidgets import * #QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QTextEdit
from math import *

mydb = mysql.connector.connect( #ustawić dane do połączenia z bazą mysql.
  host="localhost",
  user="root",
  password="",
  database="projekt" 
)
print(mydb)

class user():
    def __init__(self,login,password):

        self.login=login
        self.password=password
        self.Zalogowany="NIE"

        def Zaloguj(login,password): #pobrać dane uzytkownika

            mycursor=mydb.cursor()

            sql="SELECT * FROM users WHERE Login = %s and Haslo = %s"
            adr=(login,password,)

            mycursor.execute(sql,adr)
            myresult=mycursor.fetchall()

            if myresult != []: #jeżeli istnieje pobierz dane | pokolei
                self.Zalogowany="TAK"
                self.User_Id=myresult[0][0]
                self.Login=myresult[0][1]
                self.Password=myresult[0][2]
                self.Email=myresult[0][3]
                self.Imie=myresult[0][4]
                self.Nazwisko=myresult[0][5]
                self.Wiek=myresult[0][6]
                self.Grupa=myresult[0][7]
                self.Pkt_Elo=myresult[0][8]

                mycursor=mydb.cursor()
                sql="SELECT * FROM grupa WHERE ID = %s"
                adr=(self.Grupa,)
                mycursor.execute(sql,adr)
                myresult=mycursor.fetchall()

                self.NazwaGrupy=myresult[0][1]
                self.Uprawnienia=myresult[0][2]

            #print(myresult)

        Zaloguj(self.login,self.password)

class Projekt():
    def __init__(self):
        def Start(): #Przejscie do początku | Panel Logowania
            self.PanelLogowania=QWidget()
            self.PanelLogowania.setFixedSize(250,150)
            self.PanelLogowania.setStyleSheet("Background-color:grey;")

            self.LayoutPanelLogowania=QVBoxLayout()
            self.NapisPanelLogowania=QLabel('Panel Logowania:')
            self.NapisPanelLogowania.setStyleSheet("color:black; font-weight:800;")

            self.TextLogin=QTextEdit('Login')
            self.TextLogin.setStyleSheet("Background-color:silver;")

            self.TextHaslo=QTextEdit('Haslo')
            self.TextHaslo.setStyleSheet("Background-color:silver;")

            self.PZaloguj=QPushButton('Zaloguj')
            self.PZaloguj.setStyleSheet("Background-color:gold; border:1; border-radius:10; height:20;")
            self.PZaloguj.clicked.connect(Zaloguj)

            self.PRejestracja=QPushButton('Rejestracja')
            self.PRejestracja.setStyleSheet("Background-color:gold; border:1; border-radius:10; height:20;")
            self.PRejestracja.clicked.connect(Rejestracja)

            self.LayoutPanelLogowania.addWidget(self.NapisPanelLogowania)
            self.LayoutPanelLogowania.addWidget(self.TextLogin)
            self.LayoutPanelLogowania.addWidget(self.TextHaslo)
            self.LayoutPanelLogowania.addWidget(self.PZaloguj)  
            self.LayoutPanelLogowania.addWidget(self.PRejestracja)

            self.PanelLogowania.setLayout(self.LayoutPanelLogowania)

            self.Menu.hide()
            self.PanelRejestracji.hide()
            self.PanelLogowania.show()

        def Rejestracja(): #Przejscie do strony z rejestracją
            self.PanelRejestracji=QWidget()
            self.PanelRejestracji.setFixedSize(250,280)
            self.PanelRejestracji.setStyleSheet("Background-color:grey;")

            self.LayoutPanelRejestracji=QVBoxLayout()

            self.NapisRejestracja=QLabel('Rejestracja:')
            self.NapisRejestracja.setStyleSheet("color:black; font-weight:800;")

            self.BRLogin=QTextEdit('Login')
            self.BRLogin.setStyleSheet("Background-color:silver;")

            self.BRHaslo=QTextEdit('Haslo')
            self.BRHaslo.setStyleSheet("Background-color:silver;")

            self.BREmail=QTextEdit('Email')
            self.BREmail.setStyleSheet("Background-color:silver;")

            self.BRImie=QTextEdit('Imie')
            self.BRImie.setStyleSheet("Background-color:silver;")

            self.BRNazwisko=QTextEdit('Nazwisko')
            self.BRNazwisko.setStyleSheet("Background-color:silver;")

            self.BRWiek=QTextEdit('Wiek')
            self.BRWiek.setStyleSheet("Background-color:silver;")

            self.PZarejestruj=QPushButton('Zarejestruj')
            self.PZarejestruj.setStyleSheet("Background-color:gold; border:1; border-radius:10; height:20;")
            self.PZarejestruj.clicked.connect(Zarejestruj)

            self.PPowrot=QPushButton('Powrot')
            self.PPowrot.setStyleSheet("Background-color:gold; border:1; border-radius:10; height:20;")
            self.PPowrot.clicked.connect(Start)

            self.LayoutPanelRejestracji.addWidget(self.NapisRejestracja)
            self.LayoutPanelRejestracji.addWidget(self.BRLogin)
            self.LayoutPanelRejestracji.addWidget(self.BRHaslo)
            self.LayoutPanelRejestracji.addWidget(self.BREmail)
            self.LayoutPanelRejestracji.addWidget(self.BRImie)
            self.LayoutPanelRejestracji.addWidget(self.BRNazwisko)
            self.LayoutPanelRejestracji.addWidget(self.BRWiek)
            self.LayoutPanelRejestracji.addWidget(self.PZarejestruj)
            self.LayoutPanelRejestracji.addWidget(self.PPowrot)

            self.PanelRejestracji.setLayout(self.LayoutPanelRejestracji)

            self.PanelLogowania.hide()
            self.PanelRejestracji.show()

        def Zarejestruj():  #Rejestracja
            self.ZLogin=self.BRLogin.toPlainText()
            self.ZHaslo=self.BRHaslo.toPlainText()
            self.ZEmail=self.BREmail.toPlainText()
            self.ZImie=self.BRImie.toPlainText()
            self.ZNazwisko=self.BRNazwisko.toPlainText()
            self.ZWiek=self.BRWiek.toPlainText()

            mycursor=mydb.cursor()
            sql="INSERT INTO users VALUES(NULL,%s,%s,%s,%s,%s,%s,'1','0')"
            adr=(self.ZLogin,self.ZHaslo,self.ZEmail,self.ZImie,self.ZNazwisko,self.ZWiek,)
            mycursor.execute(sql,adr)
            mydb.commit()

            self.PanelRejestracji.hide()
            self.PanelLogowania.show()

        def Zaloguj(): #Logowanie 
            self.LLogin=self.TextLogin.toPlainText()
            self.LHaslo=self.TextHaslo.toPlainText()

            self.ObecnyUser=user(self.LLogin,self.LHaslo) #pobranie danych danego usera (jeżeli istnieje | poprawne dane)

            if self.ObecnyUser.Zalogowany == "TAK":
                Menu()
            else:
                print("Brak takiego użytkownika")
        
        def Wyloguj():
            del self.ObecnyUser
            Start()

        def Menu(): # Przejscie po zalogowaniu do menu
            self.Menu=QWidget()
            self.Menu.setFixedSize(250,150)
            self.Menu.setStyleSheet("Background-color:grey;")

            self.LayoutMenu=QVBoxLayout()

            dane1="Witaj    "+str(self.ObecnyUser.Imie)+"   "+str(self.ObecnyUser.Nazwisko)
            dane2=str(self.ObecnyUser.Email)
            dane3="Twoje pkt(elo): "+str(self.ObecnyUser.Pkt_Elo)

            self.Dane1=QLabel(dane1)
            self.Dane1.setStyleSheet("color:black; font-weight:800;")
            self.Dane2=QLabel(dane2)
            self.Dane2.setStyleSheet("color:black; font-weight:800;")
            self.Dane3=QLabel(dane3)
            self.Dane3.setStyleSheet("color:black; font-weight:800;")

            self.NapisMenu=QLabel('Menu:')
            self.NapisMenu.setStyleSheet("color:black; font-weight:800;")

            self.PrzyciskStatystyki=QPushButton('Statystyki')
            self.PrzyciskStatystyki.setStyleSheet("Background-color:gold; border:1; border-radius:10; height:20;")

            self.PrzyciskStatystyki.clicked.connect(Statystyki)

            self.PrzyciskWyloguj=QPushButton('Wyloguj')
            self.PrzyciskWyloguj.setStyleSheet("Background-color:gold; border:1; border-radius:10; height:20;")
            self.PrzyciskWyloguj.clicked.connect(Wyloguj)

            self.LayoutMenu.addWidget(self.Dane1)
            self.LayoutMenu.addWidget(self.Dane2)
            self.LayoutMenu.addWidget(self.Dane3)
            self.LayoutMenu.addWidget(self.NapisMenu)
            self.LayoutMenu.addWidget(self.PrzyciskStatystyki)
            self.LayoutMenu.addWidget(self.PrzyciskWyloguj)

            self.Menu.setLayout(self.LayoutMenu)

            self.PanelLogowania.hide()
            self.Statystyki.hide()
            self.Menu.show()

        def Zapisz(): # Zapis do pliku
            self.dodaj=self.TextStatystyki.toPlainText()
            plik=open('Statystyki.txt','w+').write(self.dodaj)
        
        def Statystyki():
            self.Statystyki=QWidget()
            self.Statystyki.setFixedSize(500,300)
            self.Statystyki.setStyleSheet("Background-color:grey;")

            self.LayoutStatystyki=QVBoxLayout()

            self.NapisStatystyki=QLabel('Statystyki:')
            self.NapisStatystyki.setStyleSheet("color:black; font-weight:800;")

            self.TextStatystyki=QTextEdit('')
            self.TextStatystyki.setStyleSheet("Background-color:white;")

            self.PrzyciskZapisz=QPushButton('Zapisz')
            self.PrzyciskZapisz.setStyleSheet("Background-color:gold; border:1; border-radius:10; height:20;")
            self.PrzyciskZapisz.clicked.connect(Zapisz)

            self.PrzyciskPowrot2=QPushButton('Powrot')
            self.PrzyciskPowrot2.setStyleSheet("Background-color:gold; border:1; border-radius:10; height:20;")
            self.PrzyciskPowrot2.clicked.connect(Menu)

            self.LayoutStatystyki.addWidget(self.NapisStatystyki)
            self.LayoutStatystyki.addWidget(self.TextStatystyki)
            self.LayoutStatystyki.addWidget(self.PrzyciskZapisz)
            self.LayoutStatystyki.addWidget(self.PrzyciskPowrot2)

            self.Statystyki.setLayout(self.LayoutStatystyki)

            self.Menu.hide()
            plik=open('Statystyki.txt','r+').read()
            self.TextStatystyki.setPlainText(plik)
            self.Statystyki.show()

        self.PanelRejestracji=QWidget()
        self.PanelLogowania=QWidget()
        self.Menu=QWidget()
        self.Statystyki=QWidget()

        Start()

app = QApplication([])
nowe = Projekt()
app.exec_()        