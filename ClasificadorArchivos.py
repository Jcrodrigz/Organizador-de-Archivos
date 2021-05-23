# Hecho por Jesús Cillero Rodríguez
# Importados:
import os
import shutil
import sys


def create_folders(directories, directory_path):
    for key in directories:
        if key not in os.listdir(directory_path):
            os.mkdir(os.path.join(directory_path, key))
    if "Otros" not in os.listdir(directory_path):
        os.mkdir(os.path.join(directory_path, "Otros"))


def organize_folders(directories, directory_path):
    for file in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file)):
            src_path = os.path.join(directory_path, file)
            for key in directories:
                extension = directories[key]
                if file.endswith(extension):
                    dest_path = os.path.join(directory_path, key, file)
                    shutil.move(src_path, dest_path)
                    break


def organize_remaining_files(directory_path):
    for file in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file)):
            src_path = os.path.join(directory_path, file)
            dest_path = os.path.join(directory_path, "Otros", file)
            shutil.move(src_path, dest_path)

def organize_remaining_folders(directories, directory_path):
    list_dir = os.listdir(directory_path)
    organized_folders = []
    for folder in directories:
        organized_folders.append(folder)
    organized_folders = tuple(organized_folders)
    for folder in list_dir:
        if folder not in organized_folders:
            src_path = os.path.join(directory_path, folder)
            dest_path = os.path.join(directory_path, "Carpetas", folder)
            try:
                shutil.move(src_path, dest_path)
            except shutil.Error:
                shutil.move(src_path, dest_path + " - copy")
                print("Esa carpeta ya existe en la carpeta de destino."
                      "/nThe folder is renamed to '{}'".format(folder + " - copy"))

if __name__ == '__main__':
    directory_path = "C:xxxx/xxxx/xxxx" # Entre paréntesis se deberá añadir la dirección donde están los archivos a organizar.
    directories = {
        "HTML": (".html5", ".html", ".htm", ".xhtml"),
        "Imágenes": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   "svg",
                   ".heif", ".psd"),
        "Videos": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng",
                   ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "Documentos": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                      ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                      "pptx"),
        "Archivos": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "Audios": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "Texto sin formato": (".txt", ".in", ".out"),
        "Pdf´s": ".pdf",
        "Python": ".py",
        "Programas": ".exe",
        "Otros": "",
        "Carpetas": ""
    }
    try:
        create_folders(directories, directory_path)
        organize_folders(directories, directory_path)
        organize_remaining_files(directory_path)
        organize_remaining_folders(directories, directory_path)
    except shutil.Error:
        print("Se produjo un error al intentar mover un elemento a su carpeta de destino.")
