# A Elza
Aplicativo criado em python como ferramenta de estudo da linguagem.
Este aplicativo gera um vídeo do stream ao vivo produzido pelo youtube.

Modo de instalação:
1 - Execute o Install_Elza.bat para atualizar o python as bibliotecas e baixar o driver Chrome e streamlink;
2 - Dê dois clicks no Elza.py
3 - insira o link do stream ao vivo e aperte em Gravar (A janela ficará travada e uma segunda janela se abrirá)
4 - Caso queira cancelar a gravação feche as duas janelas;


Para gerar o exe
pip install cxfreeze
cxfreeze Elza.py --target-dir Elza
