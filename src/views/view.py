import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class View():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Whisper")
        self.window.minsize(450, 225)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

    def main_menu(self):
        self.clear_window()
        self.path_audio = ""

        container = ttk.Frame(self.window)
        container.grid(row=0, sticky="nsew")
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        self.path = ttk.Label(container, text=self.path_audio.split("/")[-1])
        self.path.grid(column=0, sticky="n")

        audio = ttk.Button(container, text="Choose an audio file", command=self.open_file)
        audio.grid(column=0)

        model_label = ttk.Label(container, text="Choose a model :")
        model_label.grid(column=1, sticky="w")

        model = ttk.Combobox(container, values=["Select a model", "tiny.en", "base.en", "small.en", "medium.en", "tiny", "base", "small", "medium", "large"])
        model.set("Select a model")
        model.grid(column=1, sticky="e")

        button = ttk.Button(self.window, text="Retranscript", command=(lambda: self.controller.retranscript(self.path_audio, model.get())))
        button.grid(row=1, sticky="nsew")

    def loading(self):
        self.clear_window()

        button = ttk.Button(self.window, text="Return", command=self.controller.loading_return)
        button.grid(row=0, sticky="nw")


        text_label = ttk.Label(self.window, text="Loading...")
        text_label.grid(row=0, sticky="sew")

        self.progress_bar = ttk.Progressbar(self.window, orient="horizontal", length=200, mode="indeterminate")
        self.progress_bar.grid(row=1, sticky="nsew")
        self.progress_bar.start()

    def result(self, result):
        self.clear_window()

        container_text = ttk.Frame(self.window)
        container_text.grid(row=0, sticky="nsew")
        container_text.columnconfigure(0, weight=1)
        container_text.rowconfigure(0, weight=1)
        
        text_area = tk.Text(container_text)
        scrollbar = ttk.Scrollbar(container_text, command=text_area.yview)
        
        text_area.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        text_area.insert(tk.END, result)
        text_area.configure(yscrollcommand=scrollbar.set, state=tk.DISABLED)

        container_button = ttk.Frame(self.window)
        container_button.grid(row=1, sticky="nsew")
        container_button.columnconfigure(0, weight=1)
        container_button.rowconfigure(0, weight=1)

        button_save = ttk.Button(container_button, text="Save", command=self.controller.save_result)
        button_save.grid(row=0, column=0, sticky="nsew")

        button_main = ttk.Button(container_button, text="Main", command=self.controller.result_return)
        button_main.grid(row=0, column=1, sticky="nsew")

    def error(self, e_msg):
        messagebox.showerror("ERROR", e_msg)

    def saved(self):
        messagebox.showinfo("Save", "File saved")

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def open_file(self):
        self.path_audio = filedialog.askopenfilename(title="Select file", filetypes=(("Audio Files", "*.mp3 *.wav *.flac"), ("All Files", "*.*")), initialdir="")
        self.path["text"] = self.path_audio.split("/")[-1]
    
    def save_file(self):
        return filedialog.asksaveasfilename(defaultextension=".txt", title="Save file", filetypes=(("Text Files", "*.txt *.md"), ("All Files", "*.*")), initialdir="./ressources")

    def set_controller(self, controller):
        self.controller = controller

    def stop_loading(self):
        self.progress_bar.stop()

    def run(self):
        self.window.mainloop()