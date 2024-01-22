import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
import os
import pywt
import threading
def decompress_video():
    input_dir = 'C:/Users/hp/Desktop/piDecrypted'
    output_dir = 'C:/Users/hp/Desktop/piDecrypted_Decompressed'
    current_frame = 0
    t= os.listdir(input_dir)
    t.sort(key=lambda x: int(x.split(".")[0][5:]))
    for frame in t:
            if frame.endswith('.jpg'):
                # Read image file
                filepath = os.path.join(input_dir, frame)
                print(filepath)

                A = imread(filepath)
                B = np.mean(A, -1); # Convert RGB to grayscale

                ## Wavelet Compression
                n = 5
                w = 'db1'
                coeffs = pywt.wavedec2(B,wavelet=w,level=n)

                coeff_arr, coeff_slices = pywt.coeffs_to_array(coeffs)

                Csort = np.sort(np.abs(coeff_arr.reshape(-1)))

                keep = 0.1
                thresh = Csort[int(np.floor((1-keep)*len(Csort)))]
                ind = np.abs(coeff_arr) > thresh
                Cfilt = coeff_arr * ind # Threshold small indices
                    
                coeffs_filt = pywt.array_to_coeffs(Cfilt,coeff_slices,output_format='wavedec2')

                    # Perform inverse DWT on filtered coefficients
                Arecon = pywt.waverec2(coeffs_filt,wavelet=w)

                    # Plot and save reconstructed image  
                name = f"{output_dir}/frame{current_frame}.jpg"
                plt.imsave(name, Arecon.astype('uint8'), cmap='gray')
                current_frame += 1

def decompress_video_thread():
    """
    This function runs the compress_video() function in a separate thread.
    """
    t = threading.Thread(target=decompress_video)
    t.start()

def on_decompress_button_click():
    """
    This function is called when the user clicks the compress button.
    """
    decompress_video_thread()