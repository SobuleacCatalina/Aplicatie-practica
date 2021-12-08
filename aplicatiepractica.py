with open('Lista clasei 11D.txt','r') as f:
    lista=list(f)
print('Nume'.ljust(15)+'Prenume'.ljust(15)+'Nota'.ljust(7)+'Grupa'.ljust(10))
n=media=0
for linie in lista:
    coloane=linie.split()
    media+=int(coloane[2])
    n+=1
    if coloane[3]=='eng1':
        f=open('eng1.txt','a')
        f.write(linie)
        f.close()
    if coloane[3]=='eng2':
        f=open('eng2.txt','a')
        f.write(linie)
        f.close()
    print(str(coloane[0]).ljust(15)+str(coloane[1]).ljust(15)+str(coloane[2]).ljust(7)+str(coloane[3]).ljust(10))
print('media clasei = ',round(media/n,2))