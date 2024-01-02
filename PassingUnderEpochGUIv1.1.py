#PassingUnderEpochGUIv1.1
#Author:Austin Smith
#Email: ThatSmittyDude@outlook.com
#Unix Timestamp: 1704123936
import customtkinter
from datetime import datetime

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("300x150")
    
unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
        
unix_time_r = round(unix_timestamp)

frame = customtkinter.CTkFrame(master=root)
def ep():
    content=unix_time_r

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=30, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Unix Timestamp")
label.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text=unix_time_r)
label.pack(pady=12, padx=10)

root.mainloop()

