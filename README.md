IPv4Scanner adalah script python sederhana yang berfungsi untuk melakukan scanning IPv4 Address yang ada diseluruh dunia kemudian melakukan deteksi port yang terbuka di port 80 pada IP address tersebut.

OS yang saya rekomendasikan untuk menggunakan script ini adalah Kali Linux (alternatif bisa menggunakan Virtual Machine)


Script ini menggunakan modul Python nmap.
Anda harus menginstal yang berikut ini untuk membuatnya bekerja di Kali Linux:

Langkah 1: Sudo apt install python3-pip

Langkah 2: pip install python-nmap

Langkah 3: python3 ipscanner.py

Cara kerja dari script ini adalah dengan memanfaatkan fitur PortScanner yang ada pada modul Python Nmap.

Range IP yang disearch adalah 0.0.0.0 s.d. 239.255.255.255

Dari semua IP Address yang berhasil didapatkan oleh fungsi scanner host pada nmap, script akan melanjutkan dengan melakukan pembacaan pada port 80 pada IP Address tersebut.

IPv4 Address yang memiliki port yang terbuka pada port 80 kemudian akan ditampilkan pada output script.

Note : Eksekusi dari script ini memakan waktu sekitar 18~20 detik

Cara alternatif : 

Menggunakan perintah dari modul yang sudah built-in pada Kali Linux yaitu masscan

Perintah : sudo  masscan 0.0.0.0/0 -p80 --max-rate 100000 --exclude 255.255.255.255

Range IP yang disearch adalah 0.0.0.0 s.d. 239.255.255.255

Dari semua IP Address yang berhasil didapatkan pada masscan, script akan melanjutkan dengan melakukan pembacaan pada port 80 pada IP Address tersebut.

IPv4 Address yang memiliki port yang terbuka pada port 80 kemudian akan ditampilkan pada output script.

Note : Eksekusi dari script ini memakan waktu sekitar 18~ jam

