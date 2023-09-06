from tkinter import *
from tkinter import messagebox
import qrcode
import base64

def decrypt():
    password=code.get()

    if password=="1234":
        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        show(decrypt)
    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password !="1234":
        messagebox.showerror("encryption","Invalid Password")


def encrypt():
    password=code.get()

    if password=="1234":
        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        show(encrypt)
    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password !="1234":
        messagebox.showerror("encryption","Invalid Password")

def cryptography():
    
    global screen3
    global code
    global text1
    
    screen3=Toplevel(screen)
    screen3.title("Cryptography")
    screen3.geometry("800x600")
    screen3.configure(bg="#cae8cb")
    
    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(screen3,text="Enter text for encryption and decryption",fg="black",font=("calibri",19)).place(x=30,y=210)
    text1=Text(screen3,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=30,y=5,width=750,height=200)
    
    Label(screen3,text="Enter secret key for encryption and decryption",fg="black",font=("calibri",19)).place(x=30,y=315)
    
    code=StringVar()
    Entry(screen3,textvariable=code,width=19,bd=0,font=("arial",25),bg="white",show="*").place(x=30,y=270)
    
    Button(screen3,text="ENCRYPT",height="3",width="49",bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=30,y=450)
    Button(screen3,text="DECRYPT",height="3",width="49",bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=400,y=450)
    Button(screen3,text="RESET",height="3",width="102",bg="#1089ff",fg="white",bd=0,command=reset).place(x=30,y=520)  

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-','\n':''}

def m_encrypt():
    message=text4.get(1.0,END)[:-1]
    cipher =''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    show(cipher)


def m_decrypt():
    message=text4.get(1.0,END)[:-1]
    message += ' '
    decipher = ''
    citext= ''
    for letter in message:
        if(letter != ' '):
            i=0
            citext +=letter
        else:
            i+=1
            if i==2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''    
    show(decipher)

def morse_code():
    
    global screen4
    global code
    global text4
    
    screen4=Toplevel(screen)
    screen4.title("Morse Code")
    screen4.geometry("800x600")
    screen4.configure(bg="#cae8cb")
    
    def reset():
        code.set("")
        text4.delete(1.0,END)

    Label(screen4,text="Enter to Convert: ",fg="black",font=("calibri",19)).place(x=30,y=5)
    text4=Text(screen4,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text4.place(x=30,y=50,width=750,height=200)
    
    Button(screen4,text="English to morse",height="3",width="49",bg="#ed3833",fg="white",bd=0,command=m_encrypt).place(x=30,y=450)
    Button(screen4,text="Morse to English",height="3",width="49",bg="#00bd56",fg="white",bd=0,command=m_decrypt).place(x=400,y=450)
    Button(screen4,text="RESET",height="3",width="102",bg="#1089ff",fg="white",bd=0,command=reset).place(x=30,y=520)  

def qr_code():
    
    global screen4
    global code
    global text4
    
    screen4=Toplevel(screen)
    screen4.title("Morse Code")
    screen4.geometry("800x600")
    screen4.configure(bg="#cae8cb")
    
    def reset():
        code.set("")
        text4.delete(1.0,END)

    Label(screen4,text="Enter to Convert: ",fg="black",font=("calibri",19)).place(x=30,y=5)
    text4=Text(screen4,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text4.place(x=30,y=50,width=750,height=200)
    
    Button(screen4,text="QR code",height="3",width="102",bg="#00bd56",fg="white",bd=0,command=generate_qr_code).place(x=30,y=450)
    Button(screen4,text="RESET",height="3",width="102",bg="#1089ff",fg="white",bd=0,command=reset).place(x=30,y=520)  
  
def generate_qr_code(number):
    data = str(number)  # Convert the number to a string
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("qr_code.png")  # Save the QR code image to a file  

def ba_co():
    message = text4.get(1.0, 'end-1c') 
    binary_text = ''.join(format(ord(c), '08b') for c in message)  
    show(binary_text)  

      
def base_conv(): 
    global screen4
    global code
    global text4
    
    screen4=Toplevel(screen)
    screen4.title("Number Base Converter")
    screen4.geometry("800x600")
    screen4.configure(bg="#cae8cb")
    
    def reset():
        code.set("")
        text4.delete(1.0,END)

    Label(screen4,text="Enter to Convert: ",fg="black",font=("calibri",19)).place(x=30,y=5)
    text4=Text(screen4,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text4.place(x=30,y=50,width=750,height=200)
    
    Button(screen4,text="Convert",height="3",width="102",bg="#00bd56",fg="white",bd=0,command=ba_co).place(x=30,y=450)
    Button(screen4,text="RESET",height="3",width="102",bg="#1089ff",fg="white",bd=0,command=reset).place(x=30,y=520)  

def show(text):

    screen1=Toplevel(screen)
    screen1.title("encryption")
    screen1.geometry("400x200")
    screen1.configure(bg="#00bd56")

    Label(screen1,text="Converstion",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
    text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,height=150)

    text2.insert(END,text)

def main_screen():

    global screen
    global code
    global text
    
    screen=Tk()
    screen.geometry("600x450")
    
    screen.title("Home")
    screen.configure(background = "#E1F8DC")
    # code=StringVar()
    
    Button(text="Cryptography",font=("arial",15),height="3",width="50",bg="#F9FE4A",fg="black",bd=0,command=cryptography).place(x=20,y=50)
    Button(text="Morse Code",font=("arial",15),height="3",width="50",bg="#00bd56",fg="white",bd=0,command=morse_code).place(x=20,y=150)
    Button(text="Qr code",font=("arial",15),height="3",width="50",bg="red",fg="white",bd=0,command=qr_code).place(x=20,y=250)
    Button(text="Number Base Conv.",font=("arial",15),height="3",width="50",bg="black",fg="white",bd=0,command=base_conv).place(x=20,y=350)
    

    screen.mainloop()
    
main_screen()