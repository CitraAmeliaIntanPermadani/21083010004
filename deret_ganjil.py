print('\033[1m' + '', '', '', '', '', '|============================|')
print('\033[1m' + '', '', '', '', '', '|--------DERET GANJIL--------|')
print('\033[1m' + '', '', '', '', '', '|============================|')
print('')
print('\033[0m' + 'Masukkan Awal Bilangan')
A = int(input('A: '))
print('Masukkan Batas Akhir Bilangan')
Z = int(input('Z: '))
print('')

print('\033[1m' + '................................')
print('\033[0m' + 'Hasil Deret: ')
for i in range(A,Z+1):
    if i % 2 != 0:
       print(i,'  ',end='')
print('\nSelesai')

