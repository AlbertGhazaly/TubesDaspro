import data

def summonjin():
    print('''
Jenis jin yang dapat dipanggil:
 (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
 (2) Pembangun - Bertugas membangun candi
''')

    panggil_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

    while panggil_jin != 1 and panggil_jin != 2:
        print("Tidak ada jenis jin bernomor " , str(panggil_jin), "!")
        panggil_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

    if panggil_jin == 1:
        print("Memilih jin Pengumpul.")
    else:
        print("Memilih jin Pembangun.")
    
    username_jin = input("Masukkan username jin: ")

    for i in range(1000) :
        if data.users[i][0] == username_jin : 
            print("Username ", username_jin, " sudah diambil!")
            username_jin = input("Masukkan username jin: ")
    
    for i in range(1000) :
        if data.users[i][0] == 0:
            data.users[i][0] = username_jin
            password_jin = input("Masukkan password jin: ")
            while len(password_jin) < 5 and len(password_jin) > 25:
                data.users[i][0] = password_jin
                print("Password panjangnya harus 5-25 karakter!")
                password_jin = input("Masukkan password jin: ")

            data.users[i][1] = password_jin
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print("Jin ", username_jin, "berhasil dipanggil!")
            break
