from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

def encrypt_video():
    input_dir ='C:/Users/hp/Desktop/piCompressed'
    output_dir = 'C:/Users/hp/Desktop/piCompressedEncrypted'
    current_frame=0
    t= os.listdir(input_dir)
    t.sort(key=lambda x: int(x.split(".")[0][5:]))
    for frame in t:
        if frame.endswith('.jpg'):
                # Read image file
                filepath = os.path.join(input_dir, frame)
                print(filepath)
                # The original image file and the AES key
                #original_image_file = input_dir
                key = get_random_bytes(16)

                # Set up the AES cipher in CBC mode with a random IV
                iv = get_random_bytes(AES.block_size)
                cipher = AES.new(key, AES.MODE_CBC, iv=iv)

                # Open the original image
                with open(filepath, 'rb') as f:
                    original_data = f.read()

                # Convert the image to bytes and pad it
                padded_data = pad(original_data, AES.block_size)

                # Encrypt the image data
                encrypted_data = cipher.encrypt(padded_data)

                # Save the encrypted image with the IV appended to the file
                with open('C:/Users/hp/Desktop/piCompressedEncrypted/frame'+ str(current_frame)+'.bmp', 'wb') as f:
                    f.write(iv)
                    f.write(encrypted_data)
                with open("C:/Users/hp/Desktop/keys/key"+str(current_frame)+".bin", "wb") as f:
                    f.write(key)
                current_frame+=1