from socket import *

#Hyrja
print('========================================================='
      '\nUniversiteti i Prishtinës "Hasan Prishtina", njësia FIEK'
      '\n    Projekt nga lënda e Rrjetave Kompjuterike!'
      '\n  Klienti është i gatshëm të lidhet me Serverin!'
      '\n======================================================')

soketiK = socket(AF_INET, SOCK_DGRAM)
emriServerit=input('Emri i Serverit: ')
porti = int(input('Porti: '))


print('Jeni lidhur me serverin!\n')
print('Serveri përmban këto kërkesa:'
      '\nIPADRESA - Shkruaj [IPADRESA] për të marr IP adresën tuaj!'
      '\nNUMRIIPORTIT - Shkruaj [NUMRIIPORTIT] për të marr numrin e portit tuaj!'
      '\nBASHKETINGELLORE - Shkruaj [BASHKETINGELLORE {hapsirë} teksti] për të marr numrin e bashkëtingëlloreve në tekstin e shkruar!'
      '\nPRINTIMI - Shkruaj [PRINTIMI {hapsirë} teksti] për të rikthyer fjalinë e futur!'
      '\nEMRIIKOMPJUTERIT - Shkruaj [EMRIIKOMPJUTERIT] për të marr emrin e kompjuterit!'
      '\nKOHA - Shkruaj [KOHA] për të marr kohën e saktë në server!'
      '\nLOJA - Shkruaj [LOJA] për të marr 7 numra të rastësishëm nga rangu [1-49]!'
      '\nFIBONACCI - Shkruaj [FIBONACCI {hapsirë} NUMËR] për të marr numrin Fibonaqi që i përgjigjet atij'
      '\nKONVERTIMI - Shkruaj [KONVERTIMI {hapsirë} OPCIONI {hapsirë}] për të konvertuar njësitë:'
      '\nKilowattToHorsepower, HorsepowerToKilowatt, DegreesToRadians, RadiansToDegrees, GallonsToLiters, LitersToGallons'
      '\nPERIMETRIRR - Shkruaj [PERIMETRIRR {hapsirë} Numër(rrezja)] për të marr perimetrin e rrethit me atë rreze'
      '\nSIPERFAQJARR - Shkruaj [SIPERFAQJARR {hapsirë} Numër(rrezja)] për të marr sipërfaqen e rrethit me atë rreze')

while 1:
    fjala = input('\nKërkesa: ')
    soketiK.sendto(fjala.encode('UTF-8'), (emriServerit, porti))
    info,adresaK = soketiK.recvfrom(128)
    print('Rezultati nga serveri:\n' + info.decode('UTF-8'))
    if(fjala=='fund'):
        print('Keni mbyllur lidhjen')
        break

soketiK.close()
