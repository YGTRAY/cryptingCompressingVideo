from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# The encrypted image file and the AES key
input_dir_img ='C:/Users/hp/Desktop/piCompressedEncrypted'
output_dir = 'C:/Users/hp/Desktop/piDecrypted'

def decrypt_video():
    currentframe = 0
    i = 0
    t= os.listdir(input_dir_img)
    t.sort(key=lambda x: int(x.split(".")[0][5:]))
    for frame in t: 
    
        
        with open('C:/Users/hp/Desktop/keys/key'+str(i)+'.bin', "rb") as d:
            key = d.read()
           

        # Read the encrypted image data and IV from the file
        with open('C:/Users/hp/Desktop/piCompressedEncrypted/frame'+str(i)+'.bin', 'rb') as f:
            iv = f.read(AES.block_size)
            encrypted_data = f.read()

        # Set up the AES cipher in CBC mode with the saved IV
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)

        # Decrypt the image data and unpad it
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        # Write the decrypted image data to a new file
        with open('C:/Users/hp/Desktop/piDecrypted/frame'+str(currentframe)+'.jpg', 'wb') as f:
            f.write(decrypted_data)
        currentframe+=1
        i+=1