import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def get_file_names(directory):
    file_names = []
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    file_names.append(entry.name)
    except FileNotFoundError:
        log_message(f"Error: The directory at {directory} does not exist.")
    except NotADirectoryError:
        log_message(f"Error: The path {directory} is not a directory.")
    except PermissionError:
        log_message(f"Error: Permission denied for accessing the directory {directory}.")
    except Exception as e:
        log_message(f"An error occurred: {e}")
    return file_names

def delete_files_by_name(file_names, game_directory):
    try:
        with os.scandir(game_directory) as entries:
            for entry in entries:
                if entry.is_file() and entry.name in file_names:
                    file_path = os.path.join(game_directory, entry.name)
                    os.remove(file_path)
                    log_message(f"Deleted file: {entry.name}")
    except FileNotFoundError:
        log_message(f"Error: The directory at {game_directory} does not exist.")
    except PermissionError:
        log_message(f"Error: Permission denied for accessing the directory {game_directory}.")
    except Exception as e:
        log_message(f"An error occurred: {e}")

def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        game_directory_entry.delete(0, tk.END)
        game_directory_entry.insert(0, directory_path)

def start_deletion():
    game_directory = game_directory_entry.get()
    if not game_directory:
        messagebox.showwarning("Input Error", "Please select a game directory.")
        return

    main_file_path_to_delete = "mod-to-delete/Main"
    resources_file_path_to_delete = "mod-to-delete/Resources"

    game_directory_resources = os.path.join(game_directory, "DataPC_Resources_patch_01.forge")
    game_directory_main = os.path.join(game_directory, "DataPC_patch_01.forge")

    resource_file_names = get_file_names(resources_file_path_to_delete)
    main_file_names = get_file_names(main_file_path_to_delete)

    delete_files_by_name(main_file_names, game_directory_main)
    delete_files_by_name(resource_file_names, game_directory_resources)

    log_message("Mod files have been deleted successfully.")
    messagebox.showinfo("Operation Complete", "Mod files have been deleted successfully.")

def log_message(message):
    log_text.config(state=tk.NORMAL)  # Enable editing the Text widget
    log_text.insert(tk.END, message + '\n')  # Append the message
    log_text.config(state=tk.DISABLED)  # Disable editing the Text widget
    log_text.yview(tk.END)  # Scroll to the end of the log

def exit_program():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Mod File Deletion Tool")

# Create frames for layout
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

log_frame = tk.Frame(main_frame, width=300, bg='lightgray')
log_frame.pack(side=tk.LEFT, fill=tk.Y)

control_frame = tk.Frame(main_frame)
control_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Log area
log_text = tk.Text(log_frame, wrap=tk.WORD, height=20, width=40, bg='black', fg='white')
log_text.pack(expand=True, fill=tk.BOTH)
log_text.config(state=tk.DISABLED)  # Initially disable editing

# Game Directory Selection
game_directory_label = tk.Label(control_frame, text="Game Directory:")
game_directory_label.pack(pady=5)

game_directory_entry = tk.Entry(control_frame, width=50)
game_directory_entry.pack(pady=5)

browse_button = tk.Button(control_frame, text="Browse", command=browse_directory)
browse_button.pack(pady=5)

delete_button = tk.Button(control_frame, text="Delete Mod Files", command=start_deletion)
delete_button.pack(pady=20)

exit_button = tk.Button(control_frame, text="Exit", command=exit_program)
exit_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
