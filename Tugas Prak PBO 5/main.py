import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from datetime import datetime

class AplikasiCatatan:
    def __init__(self, root):
        self.root = root
        self.root.title("Catatan Harian")
        self.notes = []

        # Menu Bar
        self.menu_bar = tk.Menu(root)
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Keluar", command=self.exit_app)
        self.menu_bar.add_cascade(label="file", menu=file_menu)

        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="Tentang", command=self.tampilkan_tentang)
        self.menu_bar.add_cascade(label="bantuan", menu=help_menu)
        root.config(menu=self.menu_bar)

        # Frame utama
        frame_input = tk.Frame(root)
        frame_input.pack(padx=10, pady=10, fill=tk.X)

        # Judul
        tk.Label(frame_input, text="Judul:").grid(row=0, column=0, sticky="w")
        self.title_entry = tk.Entry(frame_input, width=40)
        self.title_entry.grid(row=0, column=1, sticky="we", padx=5)
        
        # Isi catatan
        self.content_text = ScrolledText(frame_input, wrap="word", height=5, width=40)
        self.content_text.grid(row=1, column=0, columnspan=2, pady=(5, 5), sticky="we")

        # Tombol Tambah dan Hapus
        button_frame = tk.Frame(root)
        button_frame.pack()
        tk.Button(button_frame, text="Tambah catatan", command=self.tambah_catatan).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Hapus catatan", command=self.hapus_catatan).pack(side=tk.LEFT, padx=5)

        # Frame tampilan catatan
        display_frame = tk.Frame(root)
        display_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Label untuk list dan isi
        tk.Label(display_frame, text="Daftar Catatan (listbox)").grid(row=0, column=0, sticky="w")
        tk.Label(display_frame, text="Isi catatan (Text)").grid(row=0, column=1, sticky="w")

        # Listbox catatan
        self.notes_listbox = tk.Listbox(display_frame, width=40, height=10)
        self.notes_listbox.grid(row=1, column=0, sticky="nsew", padx=(0,5))
        self.notes_listbox.bind("<<ListboxSelect>>", self.tampilkan_catatan)

        # Scrollbar
        scrollbar = tk.Scrollbar(display_frame, orient=tk.VERTICAL, command=self.notes_listbox.yview)
        scrollbar.grid(row=1, column=0, sticky="nse", padx=(0,5))
        self.notes_listbox.config(yscrollcommand=scrollbar.set)

        # Text area isi catatan
        self.content_view = ScrolledText(display_frame, wrap="word", height=10, width=40, state=tk.DISABLED)
        self.content_view.grid(row=1, column=1, sticky="nsew")

        display_frame.grid_columnconfigure(0, weight=1)
        display_frame.grid_columnconfigure(1, weight=1)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_listbox(self):
        self.notes_listbox.delete(0, tk.END)
        for note in self.notes:
            timestamp = note.get("waktu_buat", "Unknown")
            self.notes_listbox.insert(tk.END, f"{note['judul']} - ({timestamp})")

    def tambah_catatan(self):
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()
        if not title or not content:
            messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.notes.append({"judul": title, "isi": content, "waktu_buat": timestamp})
        self.update_listbox()
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)

    def tampilkan_catatan(self, event):
        selection = self.notes_listbox.curselection()
        if selection:
            index = selection[0]
            note = self.notes[index]
            self.content_view.config(state=tk.NORMAL)
            self.content_view.delete("1.0", tk.END)
            self.content_view.insert(tk.END, note['isi'])
            self.content_view.config(state=tk.DISABLED)

    def hapus_catatan(self):
        selection = self.notes_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Pilih catatan yang akan dihapus.")
            return
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus catatan ini?"):
            index = selection[0]
            del self.notes[index]
            self.update_listbox()
            self.content_view.config(state=tk.NORMAL)
            self.content_view.delete("1.0", tk.END)
            self.content_view.config(state=tk.DISABLED)

    def tampilkan_tentang(self):
        messagebox.showinfo("Tentang", "Aplikasi Catatan Harian\nVersi 1.0\nDibuat dengan Tkinter")

    def exit_app(self):
        self.root.quit()

    def on_closing(self):
        if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiCatatan(root)
    root.mainloop()
