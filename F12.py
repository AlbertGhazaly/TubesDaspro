import save

def ayamberkokok() :
    print("Kukuruyuk.. Kukuruyuk..")
    jumlah_candi = save.hitung_candi() #Memanggil Fungsi hitung_candi untuk menghitung jumlah candi 
    if jumlah_candi < 100 :
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        exit()
    else :
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        exit()