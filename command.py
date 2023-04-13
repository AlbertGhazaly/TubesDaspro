import data
import save
import F01
from F02 import logout
from F03 import summonjin
from F04 import hapusjin
from F05 import ubahjin
import F06
import F07
import F08
from F09 import laporanjin 
from F10 import laporancandi
from F11 import hancurkancandi
from F12 import ayamberkokok
import F14
import F15
from F16 import exit


def run(command : str) :
    if data.login_status == "false" :    
        if command == "login" : #fungsi login (F01)
            if data.login_status == "false": #login dapat dilakukan jika dia belum login
                F01.login()
            else : #jika dia sudah login maka login akan gagal
                print("Login gagal")
                print(f"Anda telah login dengan username {data.usernamee}, silahkan logout terlebih dahulu sebelum melakukan login kembali")
        elif command == "help" : #fungsi help (F15)
            F15.help()
        elif command == "exit" : #fungsi exit (F16)
            exit()
        else :
            print("Silahkan login dahulu untuk mengakses fungsi tersebut")
    else :
        if command == "login" : #fungsi login (F01)
            if data.login_status == "false": #login dapat dilakukan jika dia belum login
                F01.login()
            else : #jika dia sudah login maka login akan gagal
                print("Login gagal")
                print(f"Anda telah login dengan username {data.usernamee}, silahkan logout terlebih dahulu sebelum melakukan login kembali")
        elif command == "logout" : #fungsi logout (F02)
            if data.login_status == "true" : #logout dapat dilakukan jika dia telah login
                logout()
            else : #jika dia belum login maka logout akan gagal
                print("Logout gagal")
                print(f"Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        elif command == "summonjin" :#fungsi summonjin (F03)
            if data.role == "bandung_bondowoso" : #jika role = bandung_bondowoso maka dapat memiliki akses dan dapat mengakses fungsi
                jin_pengumpul = save.hitung_jin("pengumpul")
                jin_pembangun = save.hitung_jin("pembangun")
                total_jin = jin_pengumpul + jin_pembangun
                if total_jin > 100 : #jika jumlah jin sudah 100 maka tidak bisa dilanjutkan
                    print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
                else :
                    summonjin()
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "hapusjin" : #fungsi menghapus jin (F04)
            if data.role == "bandung_bondowoso" : #jika role = bandung_bondowoso maka dapat memiliki akses dan dapat mengakses fungsi
                hapusjin()
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "ubahjin" : #fungsi mengubah role jin (F05)
            if data.role == "bandung_bondowoso" : #jika role = bandung_bondowoso maka dapat memiliki akses dan dapat mengakses fungsi
                ubahjin()
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "bangun" : #fungsi membagun candi (F06)
            if data.role == "pembangun" :
                F06.bangun()
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "kumpul" : #fungsi mengumpulkan bahan candi (F07)
            if data.role == "pengumpul" :
                F07.kumpul()
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "batchkumpul" : #fungsi batch kumpul (F08)
            if data.role == "bandung_bondowoso" : #jika role = bandung_bondowoso maka dapat memiliki akses dan dapat mengakses fungsi
                F08.batchkumpul()
            else :
                ("Maaf anda tidak memiliki akses")
        elif command == "batchbangun" : #fungsi batch bangun (F08)
            if data.role == "bandung_bondowoso" : #jika role = bandung_bondowoso maka dapat memiliki akses dan dapat mengakses fungsi
                F08.batchbangun()
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "laporanjin" :
            if data.role == "bandung_bondowoso" : #jika role = bandung_bondowoso maka dapat memiliki akses dan dapat mengakses fungsi
                laporanjin()
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "laporancandi" :
            if data.role == "bandung_bondowoso" : #jika role = bandung_bondowoso maka dapat memiliki akses dan dapat mengakses fungsi
                laporancandi()
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "hancurkancandi" :
            if data.role == "roro_jonggrang" : #jika role = roro_jonggrang maka dapat memiliki akses dan dapat mengakses fungsi
                hancurkancandi()
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "ayamberkokok" :
            if data.role == "roro_jonggrang" : #jika role = roro_jonggrang maka dapat memiliki akses dan dapat mengakses fungsi
                ayamberkokok()
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "save" :
            if data.role == "bandung_bondowoso" or data.role == "roro_jonggrang" : #jika role = bandung_bondowoso atau roro_jonggrang maka dapat memiliki akses dan dapat mengakses fungsi
                folder_name = input("Masukkan nama folder: ")
                data.load_folder_name = folder_name
                F14.save("user.csv", data.users, 3, 101)
                F14.save("bahan_bangunan.csv", data.bahan_bangunan, 2, 4)
                F14.save("candi.csv", data.candi, 4, 101)
            else :
                ("Maaf anda tidak memiliki akses") #username tidak memiliki akses ke fungsi
        elif command == "help" : #fungsi help (F15)
            F15.help()
        elif command == "exit" : #fungsi exit (F16)
            exit()