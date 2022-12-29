import streamlit as st
    
    #program enkripsi dan deksripsi

#enkripsi merupakan suatu proses mengamankan informasi, agar informasi tidak dapat dibaca tanpa bantuan khusus.
#dekripsi merupakan suatu proses mencari informasi dengan bantuan khusus yaitu data hasil enkripsi.

#Rumus Enkripsi  : (n + key) % 26
#Rumus Deskripsi : (n - key) % 26

# n = merupakan urutan dari abjad yang input
# key = merupakan kunci enkripsi atau deskripsinya
# 26 = merupakan jumlah abjad

st.header("| Program Enkripsi & Deskripsi |")

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def enkripsi(abjad):
    global key
    pesan = input("Masukkan Isi : ") #input string yang akan di enkripsi
    key = int(input("Masukkan Kunci : ")) #kunci untuk pertukaran abjad ke enkripsi

    pesan = pesan.lower() #inputan string diubah ke huruf kecil agar sesuai dengan abjad
    result = ''

    for huruf in pesan: #membuat perulangan untuk pertukaran abjad
        if huruf in abjad: #memecah string 1 1 dan mengecek apakah ada velue didalam abjad
            n = abjad.index(huruf) #jika ada maka index abjad akan disimpan di variabel n
            enkripsi = (n + key) % 26 #rumus enkripsi
            convert = abjad[enkripsi] #mengkonversi nilai string ke dalam enkripsi
            result = result + convert
        else:
            result = result + ''
    print(f"result : {result}")

    with open('encrypted.txt', 'a') as file:
      file.write(f"{result} \n")

def deskripsi(abjad):
    pesan = input("Masukkan Isi : ") 
    key = int(input("Masukkan Kunci : "))

    pesan = pesan.lower()
    result = ''

    for huruf in pesan:
        if huruf in abjad:
            n = abjad.index(huruf)
            enkripsi = (n - key) % 26
            convert = abjad[enkripsi]
            result = result + convert
        else:
            result = result + ''
    print(f"result : {result}")

    with open('descripted.txt', 'a') as file:
      file.write(f"{result} \n")

#pgrogram utama
#menanyakan kepada user apakah ingin melakukan pengecekan kembali
# pilihan = 'y'
while (pilihan == 'y'): #akan diulang jika user menginput 'y'
    print("Pilih Menu yang tersedia : ")
    print("1. Menu Enkripsi")
    print("2. Menu Deskrpsi")
    print("3. Keluar")

    menu = input("Menu yang dipilih : ") #meminta user untuk memilih menu
    print("----------------------------------")

    if menu == '1':
      print(">>>[Enkripsi Data]<<<")
      enkripsi(abjad)
    elif menu == '2':
      print(">>>[Deskripsi Data]<<<")
      deskripsi(abjad)
    elif menu == '3':
      print("Program Selesai, terimakasih.")
      break
    else:
      print("Menu yang anda pilih tidak tersedia.")

    print("----------------------------------")
    pilihan = input("Apakah anda ingin melakukannya lagi? [y/t] : ")
    print("----------------------------------")


with open('encrypted.txt', 'r') as read_file:
  print(f"""
  Isi file Enkripsi adalah 
  - {read_file.read()}
  """)