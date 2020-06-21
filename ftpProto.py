from ftplib import FTP
import sys
import os
import socket


def Ftp_Request(host, user, password):
    print("host : " + host)
    print("user : " + user)
    print("password : " + password)

    saisi = input("Confirmer Y/N : ")

    if saisi == "Y" or saisi == "y":
        clearConsole()

        print("1) Afficher l'arborescence")
        print("2) Envoyer un fichier")
        print("3) créer un dossier")
        print("4) supprimer un dossier")
        print("5) renomer un dossier")
        print("6) supprimer un fichier")
        print("7) changer de dossier")

        out = input([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][
                        0] + "/CommandLine#>")

        if out == "1":
            ShowFolder_Request(host, user, password)
        elif out == "2":
            CopyFile_Request(host, user, password)
        elif out == "3":
            CreateFolder_Request(host, user, password)
        elif out == "4":
            RemoveFolder_Request(host, user, password)
        elif out == "5":
            RenameFolder_Request(host, user, password)
        elif out == "6":
            RemoveFile_Request(host, user, password)
        elif out == "7":
            ChangeFolder_Request(host, user, password)

    elif saisi == "N" or saisi == "n":
        sys.exit(0)

    connect = FTP(host, user, password)

    etat = connect.getwelcome()
    print(etat)

    connect.quit()

    return 1


# fonction auto

def clearConsole():
    print(sys.platform)
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    elif sys.platform == "win32":
        os.system('cls')


def ShowFolder_Request(host, user, password):
    ftp = FTP(host, user, password)
    print(ftp.dir())

    return 8


def CopyFile_Request(host, user, password):
    ftp = FTP(host, user, password)

    f_name = input("Insérez le chemin du fichier : ")
    f = open(f_name, 'rb')
    ftp.storbinary('STOR ' + f_name, f)
    f.close()

    return 2


# fonction manuelle

def CreateFolder_Request(host, user, password):

    out = input("Nom du dossier : ")

    ftp = FTP(host, user, password)
    ftp.mkd(out)

    return 3


def RemoveFolder_Request(host, user, password):

    out = input("Nom du dossier : ")

    ftp = FTP(host, user, password)
    ftp.rmd(out)

    return 4


def RenameFolder_Request(host, user, password):

    out = input("Nom du dossier : ")

    out2 = input("Nouveau nom : ")

    ftp = FTP(host, user, password)
    ftp.rename(out, out2)

    return 5


def RemoveFile_Request(host, user, password):

    out = input("Nom du fichier : ")

    ftp = FTP(host, user, password)
    ftp.delete(out)

    return 6


def ChangeFolder_Request(host, user, password):

    out = input("Nom du dossier : ")

    ftp = FTP(host, user, password)
    ftp.sendcmd('CWD ' + out)

    return 7
