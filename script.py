# my game directory
# /mnt/c/Program Files /Ub/U/games/Ghost Recon Breakpoint/Extracted
# /mnt/c/Program\ Files\ \(x86\)/Ubisoft/Ubisoft\ Game\ Launcher/games/Ghost\ Recon\ Breakpoint/Extracted


import sys
import os

def get_file_names(directory):
    print(f"Getting file names for directory: {directory}")
    file_names = []
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    file_names.append(entry.name)
    except FileNotFoundError:
        print(f"Error: The directory at {directory} does not exist.")
    except NotADirectoryError:
        print(f"Error: The path {directory} is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied for accessing the directory {directory}.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    return file_names

def delete_files_by_name(file_names, game_directory):
    print(f"Deleting files by name in directory: {game_directory}")
    try:
        with os.scandir(game_directory) as entries:
            print("Scanning directory")
            for entry in entries:
                if entry.is_file() and entry.name in file_names:
                    file_path = os.path.join(game_directory, entry.name)
                    os.remove(file_path)
                    print(f"Deleted file: {entry.name}")
    except FileNotFoundError:
        print(f"Error: The directory at {game_directory} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for accessing the directory {game_directory}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        print(f"Deleting mod from game directory: {sys.argv[1]}")
        
        main_file_path_to_delete = "mod-to-delete/Main"
        resources_file_path_to_delete = "mod-to-delete/Resources"
        
        game_directory_resources = os.path.join(sys.argv[1], "DataPC_Resources_patch_01.forge")
        game_directory_main = os.path.join(sys.argv[1], "DataPC_patch_01.forge")
        
        # Lists containing file names of desired deletion
        resource_file_names = get_file_names(resources_file_path_to_delete)
        main_file_names = get_file_names(main_file_path_to_delete)
        
        delete_files_by_name(main_file_names, game_directory_main)
        delete_files_by_name(resource_file_names, game_directory_resources)

        
