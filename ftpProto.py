import ftplib as ftp

def Ftp_Request(host, user, password):
    print("host : " + host)
    print("user : " + user)
    print("password : " + password)

    connect = ftp.ftplib(host, user, password)

    connect.quit()

    return 1