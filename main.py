import tkinter as tk
from tkinter import filedialog



import slice
import Compression
import cryptage
import merge
import decrytage
import decompression







# Set up the GUI window
root = tk.Tk()
root.title("Video Compression and Encryption")
root.geometry("1440x720")




# Label to show the decryption output
decryption_output = tk.Label(root, text="")
decryption_output.pack()

info_title = tk.Label(root, text="Informations sur l'application :", font=('Helvetica', 18,'bold'),fg='red')
info_title.place(relx=0.005, rely=0.05)

# Add a text area for app information
info_frame = tk.Frame(root, bg='gray')
info_frame.place(relx=0.005, rely=0.1, relwidth=0.4, relheight=0.4)

info_text = tk.Text(info_frame, font=('Helvetica', 10), bg=root.cget('bg'))
info_text.pack(fill='both', expand=True)
info_text.insert('end', "Bienvenue dans l'application de compression et de chiffrement de vidéo!\n\n") 
info_text.insert('end', 'Cette application vous permet de compresser et de chiffrer vos fichiers vidéo pour réduire leur taille. \n\n')
info_text.insert('end', 'Pour commencer,cliquez sur le bouton "Sélectionner un fichier" et choisissez le fichier vidéo que    vous souhaitez compresser et chiffrer.\n\n')
info_text.insert('end', 'Une fois que la vidéo est compressée et chiffrée, vous pouvez utiliser le bouton "Décompresser et   déchiffrer" pour revenir aux modifications précédentes.\n\n')
info_text.insert('end', 'Veuillez noter que le processus de compression et de chiffrement peut prendre du temps en          fonction de la taille de votre fichier vidéo.\n\n')


# Function to open a file dialog and select a video file
def select_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Sélectionner un fichier", filetypes=(("MP4 files", "*.mp4"), ("all files", "*.*")))
    file_entry_1.insert(0, filename)

# Label for entering the filename
file_label = tk.Label(root, text="Entrez le nom du fichier vidéo que vous souhaitez compresser et chiffrer:",font=('Helvetica', 14,'bold'),fg='blue')
file_label.place(relx=0.43, rely=0.1, anchor='w', x=50)
file_entry_1 = tk.Entry(root, width=40)
file_entry_1.pack()
file_entry_1.place(relx=0.434, rely=0.14, anchor='w', x=50)

# Button to select the video file
select_file_button = tk.Button(root, text="Sélectionner un fichier", command=select_file,width=20)
select_file_button.pack()
select_file_button.place(relx=0.434, rely=0.19, anchor='w', x=50)

# Button to split the video file
select_file_button = tk.Button(root, text="Diviser la vidéo",width=20, command=slice.on_split_button_click)
select_file_button.pack()
select_file_button.place(relx=0.434, rely=0.25, anchor='w', x=50)


# Button to compress the video
compress_button = tk.Button(root, text="Compresser la vidéo",width=20, command=Compression.on_compress_button_click)
compress_button.pack()
compress_button.place(relx=0.434, rely=0.31, anchor='w', x=50)

# Button to encrypt the video
encrypt_button = tk.Button(root, text="Chiffrer la vidéo",width=20, command=cryptage.encrypt_video)
encrypt_button.pack()
encrypt_button.place(relx=0.434, rely=0.37, anchor='w', x=50)

# Button to merge the video file
select_file_button = tk.Button(root, text="Fusionner la vidéo",width=20, command= merge.merge_video)
select_file_button.pack()
select_file_button.place(relx=0.434, rely=0.43, anchor='w', x=50)

# Function to open a file dialog and select a video file
def selecte_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Sélectionner un fichier", filetypes=(("MP4 files", "*.mp4"), ("all files", "*.*")))
    file_entry_2.insert(0, filename)


# Label for entering the filename
file_label = tk.Label(root, text="Entrez le nom du fichier vidéo que vous souhaitez déchiffrer et décompresser:",font=('Helvetica', 14,'bold'),fg='blue')
file_label.place(relx=0.43, rely=0.53, anchor='w', x=50)
file_entry_2 = tk.Entry(root, width=40)
file_entry_2.pack()
file_entry_2.place(relx=0.434, rely=0.57, anchor='w', x=50)

# Button to select the video file
select_file_button = tk.Button(root, text="Sélectionner un fichier", command=selecte_file,width=20)
select_file_button.pack()
select_file_button.place(relx=0.434, rely=0.63, anchor='w', x=50)

# Button to merge the video file
select_file_button = tk.Button(root, text="Diviser la vidéo",width=20)
select_file_button.pack()
select_file_button.place(relx=0.434, rely=0.69, anchor='w', x=50)

# Button to decrypt the video
decrypt_button = tk.Button(root, text="Déchiffrer la vidéo",width=20, command=decrytage.decrypt_video)
decrypt_button.pack()
decrypt_button.place(relx=0.434, rely=0.75, anchor='w', x=50)

# Button to decompress the video
decompress_button = tk.Button(root, text="Décompresser la Video",width=20, command=décompression.on_decompress_button_click)
decompress_button.pack()
decompress_button.place(relx=0.434, rely=0.81, anchor='w', x=50)

# Button to merge the video file
select_file_button = tk.Button(root, text="Fusionner la vidéo",width=20, command= merge.on_merge_button_click)
select_file_button.pack()
select_file_button.place(relx=0.434, rely=0.87, anchor='w', x=50)

root.mainloop()