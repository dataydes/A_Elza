from win32com.client import Dispatch
import subprocess 
from zipfile import ZipFile

def get_version_via_com(filename):  #Pega a versão do Chorme instalada
    parser = Dispatch("Scripting.FileSystemObject")
    try:
        version = parser.GetFileVersion(filename)
    except Exception:
        return None
    return version

if __name__ == "__main__":
    paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
             r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
    version = list(filter(None, [get_version_via_com(p) for p in paths]))[0]
    print(version)  #imprime a versão do Chrome instalada.
    cmd = "Invoke-WebRequest https://chromedriver.storage.googleapis.com/"+ version +"/chromedriver_win32.zip -OutFile chromedriver.zip"
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    zip = ZipFile('chromedriver.zip')   #Extrai o pacote.
    zip.extractall()
    