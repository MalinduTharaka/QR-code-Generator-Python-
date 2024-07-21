import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import qrcode

class QRCodeGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QR Code Generator")
        self.geometry("500x600")
        self.configure(bg="#2b2b2b")
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Helvetica', 12), padding=10, background='#3a3a3a', foreground='white')
        self.style.configure('TLabel', font=('Helvetica', 12), background="#2b2b2b", foreground='white')
        self.style.configure('TEntry', font=('Helvetica', 12), padding=10)
        self.style.map('TButton', background=[('active', '#1f1f1f')], foreground=[('active', 'white')])

        self.label = ttk.Label(self, text="Enter text or link:")
        self.label.pack(pady=20)
        
        self.entry = ttk.Entry(self, width=50)
        self.entry.pack(pady=10)
        
        self.generate_button = ttk.Button(self, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)
        
        self.save_button = ttk.Button(self, text="Save QR Code", command=self.save_qr_code, state=tk.DISABLED)
        self.save_button.pack(pady=10)
        
        self.qr_image_label = ttk.Label(self)
        self.qr_image_label.pack(pady=20)

        self.qr_image = None

    def generate_qr_code(self):
        text = self.entry.get()
        if text:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            self.qr_image = qr.make_image(fill='black', back_color='white')
            
            self.display_qr_code()
            self.save_button.config(state=tk.NORMAL)

    def display_qr_code(self):
        qr_img = self.qr_image.resize((300, 300), Image.Resampling.LANCZOS)
        self.qr_tk_image = ImageTk.PhotoImage(qr_img)
        self.qr_image_label.config(image=self.qr_tk_image)

    def save_qr_code(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.qr_image.save(file_path)

if __name__ == "__main__":
    app = QRCodeGenerator()
    app.mainloop()
