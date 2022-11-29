# CreateUser: momentan brauchen wir nur ein Eingabefeld + Button
# LoginUser: ein Eingabefeld + Button

import customtkinter



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")




def create():
    print("create_user: ", entry1.get())

def login():
    print("login_user: ", entry2.get())

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="NoteApp", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="create_user")
entry1.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="create_user", command=create())
button1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="login_user", show="*")
entry2.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="loging_user", command=login())
button2.pack(pady=12, padx=10)



root.mainloop()

