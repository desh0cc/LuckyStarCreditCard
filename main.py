import re, tkinter as tk
from tkinter import * 
from PIL import Image, ImageTk
from tkinter import PhotoImage, messagebox

root = tk.Tk()
root.title("Totally Not Malware >~<")

image = Image.open('aquacrying.png')
photo = ImageTk.PhotoImage(image)

frameCnt = 32
frames = [PhotoImage(file='tsukasa-lucky-star.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def validate_input(input_text, pattern):
    return re.match(pattern, input_text)

card_number_pattern = r'^\d{16}$'  
expiration_pattern = r'^\d{2}/\d{2}$' 
security_code_pattern = r'^\d{3}$'

def dyakuyu():
    card_number = entry1.get()
    expiration = entry2.get()
    security_code = entry3.get()

    card_number_valid = re.match(card_number_pattern, card_number)
    expiration_valid = re.match(expiration_pattern, expiration)
    security_code_valid = re.match(security_code_pattern, security_code)
    
    if card_number_valid and expiration_valid and security_code_valid:
        messagebox.showinfo("Succesfull", "Thanks ma frendo")
    else:
        show_sad_gif()


def show_sad_gif():
    sad_window = Toplevel()
    sad_window.title("Something goes wrong...")

    textlabl = Label(sad_window, text='Incorrect Data (╥_╥)')
    textlabl.pack(side='top')

    sad_label = Label(sad_window, image=photo)
    sad_label.pack()

    ok_button = Button(sad_window, text="S-sorry!", command=sad_window.destroy)
    ok_button.pack()

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)

label = Label(root)
label.pack(side='left')
root.after(0, update, 0)

custom_font = ("Times New Roman", 16)

text_label = Label(root, text="H-hi there...\nDo you think I could have your\ncredit card information, p-please?")
text_label.pack(anchor='ne')
text_label.configure(font=custom_font)

label1 = Label(root, text="Card number:",font=("Times New Roman", 13))
entry1 = Entry(root, width=30, font=custom_font)
label1.pack(anchor="w")
entry1.pack(fill="x")

label2 = Label(root, text="Expiry Date:",font=("Times New Roman", 13))
entry2 = Entry(root, width=30, font=custom_font)
label2.pack(anchor="w")
entry2.pack(fill="x")

label3 = Label(root, text="Security Code:",font=("Times New Roman", 13))
entry3 = Entry(root, width=30, font=custom_font)
label3.pack(anchor="w")
entry3.pack(fill="x")

spacer_frame = Frame(root)
spacer_frame.pack()

button = Button(root, text='T-Thanks...', command=dyakuyu, font=('Times New Roman', 14))
button.pack(side='bottom')

root.mainloop()