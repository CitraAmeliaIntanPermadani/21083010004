print('\033[1m' + '', '', '', '', '', '|============================|')
print('\033[1m' + '', '', '', '', '', '|-------DERET GEOMETRI-------|')
print('\033[1m' + '', '', '', '', '', '|============================|')
print('')
print('\033[0m'+'Masukkan suku pertama')
x = int(input('U1: '))
print('Masukkan suku kedua')
y = int(input('U2: '))
print('Masukkan suku ke-n yang akan dicari')
c = int(input('U ke-n: '))
print('')

r = int(y/x)
sk = int(x*(r**(c-1)))
print('Suku pertama =',x)
print('Rasio =',r)
print('U',c,' = ', sk,sep='')
print('')
suku = r
if r <= 0:
   s1 = int((x*(1-(r**c)))/(1-r))
   print('Jumlah suku ke-',c,' = ', s1,sep='')
else:
   s2 = int((x*((r**c)-1))/(r-1))
   print('Jumlah suku ke-',c,' = ', s2,sep='')
print('\033[1m'+'........................')
print('')

print('\033[0m'+'Hasil Deret')
for i in range(x,sk+2,r):
    print(i,'  ',end='')
print('\nSelesai.')
