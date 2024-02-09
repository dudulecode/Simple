import threading
from CTkMessagebox import CTkMessagebox
import customtkinter
import time

message = """
hey
"""


def show_error():
    # Default messagebox for showing some information
    CTkMessagebox(title="Error", height=50, sound=True, message="Error !", icon="cancel")

app = customtkinter.CTk()
app.title("test")
app.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
app.columnconfigure(0, weight=1)
app.minsize(1000, 650)

app.withdraw()
show_error()

app.mainloop()


