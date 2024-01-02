# PassingUnderEpochGUIv1.2
# Author: Austin Smith
# Email: ThatSmittyDude@outlook.com
# Unix Timestamp: 1704123936

import customtkinter
from datetime import datetime

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("300x150")

unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
unix_time_r = round(unix_timestamp)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=30, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame, text="Unix Timestamp")
label1.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text=unix_time_r)
label2.pack(pady=12, padx=10)

root.mainloop()
