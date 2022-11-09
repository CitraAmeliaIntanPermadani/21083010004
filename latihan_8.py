from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# Inisialisasi Fungsi yang akan digunakan:
def cetak(i):
    print("Cetak angka", i+1, "- punya ID proses", getpid())
    sleep(1)

# 1-Pemrosesan Sekuensial
print("1-Pemrosesan Sekuensial")
## untuk mendapatkan waktu sebelum eksekusi
sekuensial_awal = time()
## proses berlangsung
for i in range(10):
    cetak(i)
## untuk mendapatkan waktu setelah eksekusi
sekuensial_akhir = time()
print()

# 2-Multiprocessing dengan Kelas Process:
print("2-Multiprocessing dengan kelas Process")
## untuk menampung proses-proses
kumpulan_proses = []
## untuk mendapatkan waktu sebelum eksekusi
process_awal = time()
## proses berlangsung
for i in range(10):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()
## untuk menggabungkan proses-proses agar tidak loncat ke proses sebelumnya
for i in kumpulan_proses:
    p.join()
## untuk mendapatkan waktu setelah eksekusi
process_akhir = time()
print()

# 3-Multiprocessing dengan Kelas Pool:
print("3-Multiprocessing dengan kelas Pool")
## untuk mendapatkan waktu sebelum eksekusi
pool_awal =  time()
## proses berlangsung
pool = Pool()
pool.map(cetak, range(0,10))
pool.close()
## untuk mendapatkan waktu setelah eksekusi
pool_akhir =  time()
print()

# Membandingkan Waktu Eksekusi:
print("Perbandingan Waktu Eksekusi")
print("Sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Kelas Process :", process_akhir - process_awal, "detik")
print("Kelas Pool :", pool_akhir - pool_awal, "detik")
