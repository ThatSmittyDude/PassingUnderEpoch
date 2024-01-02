#PassingUnderEpochLIVEGUIv1.5
#Author: Austin Smith
#Email: ThatSmittyDude@outlook.com
#Unix Timestamp: 1704156525

import customtkinter
from datetime import datetime
import pyperclip

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def ep():
    unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
    unix_time_r = round(unix_timestamp)
    label2.configure(text=unix_time_r)

    # Schedule the next update after 1000 milliseconds (1 second)
    root.after(1000, ep)

def copy_to_clipboard():
    unix_timestamp = label2.cget("text")
    pyperclip.copy(str(unix_timestamp))

root = customtkinter.CTk()
root.geometry("300x200")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=30, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame, text="Unix Timestamp")
label1.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text="")
label2.pack(pady=12, padx=10)

button_copy = customtkinter.CTkButton(master=frame, text="Copy to Clipboard", command=copy_to_clipboard)
button_copy.pack(pady=12, padx=10)

# Initial update when the GUI starts
ep()

root.mainloop()
