import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("800x500")

def inputCalc():
    print("test")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20,padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="input what you want to calculate: ")
label.pack(pady=12, padx=10)

entry = ctk.CTkEntry(master=frame, placeholder_text="input what you want to calculate: ")
entry.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="=", command=inputCalc)
button.pack(pady=12, padx=10)

root.mainloop()