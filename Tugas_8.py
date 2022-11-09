from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# Input batas perulangan
batas = int(input("Masukkan batas perulangan : "))
print()

# Inisialisasi Fungsi yang akan digunakan:
def cetak(i):
    for i in range(1, batas+1):
        if i % 2 == 1:
           print(i, "Ganjil", "- ID proses", getpid())
           continue
        print(i, "Genap", "- ID proses", getpid())
    sleep(1)

# 1-Pemrosesan Sekuensial
print("sekuensial")
## untuk mendapatkan waktu sebelum eksekusi
sekuensial_awal = time()
## proses berlangsung
for i in range(1):
    cetak(i)
## untuk mendapatkan waktu setelah eksekusi
sekuensial_akhir = time()
print()

# 2-Multiprocessing dengan Kelas Process
print("multiprocessing.Process")
## untuk menampung proses-proses
kumpulan_proses = []
## untuk mendapatkan waktu sebelum eksekusi
process_awal =  time()
## proses berlangsung
for i in range(1):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()
## untuk menggabungkan proses-proses agar tidak loncat ke proses sebelumnya
for i in kumpulan_proses:
    p.join()
## untuk mendapatkan waktu setelah eksekusi
process_akhir = time()
print()

# 3-Multiprocessing dengan Kelas Pool
print("multiprocessing.Pool")
## untuk mendapatkan waktu sebelum eksekusi
pool_awal = time()
## proses berlangsung
pool = Pool()
pool.map(cetak, range(0,1))
pool.close()
## untuk mendapatkan waktu setelah eksekusi
pool_akhir = time()
print()

# Perbandingan waktu eksekusi
print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu multiprocessing.Pool :", pool_akhir - pool_awal, "detik")
