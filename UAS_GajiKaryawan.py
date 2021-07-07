"""
GAJI POKOK
Gaji pokok akan terisi dengan ketentuan jika golongan kerjanya:
- Golongan 1 = 2.500.000
- Golongan 2 = 4.500.000
- Golongan 3 = 6.500.000
TUNJANGAN ISTRI
- Tunjangan Istri diberikan hanya kepada pegawai berjenis kelamin “LAKI-LAKI” dan
“KAWIN”, dengan ketentuan:
- Jika pegawai itu ber- Golongan 1 = 1% dari Gaji Pokok
- Golongan 2 = 3% dari Gaji Pokok
- Golongan 3 = 5% dari Gaji Pokok

TUNJANGAN ANAK
Tunjangan Anak diberikan kepada semua pegawai yang sudah “KAWIN” dan PUNYA ANAK
sebesar 2% dari Gaji Pokok

GAJI BRUTO
- Gaji Bruto = Gaji Pokok + Tunjangan Anak + Tunjangan Istri

BIAYA JABATAN
- Biaya jabatan diambil sebesar 0.5% dari gaji bruto
IURAN PENSIUN
- Setiap karyawan membayar iuran Pensiun sebesar Rp. 15.500
IURAN ORGANISASI
- Setiap karyawan membayar iuran organisasi sebesar Rp.3.500.
GAJI NETTO
- Gaji Netto adalah gaji bersih yang diperoleh dari gaji bruto dikurangi iuran-iuran atau
biaya-biaya.

ALUR:
1. User menginputkan data pokok seperti Nama, golongan, jenis kelamin, dan status kawin.
2. Data pada no (1) digunakan untuk filter dalam menghitung syarat-syarat mendapatkan
nilai gaji pokok dst.
"""

import datetime
from time import process_time_ns

x = datetime.datetime.now()
ulang="y"
while ulang=="y" or ulang =="Y":
    print("========================================================")
    print("                     input Gaji Karyawan                 ")
    print("                     Tanggal : ",x.strftime("%x"))
    print("========================================================")


    golongan = ['1','2','3']
    gajipokok = ['2500000','4500000','6500000']

    nama = input("Nama                    =       ")
    g= input("Golongan                =       ")
    gol = int(g)
    if gol == 1 :
        idx = 0
        tunjangan = 0.01
    elif gol == 2:
        idx = 1
        tunjangan = 0.03
    elif gol == 3:
        idx = 2
        tunjangan = 0.05
    else :
        print("Masukkan kembali golongan dengan benar")

    print("Laki  Laki atau Perempuan")
    jenis_kelamin = input("Jenis kelamin           =      ")
    print("========================================================")
    print ("Kawin atau belum")
    status_kawin = input("status Kawin            =      ")
    print("========================================================")
    print ("Iya atau Tidak")
    status_anak = input("Apakah punya anak       =      ")

    #status
    if jenis_kelamin == "Laki Laki" or "Laki laki" or "laki laki" and status_kawin == "Kawin" or "kawin":
        tunjanganistri = int(gajipokok[idx]) * tunjangan
    else :
        tunjanganistri = 0
    #Anak
    if status_kawin == "Kawin" or "kawin" and status_anak == "Iya" or "iya":
        tunjangananak = int(gajipokok[idx]) * 0.02
    else :
        tunjangananak = 0
    #Bruto
    gajibruto = int(gajipokok[idx]) + int(tunjanganistri) + int(tunjangananak)

    #Jabatan
    biayajabatan = int(gajibruto) * 0.05

    #Pensiun
    iuran_pensiun = 15500

    #Organsasi
    iuran_organisasi = 3500

    #Net
    GajiNetto = int(gajibruto) - int(iuran_organisasi) - int(iuran_pensiun)
    

    print("========================================================")
    print("                     SLIP GAJI                  ")
    print("                   Tanggal : ",x.strftime("%x"))
    print("========================================================")

    print("Nama                     " + nama)
    print("Golongan                 " + str(gol))
    print("jenis kelamin            " + jenis_kelamin)
    print("Staus Kawin              " + status_kawin)
    print("Gaji Pokok               " + gajipokok[idx])
    print("Tunjangan istri          " + str(tunjanganistri))
    print("Tunjangan Anak           " + str(tunjangananak))
    print(">>Gaji bruto             " + str(gajibruto))
    print("========================================================")
    print("Biaya Jabatan            " + str(biayajabatan))
    print("Iuran Pensiun            " + str(iuran_pensiun))
    print("Iuran Organisasi         " + str(iuran_organisasi))
    print(">>Gaji Netto             " + str(GajiNetto))
    ulang = input(" Ulang program? y/t = ")
    if ulang=="t" or ulang=="T":
        break