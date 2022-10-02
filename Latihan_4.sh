#!/bin/bash

a=0;
echo -n "Masukkan Angka: "
read input
until [ ! $input -gt $a ];
do
   echo $input " ";
   input=$((input-2))
done
