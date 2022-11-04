def main():
    import os
    import time
    print('-' * 22)
    print("--- Selamat Datang ---")
    print('-' * 22)
    print("Silahkan Pilih Operasi")
    print("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Exit")
    m = input('Pilihan: ')

    if(m == '1'):
        x = eval(input('Angka pertama: '))
        y = eval(input('Angka kedua: '))
        z = x+y
        print("Hasil penjumlahannya adalah: ", z)
        time.sleep(3)
        os.system('cls')
        main()
    elif(m == '2'):
        x = eval(input('Angka pertama: '))
        y = eval(input('Angka kedua: '))
        z = x-y
        print("Hasil pengurangannya adalah: ", z)
        time.sleep(3)
        os.system('cls')
        main()
    elif(m == '3'):
        x = eval(input('Angka pertama: '))
        y = eval(input('Angka kedua: '))
        z = x*y
        print("Hasil perkaliannya adalah: ", z)
        time.sleep(3)
        os.system('cls')
        main()
    elif(m == '4'):
        x = eval(input('Angka pertama: '))
        y = eval(input('Angka kedua: '))
        z = x/y
        print("Hasil pembagiannya adalah: ", z)
        time.sleep(3)
        os.system('cls')
        main()
    elif(m == '5'):
        os.system('cls')
        exit()
    else:
        print("Pilihan tidak ada")
        main()

def exit():
    pass

main()