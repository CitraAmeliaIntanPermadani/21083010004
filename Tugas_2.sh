#!/bin/bash

echo "PROGRAM ARITMATIKA"
echo "1. Penjumlahan"
echo "2. Pengurangan"
echo "3. Perkalian"
echo "4. Pembagian"
echo
echo "Silahkan Pilih program aritmatika di atas"
read pil
case "$pil" in
	"1")
	echo "Penjumlahan"
	echo "Masukkan nilai1: "
	read a
	echo "Masukkan nlai2: "
	read b
	let hasil=$a+$b
	echo "Hasilnya adalah $hasil"
	;;
	 "2")
        echo "Pengurangan"
        echo "Masukkan nilai1: "
        read a
        echo "Masukkan nlai2: "
        read b
        let hasil=$a-$b
        echo "Hasilnya adalah $hasil"
        ;;
	 "3")
        echo "Perkalian"
        echo "Masukkan nilai1: "
        read a
        echo "Masukkan nlai2: "
        read b
        let hasil=$a*$b
        echo "Hasilnya adalah $hasil"
        ;;
	 "4")
        echo "Pembagian"
        echo "Masukkan nilai1: "
        read a
        echo "Masukkan nlai2: "
        read b
        let hasil=$a/$b
        echo "Hasilnya adalah $hasil"
        ;;
esac
