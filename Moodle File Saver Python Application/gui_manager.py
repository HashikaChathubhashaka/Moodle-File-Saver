import tkinter as tk
from tkinter import filedialog
from config_manager import load_config, save_config
import pystray
from pystray import MenuItem, Icon
from PIL import Image, ImageDraw
import webbrowser

# Global variables
main_destination_folder = ""
label_folder = None
root = None
icon = None


# Function to select and update the folder
def select_destination_folder():
    global main_destination_folder, label_folder
    folder_selected = filedialog.askdirectory(title="Select New Save Directory")
    if folder_selected:
        main_destination_folder = folder_selected
        save_config(main_destination_folder)
        label_folder.config(text=f"Current Folder: {main_destination_folder}")


# # Load the stored folder or set an empty one
config = load_config()

main_destination_folder = config["destination_folder"]


# GUI for changing the folder
def open_gui():
    global label_folder
    global root
    root = tk.Tk()
    root.title("Moodle File Saver")
    root.geometry("400x180")
    # Hide the window close button
    root.protocol("WM_DELETE_WINDOW", on_closing)

    icon_path = "icon.png"
    icon_image = tk.PhotoImage(file=icon_path)
    root.iconphoto(True, icon_image)

    root.resizable(False, False)
    label_folder = tk.Label(root, text=f"Current Save Directory: {main_destination_folder}", wraplength=380)
    label_folder.pack(pady=10)

    btn_change = tk.Button(root, text="Change Folder", command=select_destination_folder)
    btn_change.pack(pady=10)



    # Button to close the application
    close_button = tk.Button(root, text="Close", command=on_closing)
    close_button.pack(pady=10)


    # GitHub Link Label
    github_label = tk.Label(root, text="More Details & Updates - GitHub", fg="blue", cursor="hand2")
    github_label.pack(pady=15)
    github_label.bind("<Button-1>", open_github)  # Make it clickable

    root.mainloop()


def get_main_destination_folder():
    return main_destination_folder


def on_closing():
    # Hide the window instead of destroying it
    root.withdraw()  # Hide the window
    create_tray_icon()  # Create the tray icon


def create_tray_icon():
    global icon

    icon_image = Image.open("tray_icon.ico")
    icon = Icon("File Saver icon", icon_image, " Moodle File Saver", menu=pystray.Menu(
        MenuItem("Restore", restore_gui),
        MenuItem("Exit", exit_application)
    ))
    icon.run()


def create_image():
    # Create an image for the tray icon (using Pillow)
    image = Image.new("RGB", (64, 64), "white")
    dc = ImageDraw.Draw(image)
    dc.ellipse((0, 0, 64, 64), fill="blue")
    return image


def restore_gui():
    root.deiconify()  # Restore the GUI window
    icon.stop()  # Stop the tray icon


def exit_application():
    root.quit()  # Quit the application
    icon.stop()  # Stop the tray icon


def open_github(event):
    webbrowser.open_new("https://github.com/HashikaChathubhashaka/Moodle-File-Saver")