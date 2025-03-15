#HATALI YAPTIĞIM PROJE İLERDE DÜZELTMEYE ÇALIŞACAĞIM
#hatası belli bir txt'ye kaydedilecek ve title ile yazısı kayıt olacak ama title yazdığımda yeni txt oluşuyor dediğim gibi olmalı!

import os
import tkinter
from tkinter import PhotoImage, messagebox, Canvas
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

SAVE_PATH = "../../../PythonSecretNote"

os.makedirs(SAVE_PATH, exist_ok=True)

def save_file():
    title = title_entry.get().strip()
    content = content_text.get("1.0", tkinter.END).strip()
    secret = secret_entry.get().strip()  # Şifreyi alıyoruz

    if not title or not content or not secret:
        messagebox.showwarning("Uyarı", "Başlık, içerik ve şifre boş olamaz!")
        return

    file_path = os.path.join(SAVE_PATH, f"{title}.txt")

    # İçeriği şifreliyoruz
    message_encrypt = encode(secret, content)
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(message_encrypt)  # Şifreli içeriği kaydediyoruz
        messagebox.showinfo("Başarılı", f"Dosya kaydedildi:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya kaydedilirken bir hata oluştu:\n{e}")
    finally:
        title_entry.delete(0, tkinter.END)
        content_text.delete("1.0", tkinter.END)
        secret_entry.delete(0, tkinter.END)


def decrypt_notes():
    message_encrypted = content_text.get(1.0,tkinter.END).strip()
    master_secret = secret_entry.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0 :
        messagebox.showerror(title="Error",message="please enter all info")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            content_text.delete(1.0,tkinter.END)
            content_text.insert(1.0,decrypted_message)
        except:
            messagebox.showerror(title="Error",message="Decrypted text cannot be decoded again")



# Tkinter Penceresi
Screen = tkinter.Tk()
Screen.minsize(width=350, height=740)
Screen.title("Secret Notes Books")

# Resim ekleme
image = PhotoImage(file="output2.png")
image_label = tkinter.Label(Screen, image=image, width=200, height=200)
image_label.pack(padx=10, pady=10)

# İlk kısım (Başlık)
title_label = tkinter.Label(text="Enter your file title", font=('arial', 15, "normal"))
title_label.pack()
title_entry = tkinter.Entry(width=30)
title_entry.pack()

# İkinci kısım (İçerik)
content_label = tkinter.Label(text="Enter your secret content", font=('arial', 15, "normal"))
content_label.pack(padx=5, pady=5)
content_text = tkinter.Text(width=35, height=18)
content_text.pack()

# Üçüncü kısım (Şifre)
secret_label = tkinter.Label(text="Enter your password", font=('arial', 15, "normal"))
secret_label.pack()
secret_entry = tkinter.Entry(width=30, show="*")  # Şifre gizli olarak girilsin
secret_entry.pack()

# Kaydetme butonu
save_button = tkinter.Button(text="Save", width=20, command=save_file)
save_button.pack(padx=5, pady=5)

# Şifreyi çözme butonu
decrypt_btn = tkinter.Button(text="Decrypt", width=10, command=decrypt_notes)
decrypt_btn.pack(padx=5, pady=5)



Screen.mainloop()


'''
Foto ekleme farklı yolu 

photo = PhotoImage(file="foto.png")
photo_label = Label(image=photo)
photo_label.pack()

2.Yolu
photo = PhotoImage(file="foto.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image=photo)
'''
