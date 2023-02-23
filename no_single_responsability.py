# Premisa, hacer un codigo para encriptar y desencriptar segun la clave dada 

def encryp_or_decrypt(encrypt_or_decrypt):
    asciiCount = 0
    for c in clave:
        asciiCount+= ord(c)
    asciiStrCount = str(asciiCount)

    key=0
    for c in asciiStrCount:
        key+=int(c)
    while key>128:
        key=key//2
    textAsciiArr=[]

    for c in text:
        textAsciiArr.append(ord(c))
    if encrypt_or_decrypt == "E":
        encrypted_ascii_text_arr=[]
        for textAscii in textAsciiArr:
            encrypted_ascii_text_arr.append(textAscii+key)

        mystring = ""
        for char in encrypted_ascii_text_arr:
            mystring = mystring + chr(char)
        print(mystring)
    elif encrypt_or_decrypt == "D":
        decrypted_ascii_text_arr=[]
        for textAscii in textAsciiArr:
            decrypted_ascii_text_arr.append(textAscii-key)

        mystring = ""
        for char in decrypted_ascii_text_arr:
            mystring = mystring + chr(char)
        print(mystring)




encrypt_or_decrypt = input("Encryptar o Desencryptar: E/D ")
clave = input("Clave para procesar: ")
text = input("Texto a procesar: ")
encryp_or_decrypt(encrypt_or_decrypt)

