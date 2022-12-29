import streamlit as st

st.header(' Program Enkripsi & Deskripsi ')

user_input = st.text_input("Masukkan data yang ingin di enkripsi").lower()

user_input_key = int(st.number_input("Masukkan Key"))

abjad =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

result = ''

for huruf in user_input: 
  if huruf in abjad: 
      n = abjad.index(huruf)
      enkripsi = (n + user_input_key) % 26
      convert = abjad[enkripsi]
      result = result + convert
  else:
      result = result + ''

with open('encrypted.txt', 'a') as file:
  file.write(f"{result} \n")



if st.button("Hasil Enkripsi"):
   st.success(f"hasil Enkripsi dari {user_input.capitalize()} adalah :  {result}")

page = """
<style>
.main{
     background-image: url("https://i.ytimg.com/vi/DlzRUDrN3ug/maxresdefault.jpg");
     background-size: cover;
     background-position: center;
}

.egzxvld2{
  background: #0000005d;
}
</style>
"""

st.markdown(page, unsafe_allow_html=True)