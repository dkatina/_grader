import os
import shutil
import subprocess


current_file_path = os.path.abspath(__file__)
current_folder_path = os.path.dirname(current_file_path)

students ={
"Dylan":"https://github.com/badreddin98/advanced-e-commerce-api",
}

flask = True

for name, url in students.items():
    os.system(f"git clone {url} {name}")
    if flask:
        shutil.copyfile("./_grader/.env", f"./{name}/.env")
        print(name)#
        os.chdir(f"{name}")
        if os.path.isdir("./venv"):
            shutil.rmtree('venv')
        elif os.path.isdir("./myvenv"):
            shutil.rmtree('myvenv')
        if os.name == "nt":
            subprocess.call(f"start {current_folder_path}\\flask-load.bat", shell=True)            
        if os.name != "nt":
            subprocess.call(f". {current_folder_path}/flask-load.sh", shell=True)
        os.chdir(f"..")
    if os.path.isfile(f"./{name}/package.json"):
        os.chdir(f"{name}")
        os.system("npm install")
        os.chdir(f"..")
