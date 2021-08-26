IPv4Scanner adalah script python sederhana yang berfungsi untuk melakukan scanning IPv4 Address yang ada diseluruh dunia kemudian melakukan deteksi port yang terbuka di port 80 pada IP address tersebut.

OS yang saya rekomendasikan untuk menggunakan script ini adalah Kali Linux (alternatif bisa menggunakan Virtual Machine)

Script ini menggunakan modul Python nmap.

Pengguna harus menginstal modul berikut ini untuk membuatnya bekerja di Kali Linux:

Sudo apt install python3-pip

pip install python-nmap

Jika instalasi selesai pengguna dapat menjalankan perintah berikut : 

python3 ipscanner.py

Cara kerja : 

script ini memanfaatkan fitur PortScanner yang ada pada modul Python Nmap.

Range IP yang disearch adalah 0.0.0.0 s.d. 239.255.255.255

Dari semua IP Address yang berhasil didapatkan oleh fungsi scanner host pada nmap, script akan melanjutkan dengan melakukan pembacaan pada port 80 pada IP Address tersebut.

IPv4 Address yang memiliki port yang terbuka pada port 80 kemudian akan ditampilkan pada output script.

Note : Eksekusi dari script ini memakan waktu sekitar 18~20 detik

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Cara alternatif : 

Menggunakan perintah dari modul yang sudah built-in pada Kali Linux yaitu masscan

Jika pengguna tidak menggunakan Kali Linux dapat mengikuti perintah instalasi berikut :

sudo apt-get --assume-yes install git make gcc

git clone https://github.com/robertdavidgraham/masscan

cd masscan

make

make -j

Jika instalasi selesai pengguna dapat menjalankan perintah berikut : 

sudo  masscan 0.0.0.0/0 -p80 --max-rate 100000 --exclude 255.255.255.255

Cara kerja : 

Perintah diatas akan menjalankan modul masscan untuk melakukan scanning seluruh IPv4 address yang ada di seluruh dunia.

Dari semua IP Address yang berhasil didapatkan pada masscan, script akan melanjutkan dengan melakukan pembacaan pada port 80 pada IP Address tersebut.

IPv4 Address yang memiliki port yang terbuka pada port 80 kemudian akan ditampilkan pada output script.

Note : Eksekusi dari script ini memakan waktu sekitar 18~ jam tergantung dari kecepat rate paket/detik yang digunakan

