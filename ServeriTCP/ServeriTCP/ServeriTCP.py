from socket import *
from _thread import *
import random, datetime, re

#Hyrja
print('========================================================='
      '\nUniversiteti i Prishtinës "Hasan Prishtina", njësia FIEK'
      '\n    Projekt nga lënda e Rrjetave Kompjuterike!'
      '\n    Serveri është i gatshëm të pranoj kërkesa!'
      '\n=======================================================')

emriServerit = 'localhost'
portiServerit = 12000
soketiServerit = socket(AF_INET, SOCK_STREAM)
soketiServerit.bind((emriServerit, portiServerit))
# <- Vendoset lidhja

print('     Serveri filloi punën në portin: '+str(portiServerit))
soketiServerit.listen(7)

#VEPRIMET
#IP adresa
def IPADRESA (adresa):
    return str(adresa[0])

#Numri i portit
def NUMRIIPORTIT(adresa):
    return str(adresa[1])

#Bashkëtingëlloret
def BASHKETINGELLORE (fjaliaF):
    numratori = len(re.findall('[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz]', fjaliaF))
    return (numratori - 10)

#Printimi
def PRINTIMI(fjaliaF):
    fjaliaF=str(fjaliaF).replace('PRINTIMI ', '')
    return str(fjaliaF)

#Emri i kompjuterit
def EMRIIKOMPJUTERIT():
    try:
        emriPC=gethostname()
        return str(emriPC)
    except socket.error as gabim:
        return 'Emri i Pc-së nuk mund të gjindej!'
     
#Koha
def KOHA():
    return str(datetime.datetime.now())

#Loja
def LOJA():
    numrat=[]
    return random.sample(range(1, 49), 7)
    

#Fibonacci
def FIBONACCI(numri):
    hyrja = int(numri)
    a = 0; b = 1
    if(hyrja < 0 or hyrja == 'Null'):
        return 'Provoni përsëri'
    elif hyrja == 1: 
        return a 
    elif hyrja == 2: 
        return b 
    else:
        for i in range(2, hyrja + 1): 
            c = a + b 
            a = b 
            b = c
        return str(b)

#Shëndërrimi
def KONVERTIMI(njesia,sasia):
    if(njesia == 'KilowattToHorsepower'): 
        return float(sasia/0.746)
    elif(njesia == 'HorsepowerToKilowatt'):
        return float(sasia*0.746)
    elif(njesia == 'DegreesToRadians'):
        return float(sasia*3.14/180)
    elif(njesia == 'RadiansToDegrees'):
        return float(sasia*180/3.14)
    elif(njesia == 'GallonsToLiters'):
        return float(sasia*3.785)
    elif(njesia == 'LitersToGallons'):
        return float(sasia*0.264)
    else:
        return 'Provo përsëri!'

#Perimetri i rrethit
def PERIMETRIRR(rrezja):
    P = 2*rrezja*3.14
    return P

#Sipërfaqja e rrethit
def SIPERFAQJARR(rrezja):
    S = 3.14*rrezja*rrezja
    return S

#Thredi
def thredi(connectionSocket):
    while 1:
       
            print('Klienti u lidh ne serverin %s me port %s' % adresa)
            fjala=(bytes)('Infot'.encode())
            try:

                while str(fjala.decode())!='':
                    try:

                        fjala = connectionSocket.recv(1024)
                        fjalaKapur = fjala.decode('UTF-8');
                        print('Kërkesa nga klienti: ' + fjalaKapur)
                        fjalaKapur = fjalaKapur.split(' ')

                        fjalaFund = ''.join(fjalaKapur)
                        fjalaPrint = ' '.join(fjalaKapur)

                    except:
                        print(fjala.decode())

                    if (fjalaKapur[0] == 'IPADRESA'):
                        kap = IPADRESA (adresa);
                        rezultati = 'IP-adresa: ' + str(kap);
                        connectionSocket.send (rezultati.encode('UTF-8'))
                        
                    elif(fjalaKapur[0] == 'NUMRIIPORTIT'):
                        kap=NUMRIIPORTIT(adresa)
                        rezultati='Numri i portit: '+str(kap)
                        connectionSocket.send (rezultati.encode('UTF-8'))
                        
                    elif(fjalaKapur[0]=='BASHKETINGELLORE'):
                        kap=BASHKETINGELLORE(fjalaFund);
                        rezultati='Numri i bashkëtingëlloreve në fjali: '+str(kap)
                        connectionSocket.send(rezultati.encode('UTF-8'))

                    elif(fjalaKapur[0]=='PRINTIMI'):
                        kap=PRINTIMI(fjalaPrint)
                        rezultati='Teksti i shtypur: '+str(kap)
                        connectionSocket.send(rezultati.encode('UTF-8'))

                    elif(fjalaKapur[0] == 'EMRIIKOMPJUTERIT'):
                        kap=EMRIIKOMPJUTERIT();
                        rezultati='Emri i PC-së: '+str(kap);
                        connectionSocket.send(rezultati.encode('UTF-8'))
                    
                    elif(fjalaKapur[0] == 'KOHA'):
                        kap=KOHA();
                        rezultati='Koha në server: '+str(kap)                        
                        connectionSocket.send(rezultati.encode('UTF-8'))

                    elif(fjalaKapur[0]=='LOJA'):
                        kap=LOJA()
                        rezultati='Numrat e rastit: '+str(kap)
                        connectionSocket.send(rezultati.encode('UTF-8'))

                    elif (fjalaKapur[0] == 'FIBONACCI'):
                        kap = FIBONACCI(fjalaKapur[1])
                        rezultati = 'Numri rendor Fibonacci: ' + str(kap)
                        connectionSocket.send (rezultati.encode('UTF-8'))

                    elif (fjalaKapur[0] == 'KONVERTIMI'):
                        kap = KONVERTIMI(str(fjalaKapur[1]),int(fjalaKapur[2]))
                        rezultati= 'Shëndërrimi: ' + str(kap)
                        connectionSocket.send(rezultati.encode('UTF-8'))

                    elif (fjalaKapur[0] == 'PERIMETRIRR'):
                        kap = PERIMETRIRR(int(fjalaKapur[1]))
                        rezultati= 'Perimetri i rrethit: ' + str(kap)
                        connectionSocket.send(rezultati.encode('UTF-8'))

                    elif (fjalaKapur[0] == 'SIPERFAQJARR'):
                        kap = SIPERFAQJARR(int(fjalaKapur[1]))
                        rezultati= 'Sipërfaqja e rrethit: ' + str(kap)
                        connectionSocket.send(rezultati.encode('UTF-8'))

                    else:
                        connectionSocket.send('Kërkesa shpërfillet'.encode())
                connectionSocket.close()
            except Exception:
                print('Klienti është jashtë linjës')
                break

while True:
    connectionSocket, adresa = soketiServerit.accept()
    start_new_thread(thredi,(connectionSocket,))
connectionSocket.close()
