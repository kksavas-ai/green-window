import tkinter as tk

def create_window():
    root = tk.Tk()
    root.title("Green Window")
    # Set window size (optional)
    root.geometry("400x300")
    # Configure background color to green
    root.configure(bg="green")
    return root

if __name__ == "__main__":
    win = create_window()
    win.mainloop()