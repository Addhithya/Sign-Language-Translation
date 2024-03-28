import tkinter as tk
import customtkinter as ct
from PIL import Image, ImageTk


# Create tkinter window
app = ct.CTk()
app.title('Sign Language')
ct.set_appearance_mode("light")

app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), 650))
app.resizable(width=False, height=False)


def print1():
    print('hello')


frame1 = ct.CTkFrame(master=app, width=2900, height=150, corner_radius=10, fg_color='#191970')
frame1.place(relx=0, rely=0, anchor=tk.CENTER)

l2 = ct.CTkLabel(master=app, text="SignCraft", font=('Microsoft Sans Serif', 35), text_color='white',bg_color='#191970')
l2.place(relx=0.07, rely=0.05, anchor=tk.CENTER)

button1 = ct.CTkButton(master=app, width=100, text="login", command=print1, corner_radius=20,height=35,font=("Arial", 20),fg_color='#FF5733',bg_color='#191970')
button1.place(relx=0.86, rely=0.06, anchor=tk.CENTER)

button1 = ct.CTkButton(master=app, width=100, text="signUp", command=print1, corner_radius=20,height=35,font=("Arial", 20),fg_color='#FF5733',bg_color='#191970')
button1.place(relx=0.95, rely=0.06, anchor=tk.CENTER)








frame = ct.CTkFrame(master=app, width=600, height=400, corner_radius=10, fg_color='white')
frame.place(relx=0.37, rely=0.5, anchor=tk.CENTER)

combobox = ct.CTkComboBox(master=app,
                                     values=["English",
    "Mandarin Chinese",
    "Spanish",
    "Hindi",
    "Arabic",
    "Bengali",
    "Portuguese",
    "Russian",
    "Japanese",
    "French"])
combobox.place(relx=0.9, rely=0.19, anchor=tk.CENTER)
combobox.set("English")

chat_frame = ct.CTkFrame(master=app, width=420, height=430, corner_radius=10,fg_color='white',border_color='black',border_width=3)
chat_frame.place(relx=0.8, rely=0.55, anchor=tk.CENTER)



button1 = ct.CTkButton(master=app, width=180, text="Translate", command=print1, corner_radius=10,height=40,font=("Arial", 20))
button1.place(relx=0.37, rely=0.9, anchor=tk.CENTER)



app.mainloop()



