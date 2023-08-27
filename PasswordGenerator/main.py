import customtkinter as ct
import random
import json


app = ct.CTk()


with open('settings.json') as setting:
    settings_data = json.load(fp=setting)


def slider_command(value):
    label_info_length.configure(text=int(value))


def generate_password():
    length = int(slider.get())
    characters = settings_data['characters']
    password = ''.join(random.choices(characters, k=length))
    label_password.configure(text=password)


app.geometry('470x270')
app.resizable(False, False)
app.title("Password generator")


slider_frame = ct.CTkFrame(app, width=460, height=50)
slider_frame.pack(side='bottom' ,pady=5)
slider_label = ct.CTkLabel(slider_frame, text='Password Length:  ', font=('Arial', 12))
slider_label.pack(side='left')
slider = ct.CTkSlider(slider_frame,command=slider_command, from_=1, to=settings_data['max_password_length'])
slider.pack(side='left')


label_info_length = ct.CTkLabel(slider_frame, text='20')
label_info_length.pack(side='left', pady=20)


btn_generate = ct.CTkButton(app, text='Generate', width=140, height=40, command=generate_password)
btn_generate.pack(side='bottom', pady=15)


pass_frame = ct.CTkFrame(app, width=460, height=100)
pass_frame.pack(anchor='n', pady=5)
label_password = ct.CTkLabel(pass_frame, text='hello', width=460, height=100, font=('Arial', 18))
label_password.pack()

app.mainloop()
