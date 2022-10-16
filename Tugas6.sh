 #!/bin/bash

declare -a jumlahIPS
read -p "Masukkan Jumlah IPS: " jumlahIPS

declare -a nilaiIPS
read -p "Masukkan Nilai IPS: " nilaiIPS

for i in ${nilaiIPS[@]}
do
	echo $i
	if [ $i -ge 0 ]
	then
		((JmlhIPS=$jumlahIPS))
		((totIPS=$totIPS + $i))
	fi
	((IPK=$totIPS/$jumlahIPS))

done
echo "IPK mhs= $totIPS/$jumlahIPS"
echo "IPK mhs= $IPK"
