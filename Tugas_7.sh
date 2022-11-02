#!/bin/bash

# Mendeklarasikan Fungsi
panjang() {
       echo "Masukkan Panjang:"
       read panjang
       echo " "
       lebar
}
lebar() {
       echo "Masukkan Lebar:"
       read lebar
       echo " "
       luas_persegi
}
luas_persegi() {
       let  luas_persegi=$panjang*$lebar
       echo -e "Luas Persegi:"
       echo -e "$luas_persegi"
}

# Memanggil Fungsi
panjang
