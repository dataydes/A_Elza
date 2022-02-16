echo "Instalando pacotes necessários"
pip install urllib3
pip install selenium==3.141.0
pip install html5lib
pip install requests
pip install pywin32
python -m pip install --upgrade pip
python Update_ChormeDriver.py
cd src
start streamlink-2.2.0.exe
cd ..
del chromedriver.zip