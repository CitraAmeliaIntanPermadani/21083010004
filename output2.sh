#!/bin/bash

a=55;
b=4;
distroLinux="UBuntu 19.04 LTS";
let c=a%b;

printf "OS : $distroLinux \n";
printf "$c \n";
printf "%.2f float \n" $a;
printf "%.1f float \n" $a;
