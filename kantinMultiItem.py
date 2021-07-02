"""

AYATULLOH AL KURSI/20083000116/2E
Kantin Multi Item

"""
ulang="y"
while ulang=="y" or ulang =="Y":
    mkn = input("Ingin Memesan Makanan? y/t = ")
    if mkn == "Y" or mkn == "y":
        print("|================ MENU MAKANAN ================|")
        print("|                                              |")
        print("| A). Nasi Goreng        : Rp. 15.000          |")
        print("| B). Lontong Goreng     : Rp. 14.900          |")
        print("| C). Bakso Goreng       : Rp. 12.900          |")
        print("| D). Rujak Goreng       : Rp. 13.000          |")
        print("| E). Rujak Bakso        : Rp. 15.000          |")
        print("| F). Rujak Bakso Pecel  : Rp. 17.000          |")
        print("|==============================================|")
        kode = ['a', 'b', 'c', 'd', 'e', 'f']
        namamkn = ["Nasi Goreng", "Lontong Goreng", "Bakso Goreng", "Rujak Goreng", "Rujak Bakso", "Rujak Bakso Goreng"]
        harga = [15000,14900,12900,13000,15000,17000]
        pilihanmkn = input("Masukan Kode Makanan = ")
        qtymkn     = input("Masukkan Jumlah Makanan  = ")
        ##cek nama barang dan ambil harga satuan
        i = 0
        while i<len(namamkn):
            #jika value pada list kode[i] == pilihan
            if kode[i] == pilihanmkn:
                #ambil nama barang
                nm_mkn = namamkn[i]
                #ambil harga satuan
                hrgsat = harga[i]
            #jika tidak cocok, lanjut ke i berikutnya
            i+=1
        tot_byr = hrgsat * int(qtymkn)

        print(">>> NAMA MAKANAN      : " + nm_mkn)
        print(">>> HARGA MAKANAN     : " + str(hrgsat))
        print(">>> JUMLAH MAKANAN    : " + qtymkn)
        print(">>> TOTAL BAYAR MAKANAN      : " + str(tot_byr))
        minum = input("Apakan Ingin Memesan Minuman? y/t= ")
        if minum == "y" or minum =="y":
            print("|================ MENU MINUMAN ================|")
            print("|                                              |")
            print("| A). Teh Dingin/Panas   : Rp. 2.500           |")
            print("| B). Kopi Dingin        : Rp. 5.000           |")
            print("| C). Kopi Teh Panas     : Rp. 6.500           |")
            print("| D). Coca-Cola Dingin   : Rp. 3.500           |")
            print("| E). Coca-Cola Panas    : Rp. 5.000           |")
            print("|                                              |")
            print("|----------------------------------------------|")
            kodeminum = ['a', 'b', 'c', 'd', 'e']
            namamnm = ["Teh Dingin/Panas", "Kopi Dingin", "Kopi Teh Panas", "Coca-Cola Dingin", "Coca-Cola Panas"]
            hargamnm = [2500,5000,6500,3500,5000]
            pilihanminum = input("Masukan Kode Minuman = ")
            qtyminum = input("Masukkan Jumlah Minuman  = ")
            ##cek nama barang dan ambil harga satuan
            l = 0
            while l<len(namamnm):
                #jika value pada list kode[l] == pilihan
                if kodeminum[l] == pilihanminum:
                    #ambil nama barang
                    nm_mnm = namamnm[l]
                    #ambil harga satuan
                    hrgsatminum = hargamnm[l]
                #jika tidak cocok, lanjut ke l berikutnya
                l+=1
            tot_byrminum = hrgsatminum * int(qtyminum)
            
            print(">>> NAMA MINUMAN      : " + nm_mnm)
            print(">>> HARGA MINUMAN     : " + str(hrgsatminum))
            print(">>> JUMLAH MINUMAN    : " + qtyminum)
            print(">>> TOTAL BAYAR MINUMAN      : " + str(tot_byrminum))
            #Total Tagihan
            totBayar = tot_byr + tot_byrminum
            print(">>> TOTAL Pembayaran       : " + str(totBayar))

            ulang = input(" Ulang program? y/t = ")
            if ulang=="t" or ulang=="T":
                break

        elif minum=="t" or minum=="T" :
            totBayar = tot_byr
            print(">>> TOTAL Pembayaran       : " + str(totBayar))

            ulang = input(" Ulang program? y/t = ")
            if ulang=="t" or ulang=="T":
                break
    
    elif mkn == "t" or mkn == "T":
        minum = input("Apakan Ingin Memesan Minuman? y/t= ")
        if minum == "y" or minum =="y":
            print("|================ MENU MINUMAN ================|")
            print("|                                              |")
            print("| A). Teh Dingin/Panas   : Rp. 2.500           |")
            print("| B). Kopi Dingin        : Rp. 5.000           |")
            print("| C). Kopi Teh Panas     : Rp. 6.500           |")
            print("| D). Coca-Cola Dingin   : Rp. 3.500           |")
            print("| E). Coca-Cola Panas    : Rp. 5.000           |")
            print("|                                              |")
            print("|----------------------------------------------|")

            kodemnm = ['a', 'b', 'c', 'd', 'e']
            namamnm = ["Teh Dingin/Panas", "Kopi Dingin", "Kopi Teh Panas", "Coca-Cola Dingin", "Coca-Cola Panas"]
            hargamnm = [2500,5000,6500,3500,5000]
            pilihanminum = input("Masukan Kode Minuman = ")
            qtyminum = input("Masukkan Jumlah Minuman  = ")
            ##cek nama barang dan ambil harga satuan
            l = 0
            while l<len(namamnm):
                #jika value pada list kode[l] == pilihan
                if kodemnm[l] == pilihanminum:
                    #ambil nama barang
                    nm_mnm = namamnm[l]
                    #ambil harga satuan
                    hrgsatminum = hargamnm[l]
                #jika tidak cocok, lanjut ke l berikutnya
                l+=1
            tot_byrminum = hrgsatminum * int(qtyminum)
            
            print(">>> NAMA MINUMAN      : " + nm_mnm)
            print(">>> HARGA MINUMAN     : " + str(hrgsatminum))
            print(">>> JUMLAH MINUMAN    : " + qtyminum)
            print(">>> TOTAL BAYAR MINUMAN      : " + str(tot_byrminum))
            #Total Tagihan
            totBayar = tot_byrminum
            print(">>> TOTAL Pembayaran       : " + str(totBayar))
            ulang = input(" Ulang program? y/t = ")
            if ulang=="t" or ulang=="T":
                break

        elif minum=="t" or minum=="T" :
            print(">>> PESAN       : Pulang saja sana")

            ulang = input(" Ulang program? y/t = ")
            if ulang=="t" or ulang=="T":
                break

