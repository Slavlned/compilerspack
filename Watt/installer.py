from pyfiglet import Figlet
import subprocess
import sys
import shutil
import os
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from termcolor import colored

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

f = Figlet(font='larry3d')

def logo():
    print(colored(f.renderText('WATT'), color="yellow"))

def check_dependencies():
    def is_command_available(command):
        return shutil.which(command) is not None

    if not is_command_available("java"):
        print('Java is not installed!')
        sys.exit(-1)

    if not is_command_available("mvn"):
        print('Maven is not installed!')
        sys.exit(-1)

def install_watt():
    clear_screen()
    logo()
    print("Installing WATT... [0%]")

    print("Cloning repository...")
    subprocess.run("git clone https://github.com/kilwatt/wat", shell=True)
    
    os.chdir('wat')
    clear_screen()
    logo()
    print("Installing WATT... [30%]")
    print("Building with Maven...")
    subprocess.run("mvn clean package", shell=True)
    
    os.chdir('target')
    jar_files = [f for f in os.listdir(os.getcwd()) if f.endswith(".jar")]
    jar_path = os.path.join(os.getcwd(), jar_files[1])
    
    clear_screen()
    logo()
    print("Installing WATT... [70%]")
    print("Generating start script...")
    
    script_name = "watt.bat" if os.name == "nt" else "watt.sh"
    script_path = os.path.join(os.getcwd(), script_name)
    
    with open(script_path, "w", encoding="utf-8") as f:
        if os.name == "nt":
            f.write(f'@echo off\njava -jar "{jar_path}" %*\n')
        else:
            f.write(f'#!/bin/bash\njava -jar "{jar_path}" "$@"\n')
            os.chmod(script_path, 0o755)
    
    print(f"Created {script_name}: {script_path}")
    
    print("Installing WATT.... [90%]")
    if sys.platform.startswith("win"):
        subprocess.run("..\\..\\win_helper.bat")
    elif 'linux' in sys.platform:
        subprocess.run("..\\..\\linux_helper.bat")
    else:
        subprocess.run("..\\..\\mac_helper.bat")

    console = Console()
    with Progress(SpinnerColumn(), TextColumn("[progress.percentage] Finishing... {task.percentage:.0f}%")) as progress:
        task = progress.add_task("Finishing...", total=100)
        for _ in range(100):
            time.sleep(0.025)
            progress.update(task, advance=1)
    
    clear_screen()
    logo()
    print("Installation completed!")

def main():
    clear_screen()
    logo()
    while True:
        choice = input("Would you like to install WATT programming language? [y/n]: ").strip().lower()
        if choice in ['y', 'n']:
            break
    
    if choice == 'n':
        print("Exited.")
        return
    
    clear_screen()
    logo()
    print("Processing install...")
    check_dependencies()
    install_watt()

if __name__ == "__main__":
    main()
