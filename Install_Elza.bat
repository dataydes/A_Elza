echo "Instalando pacotes necessários"
python -m pip install --upgrade pip
pip install urllib3
pip install selenium==3.141.0
pip install html5lib
pip install requests
pip install pywin32
::pip install streamlink
cd src
start /wait python Update_ChormeDriver.py
move chromedriver.exe ../
del chromedriver.*
start streamlink-2.2.0.exe
cd ..