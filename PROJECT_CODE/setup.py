import sys, os
from cx_Freeze import setup, Executable

os.environ["TCL_LIBRARY"] = r"C:\\Users\\Jency\\AppData\\Local\\Programs\\Python\\Python312\\DDLs\\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\\Users\\Jency\\AppData\\Local\\Programs\\Python\\Python312\\DDLs\\tk8.6"

base = None
include_files = [
    r"C:\Users\Jency\Downloads\assets",
    r"C:\\Users\\Jency\\AppData\\Local\\Programs\\Python\\Python312\\DLLs\\tcl86t.dll",
    r"C:\\Users\\Jency\\AppData\\Local\\Programs\\Python\\Python312\\DLLs\\tk86t.dll"
]

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="KrypApp",
    version="1.4",
    description="File Encryption App",
    options={
        "build_exe": {
            "include_files": include_files
            }
    },
    executables=[
        Executable(
            "KrypApp.py",
            base=base,
            #targetName="KrypApp.exe",
            icon="./assets/icon.ico"
        )
    ]
)
