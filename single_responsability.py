
def stringToAsciiArray(text):
    text_ascii_arr=[]
    for c in text:
        text_ascii_arr.append(ord(c))
    return text_ascii_arr

def reformatAscii(ascii_arr,key_value):
    ascii_reformat_arr=[]
    for text_ascii in ascii_arr:
        ascii_reformat_arr.append(text_ascii+key_value)
    return ascii_reformat_arr

def asciiArrToString(ascii_arr):
    mystring = ""
    for char in ascii_arr:
        mystring = mystring + chr(char)
    return mystring

def process_text(text, key):
    text_ascii_arr=stringToAsciiArray(text)
    procesed_text=reformatAscii(text_ascii_arr, key)
    return asciiArrToString(procesed_text)

def getInputs():
    encrypt_or_decrypt = input("Encryptar o Desencryptar: E/D ")
    clave = input("Clave para procesar: ")
    text = input("Texto a procesar: ")
    return encrypt_or_decrypt,clave,text 

def getKey(clave, encrypt_or_decrypt):
    asciiCount = 0
    key = 0
    for c in clave:
        asciiCount+= ord(c)
    asciiStrCount = str(asciiCount)
    for c in asciiStrCount:
        key+=int(c)
    while key>128:
        key=key//2
    if encrypt_or_decrypt == "E":
        return key
    return -key

def main ():
    encrypt_or_decrypt,clave,text=getInputs()
    key = getKey(clave, encrypt_or_decrypt)
    print(process_text(text, key))

main()