echo "Instalando pacotes necessários"
pip3 install urllib3
pip3 install selenium
pip3 install html5lib
pip3 install requests
python -m pip install upgrade pip

curl https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_win32.zip > chromedriver_win32.zip
tar -xf chromedriver_win32.zip
del chromedriver_win32.zip
start streamlink-2.1.2.exe
