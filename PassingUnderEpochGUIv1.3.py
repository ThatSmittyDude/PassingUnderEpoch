# PassingUnderEpochGUIv1.3
# Author: Austin Smith
# Email: ThatSmittyDude@outlook.com
# Unix Timestamp: 1704133441

import customtkinter
from datetime import datetime

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def ep():
    unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
    unix_time_r = round(unix_timestamp)
    label2.configure(text=unix_time_r)

root = customtkinter.CTk()
root.geometry("300x150")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=30, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame, text="Unix Timestamp")
label1.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text="")
label2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Update Timestamp", command=ep)
button.pack(pady=12, padx=10)

# Initial update when the GUI starts
ep()

root.mainloop()
