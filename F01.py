import data

def login() :
    username = input("Username : ") #meminta masukkan username
    password = input("Password : ") #meminta masukkan password
    data.usernamee = username
    u_found = False
    p_found = False
    # iterate over the rows in the users list
    
    #mengecek apakah akun tersebut ada atau tidak, jika tidak, login gagal
    for i in range(1000):
        # check if the username and password match
        if username == data.users[i][0]:
            if password == data.users[i][1]:
                u_found = True  
                p_found = True
                data.login_status = "true"
                data.role = data.users[i][2]
            else:
                u_found = True  
                p_found = False


    if u_found == True and p_found == True :
        print(f"Selamat datang, {username}!")
        print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
    elif u_found == True and p_found == False :
        print("Password salah!")
    elif u_found == False :
        print("Username tidak terdaftar")
