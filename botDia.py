import pyautogui
import time
import keyboard

# Ativação do código na letra F12
def meu_codigo():
    # Começo do bot

    # Abertura do relatório
    pyautogui.click(x=722, y=111)
    time.sleep(1)

    # Click em atendimento
    pyautogui.click(x=557, y=101)
    time.sleep(1)

    mes = 11  # Diga qual será o mês da pesquisa? OBS.: 01=janeiro 02=fevereiro ... 12=Dezembro
    dataFinal = 31  # Qual será o último dia deste mês?
    if dataFinal==31:

        dataPri = 1
        dataSeg = dataPri + 1

        # 1 Data
        data_escrever_01 = f"0+{str(dataPri)}+{str(mes)}2023"
        pyautogui.click(x=492, y=163)
        pyautogui.write(data_escrever_01)

        # 2 Data
        data_escrever_02 = f"0+{str(dataSeg)}+{str(mes)}2023"
        pyautogui.click(x=628, y=162)
        pyautogui.write(data_escrever_02)

        # Selecionando o status
        pyautogui.click(x=646, y=202)
        pyautogui.click(x=496, y=262)

        # Selecionando a unidade
        pyautogui.doubleClick(x=881, y=244)
        pyautogui.typewrite('up')
        pyautogui.click(x=498, y=320)

        # Selecionando Imprimir
        pyautogui.click(x=912, y=708)
        time.sleep(2)

        # Alterando o zoom
        pyautogui.click(x=194, y=39)

        # Zoom 75%
        pyautogui.click(x=174, y=84)

        # Pressiona a tecla "End"
        pyautogui.press('end')

        # Arrastando a página para baixo
        pyautogui.mouseDown(x=1013, y=212)
        pyautogui.moveTo(x=1090, y=82)
        pyautogui.mouseUp(x=1090, y=82)
        time.sleep(4)

        # Dando alt tab para escrever na tabela
        pyautogui.hotkey('alt', 'tab')

        # Click na tabela para a escrita
        pyautogui.click(x=62, y=235)
        time.sleep(4)

        # Scroll para lado
        pyautogui.click(x=1331, y=709)
        pyautogui.hotkey('alt', 'tab')

        # fechando a tabela
        pyautogui.click(x=592, y=38)


        contador=0
        for _ in range(7):
            
            dataPri = 2+contador
            dataSeg = dataPri + 1

            
            # 1 Data
            data_escrever_01 = f"0+{str(dataPri)}+{str(mes)}2023"
            pyautogui.click(x=492, y=163)
            pyautogui.write(data_escrever_01)

            # 2 Data
            data_escrever_02 = f"0+{str(dataSeg)}+{str(mes)}2023"
            pyautogui.click(x=628, y=162)
            pyautogui.write(data_escrever_02)

            # Selecionando Imprimir
            pyautogui.click(x=909, y=703)
            time.sleep(2)

            # Alterando o zoom
            pyautogui.click(x=194, y=39)

            # Zoom 75%
            pyautogui.click(x=174, y=84)

            # Pressiona a tecla "End"
            pyautogui.press('end')

            # Arrastando a página para baixo
            pyautogui.mouseDown(x=1013, y=212)
            pyautogui.moveTo(x=1090, y=82)
            pyautogui.mouseUp(x=1090, y=82)
            time.sleep(4)

            # Dando alt tab para escrever na tabela
            pyautogui.hotkey('alt', 'tab')

            # Click na tabela para a escrita
            pyautogui.click(x=62, y=235)
            time.sleep(4)

            # Scroll para lado
            pyautogui.click(x=1331, y=709)
            pyautogui.hotkey('alt', 'tab')

            # Fechando a tabela
            pyautogui.click(x=592, y=38)
            
            # Incrementa o contador
            contador += 1
        contador=0
        for _ in range(23):
            mes = 11  # Diga qual será o mês da pesquisa? OBS.: 01=janeiro 02=fevereiro ... 12=Dezembro
            dataFinal = 31  # Qual será o último dia deste mês?
            
            dataPri = 9+contador
            dataSeg = dataPri + 1

            
            # 1 Data
            data_escrever_01 = f"{str(dataPri)}+{str(mes)}2023"
            pyautogui.click(x=492, y=163)
            pyautogui.write(data_escrever_01)

            # 2 Data
            data_escrever_02 = f"{str(dataSeg)}+{str(mes)}2023"
            pyautogui.click(x=628, y=162)
            pyautogui.write(data_escrever_02)

            # Selecionando Imprimir
            pyautogui.click(x=909, y=703)
            time.sleep(2)

            # Alterando o zoom
            pyautogui.click(x=194, y=39)

            # Zoom 75%
            pyautogui.click(x=174, y=84)

            # Pressiona a tecla "End"
            pyautogui.press('end')

            # Arrastando a página para baixo
            pyautogui.mouseDown(x=1013, y=212)
            pyautogui.moveTo(x=1090, y=82)
            pyautogui.mouseUp(x=1090, y=82)
            time.sleep(4)

            # Dando alt tab para escrever na tabela
            pyautogui.hotkey('alt', 'tab')

            # Click na tabela para a escrita
            pyautogui.click(x=62, y=235)
            time.sleep(4)

            # Scroll para lado
            pyautogui.click(x=1331, y=709)
            pyautogui.hotkey('alt', 'tab')

            # Fechando a tabela
            pyautogui.click(x=592, y=38)
            
            # Incrementa o contador
            contador += 1
    else:
        
        dataPri = 1
        dataSeg = dataPri + 1

        # 1 Data
        data_escrever_01 = f"0+{str(dataPri)}+{str(mes)}2023"
        pyautogui.click(x=492, y=163)
        pyautogui.write(data_escrever_01)

        # 2 Data
        data_escrever_02 = f"0+{str(dataSeg)}+{str(mes)}2023"
        pyautogui.click(x=628, y=162)
        pyautogui.write(data_escrever_02)

        # Selecionando o status
        pyautogui.click(x=646, y=202)
        pyautogui.click(x=496, y=262)

        # Selecionando a unidade
        pyautogui.doubleClick(x=881, y=244)
        pyautogui.typewrite('up')
        pyautogui.click(x=498, y=320)

        # Selecionando Imprimir
        pyautogui.click(x=912, y=708)
        time.sleep(2)

        # Alterando o zoom
        pyautogui.click(x=194, y=39)

        # Zoom 75%
        pyautogui.click(x=174, y=84)

        # Pressiona a tecla "End"
        pyautogui.press('end')

        # Arrastando a página para baixo
        pyautogui.mouseDown(x=1013, y=212)
        pyautogui.moveTo(x=1090, y=82)
        pyautogui.mouseUp(x=1090, y=82)
        time.sleep(4)

        # Dando alt tab para escrever na tabela
        pyautogui.hotkey('alt', 'tab')

        # Click na tabela para a escrita
        pyautogui.click(x=62, y=235)
        time.sleep(4)

        # Scroll para lado
        pyautogui.click(x=1331, y=709)
        pyautogui.hotkey('alt', 'tab')

        # fechando a tabela
        pyautogui.click(x=592, y=38)


        contador=0
        for _ in range(7):
            
            dataPri = 2+contador
            dataSeg = dataPri + 1

            
            # 1 Data
            data_escrever_01 = f"0+{str(dataPri)}+{str(mes)}2023"
            pyautogui.click(x=492, y=163)
            pyautogui.write(data_escrever_01)

            # 2 Data
            data_escrever_02 = f"0+{str(dataSeg)}+{str(mes)}2023"
            pyautogui.click(x=628, y=162)
            pyautogui.write(data_escrever_02)

            # Selecionando Imprimir
            pyautogui.click(x=909, y=703)
            time.sleep(2)

            # Alterando o zoom
            pyautogui.click(x=194, y=39)

            # Zoom 75%
            pyautogui.click(x=174, y=84)

            # Pressiona a tecla "End"
            pyautogui.press('end')

            # Arrastando a página para baixo
            pyautogui.mouseDown(x=1013, y=212)
            pyautogui.moveTo(x=1090, y=82)
            pyautogui.mouseUp(x=1090, y=82)
            time.sleep(4)

            # Dando alt tab para escrever na tabela
            pyautogui.hotkey('alt', 'tab')

            # Click na tabela para a escrita
            pyautogui.click(x=62, y=235)
            time.sleep(4)

            # Scroll para lado
            pyautogui.click(x=1331, y=709)
            pyautogui.hotkey('alt', 'tab')

            # Fechando a tabela
            pyautogui.click(x=592, y=38)
            
            # Incrementa o contador
            contador += 1
        contador=0
        for _ in range(22):
        
            dataPri = 2+contador
            dataSeg = dataPri + 1

            
            # 1 Data
            data_escrever_01 = f"{str(dataPri)}+{str(mes)}2023"
            pyautogui.click(x=492, y=163)
            pyautogui.write(data_escrever_01)

            # 2 Data
            data_escrever_02 = f"{str(dataSeg)}+{str(mes)}2023"
            pyautogui.click(x=628, y=162)
            pyautogui.write(data_escrever_02)

            # Selecionando Imprimir
            pyautogui.click(x=909, y=703)
            time.sleep(2)

            # Alterando o zoom
            pyautogui.click(x=194, y=39)

            # Zoom 75%
            pyautogui.click(x=174, y=84)

            # Pressiona a tecla "End"
            pyautogui.press('end')

            # Arrastando a página para baixo
            pyautogui.mouseDown(x=1013, y=212)
            pyautogui.moveTo(x=1090, y=82)
            pyautogui.mouseUp(x=1090, y=82)
            time.sleep(4)

            # Dando alt tab para escrever na tabela
            pyautogui.hotkey('alt', 'tab')

            # Click na tabela para a escrita
            pyautogui.click(x=62, y=235)
            time.sleep(4)

            # Scroll para lado
            pyautogui.click(x=1331, y=709)
            pyautogui.hotkey('alt', 'tab')

            # Fechando a tabela
            pyautogui.click(x=592, y=38)
            
            # Incrementa o contador
            contador += 1
# Configuração da tecla de ativação (por exemplo, F12)
tecla_ativacao = "F1"

# Adiciona um manipulador de evento para a tecla de ativação
keyboard.add_hotkey(tecla_ativacao, meu_codigo)

# Mantém o script em execução
keyboard.wait("esc")
