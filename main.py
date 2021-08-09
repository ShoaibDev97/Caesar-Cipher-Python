# Declaring Variables 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
ceaser_type = input("Type 'encode' to Encrypt and 'decode' to Decrypt : ")
message = input("Type Your Message : ")
key = int(input("Enter Shift Key : "))

def ceaser_cipher(ceaser_type, message, key):
    ceaser_type = ceaser_type.lower()
    encode_message = []
    decode_message = []
    if ceaser_type == "encode":
        for letter in (message):
            if(letter == " " ):
                encode_message.append(letter)
            else:
                alphabet_index = alphabet.index(letter) + key
                if(alphabet_index > 25):
                    alphabet_index = alphabet_index % 26
                    
                encode_message.append(alphabet[alphabet_index])
    
        encodeStr = ''.join(map(str, encode_message))
        print(encodeStr)            

    elif ceaser_type == "decode":
        for letter in (message):
            if(letter == " "):
                decode_message.append(letter)
            else:
                alphabet_index = alphabet.index(letter) - key
                if(alphabet_index < 0):
                    alphabet_index = alphabet_index % 26
                
                decode_message.append(alphabet[alphabet_index])

        decodeStr = ''.join(map(str, decode_message))
        print(decodeStr)


ceaser_cipher(ceaser_type,message,key)

