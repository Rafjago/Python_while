print("===== PILIH PROGRAM =====")
print("1. Mencari genap")
print("2. Mencari ganjil")
print("0. Keluar")

while True:
    pilihan = input("Ketik angka untuk memilih program: ")

    if pilihan == "1":
        while True:
            print("\n===== PROGRAM GENAP =====")

            awal = int(input("Ketik nilai awal = "))
            selisih = int(input("Ketik nilai selisih = "))
            akhir = int(input("Ketik nilai akhir = "))

            while awal <= akhir:
                if awal % 2 == 0:
                    print(awal)

                awal += selisih

            print("\n1. Hitung lagi")
            print("2. Kembali ke halaman sebelumnya")

            pilih = input("Pilih = ")

            if pilih == "2":
                break

    elif pilihan == "2":
        while True:
            print("\n===== PROGRAM GANJIL =====")

            awal = int(input("Ketik nilai awal = "))
            selisih = int(input("Ketik nilai selisih = "))
            akhir = int(input("Ketik nilai akhir = "))

            while awal <= akhir:
                if awal % 2 != 0:
                    print(awal)

                awal += selisih

            print("\n1. Hitung lagi")
            print("2. Kembali ke halaman sebelumnya")

            pilih = input("Pilih = ")

            if pilih == "2":
                break

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Tolong pilih 0, 1, atau 2!")
