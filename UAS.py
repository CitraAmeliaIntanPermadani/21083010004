import fractions

print('\033[1m' + '==================TUGAS SISOP PROJECT AKHIR==================')
print('')
print('Nama : Citra Amelia Intan Permadani')
print('NPM  : 21083010004')
print('Sains Data')
print('Sistem Operasi - B')
print('')
print('======================DERET MATEMATIKA=====================')
print('\033[0m' + '')

def deret_aritmatika():
        print('\033[1m' + '', '', '', '', '', '|============================|')
        print('\033[1m' + '', '', '', '', '', '|------DERET ARITMATIKA------|')
        print('\033[1m' + '', '', '', '', '', '|============================|')
        print('\033[0m'+'Masukkan suku pertama')
        x = int(input('U1: '))
        print('Masukkan suku kedua')
        y = int(input('U2: '))
        print('Masukkan total suku')
        z = int(input('Un: '))
        print('Masukkan suku ke-n yang akan dicari')
        c = int(input('U ke-n: '))
        print('')

        beda = int(y-x)
        sk = int(x + (c-1)*beda) 
        print('Suku pertama = ',x)
        print('Beda = ',beda)
        print('U',c,' = ',sk,sep='')
        print('')
        suku = int(c/2*(x+sk))
        print('Jumlah',c,'suku pertama = ',suku)
        print('\033[1m'+'..........................................')
        print('')

        print('\033[0m'+'Hasil Deret: ')
        for i in range(1,z+1):
            b = x+(i-1)*beda 
            print(b,' ',end='')

        print('\nSelesai.')

def deret_geometri():
        print('\033[1m' + '', '', '', '', '', '|============================|')
        print('\033[1m' + '', '', '', '', '', '|-------DERET GEOMETRI-------|')
        print('\033[1m' + '', '', '', '', '', '|============================|')
        print('')
        print('\033[0m'+'Masukkan suku pertama')
        x = float(fractions.Fraction(input('U1: ')))
        print('Masukkan total suku')
        z = int(input('Un: '))
        print('Masukkan suku ke-n yang akan dicari')
        c = int(input('U ke-n: '))
        print('')

        r = float(fractions.Fraction(input('Rasio: ')))
        sk = float(x*(r**(c-1)))
        print('Suku pertama =',x)
        print('U',c,' = ', sk,sep='')
        print('')

        print('\033[1m'+'........................')
        print('')

        if r > 1:
           s_n = (x*(r**z))/(r-1)
        elif r < 1:
           s_n = (x*(r**z))/(1-r)
        else:
           print('Kesalahan')

        hasil = 0.01
        print('\033[0m'+'Hasil Deret')
        for i in range(1, z+1):
            s = x*r**(i-1)
            hasil = hasil + s
            print(round(s,4),'  ',end='')

        print('\nJumlah semua suku (Sn) = ', round(hasil,2))
        print('')
        print('\nSelesai.')

def deret_ganjil():
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

def deret_genap():
        print('\033[1m' + '', '', '', '', '', '|============================|')
        print('\033[1m' + '', '', '', '', '', '|---------DERET GENAP--------|')
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
            if i % 2 == 0:
               print(i,'  ',end='')
        print('\nSelesai')

while True:
	print('----------MENU----------')
	print('1 - Deret Aritmatika')
	print('2 - Deret Geometri')
	print('3 - Deret Ganjil')
	print('4 - Deret Genap')
	print('5 - Exit')

	print('')
	pilihan = int(input('Masukkan Pilihan dari Menu(masukkan angka): '))

	if pilihan == 1:
	    deret_aritmatika()
	    print('')
	elif pilihan == 2:
	    deret_geometri()
	    print('')
	elif pilihan == 3:
	    deret_ganjil()
	    print('')
	elif pilihan == 4:
	    deret_genap()
	    print('')
	elif pilihan == 5:
	    print('')
	    print('====================TERIMA KASIH====================')
	    print('')
	    break
	else:
	    print('Kesalahan')
	    print('')
