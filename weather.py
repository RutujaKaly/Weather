from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    api_key = "61ebd483a0518071866f59f4ed2ebe9f"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()  
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)))  
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("My Weather  ")
win.config(bg="#87CEEB") 
win.geometry("500x480")


name_label = Label(win, text="⛅My Weather⛅", font=("Comic Sans MS", 30, "bold"), bg="#87CEEB", fg="#FFFFFF")
name_label.pack(pady=20)

city_name = StringVar()
state_list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
    "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
    "National Capital Territory of Delhi", "Puducherry"
]

com = ttk.Combobox(win, values=state_list_name, font=("Arial", 15), textvariable=city_name)
com.pack(pady=10, padx=20, fill=X)


done_button = Button(win, text="Done", font=("Arial", 15, "bold"), bg="#4682B4", fg="#FFFFFF", command=data_get)
done_button.pack(pady=10)

info_frame = Frame(win, bg="#87CEEB")
info_frame.pack(pady=20, padx=20, fill=X)

w_label = Label(info_frame, text="🌈 Weather Climate ", font=("Arial", 15), bg="#87CEEB", fg="#FFFFFF")
w_label.grid(row=0, column=0, sticky=W, pady=5)
w_label1 = Label(info_frame, text="", font=("Arial", 15), bg="#87CEEB", fg="#FFFFFF")
w_label1.grid(row=0, column=1, sticky=E, pady=5)

wb_label = Label(info_frame, text="🌚Weather Description: ", font=("Arial", 15), bg="#87CEEB", fg="#FFFFFF")
wb_label.grid(row=1, column=0, sticky=W, pady=5)
wb_label1 = Label(info_frame, text="", font=("Arial", 15), bg="#87CEEB", fg="#FFFFFF")
wb_label1.grid(row=1, column=1, sticky=E, pady=5)

temp_label = Label(info_frame, text="🌞 Temperature (°C):", font=("Arial", 15), bg="#87CEEB", fg="#FFFFFF")
temp_label.grid(row=2, column=0, sticky=W, pady=5)
temp_label1 = Label(info_frame, text="", font=("Arial", 15), bg="#87CEEB", fg="#FFFFFF")
temp_label1.grid(row=2, column=1, sticky=E, pady=5)

per_label = Label(info_frame, text="💨Pressure (hPa):", font=("Arial", 15), bg="#87CEEB", fg="#FFFFFF")
per_label.grid(row=3, column=0, sticky=W, pady=5)
per_label1 = Label(info_frame, text="", font=("Arial", 15), bg="#87CEEB", fg="#FFFFFF")
per_label1.grid(row=3, column=1, sticky=E, pady=5)


win.mainloop()
