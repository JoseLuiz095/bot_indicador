import pyautogui
import time
import keyboard
import sys

mes = str(sys.argv[1])
ultimo_dia_do_mes = str(sys.argv[2])
ano = str(sys.argv[3])

# verifica e instalar dependências
try:
    import pyautogui
    import keyboard
except ImportError as e:
    print(f"Falha ao importar a biblioteca: {e.name}")
    print("Baixando arquivos necessários para o BOT...")

    # Instalar dependências usando o pip
    try:
        import pip
        pip.main(["install", "pyautogui", "keyboard"])
    except ImportError:
        print("Certifique-se de ter o pip instalado no seu sistema.")







def botTotal():
      # Começo do bot

        # Abertura do relatório
        pyautogui.click(x=722, y=111)
        time.sleep(0.7)
        time.sleep(1)

        # Click em atendimento
        pyautogui.click(x=557, y=101)
        time.sleep(0.7)
        time.sleep(1)

        datainicial=1
        
    
        # 1 Data
        data_escrever_01 = f"0+{str(datainicial)}+{str(mes)}+{str(ano)}"
        pyautogui.click(x=492, y=163)
        time.sleep(0.7)
        pyautogui.write(data_escrever_01, interval=0.1)

        # 2 Data
        data_escrever_02 = f"{str(ultimo_dia_do_mes)}+{str(mes)}+{str(ano)}"
        pyautogui.click(x=628, y=162)
        time.sleep(0.7)
        pyautogui.write(data_escrever_02, interval=0.1)

        # Selecionando o status
        pyautogui.click(x=645, y=203)
        time.sleep(0.7)
        time.sleep(0.7)
        pyautogui.click(x=496, y=260)
        time.sleep(0.7)
        time.sleep(0.7)

        # Selecionando a unidade
        pyautogui.doubleClick(x=983, y=249)
        pyautogui.typewrite('up')
        pyautogui.click(x=498, y=320)
        time.sleep(0.7)

        # Selecionando Imprimir
        pyautogui.click(x=912, y=708)
        time.sleep(0.7)
        time.sleep(8)

        # Alterando o zoom
        pyautogui.click(x=194, y=39)

        time.sleep(0.7)
        # Zoom 75%
        pyautogui.click(x=174, y=84)
        time.sleep(0.7)
        # Pressiona a tecla "End"
        pyautogui.press('end')

        # Arrastando a página para baixo
        pyautogui.mouseDown(x=1013, y=212)
        pyautogui.moveTo(x=1090, y=82)
        pyautogui.mouseUp(x=1090, y=82)
        time.sleep(4)
        
        # Dando alt tab para escrever na tabela
        pyautogui.hotkey('alt', 'tab')
    
             

# Função para executar o bot
def botDia():
      # Começo do bot

        # Abertura do relatório
        pyautogui.click(x=722, y=111)
        time.sleep(0.7)
        time.sleep(1)

        # Click em atendimento
        pyautogui.click(x=557, y=101)
        time.sleep(0.7)
        time.sleep(1)

        dataPri = 1
        dataSeg = dataPri + 1

        # 1 Data
        data_escrever_01 = f"0+{str(dataPri)}+{str(mes)}+{str(ano)}"
        pyautogui.click(x=492, y=163)
        time.sleep(0.7)
        pyautogui.write(data_escrever_01, interval=0.1)

        # 2 Data
        data_escrever_02 = f"0+{str(dataSeg)}+{str(mes)}+{str(ano)}"
        pyautogui.click(x=628, y=162)
        time.sleep(0.7)
        pyautogui.write(data_escrever_02, interval=0.1)

        # Selecionando o status
        pyautogui.click(x=646, y=202)
        time.sleep(0.7)
        pyautogui.click(x=496, y=262)
        time.sleep(0.7)

        # Selecionando a unidade
        pyautogui.doubleClick(x=881, y=244)
        pyautogui.typewrite('up')
        pyautogui.click(x=498, y=320)
        time.sleep(0.7)

        # Selecionando Imprimir
        pyautogui.click(x=912, y=708)
        time.sleep(0.7)
        time.sleep(2)

        # Alterando o zoom
        pyautogui.click(x=194, y=39)
        time.sleep(0.7)
        # Zoom 75%
        pyautogui.click(x=174, y=84)
        time.sleep(0.7)
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
        time.sleep(0.7)
        pyautogui.hotkey('alt', 'tab')

        # fechando a tabela
        pyautogui.click(x=592, y=38)
        time.sleep(0.7)
  
        if ultimo_dia_do_mes==31:
            contador=1
            for _ in range(31):
                
                dataPri = contador+1
                dataSeg = dataPri + 1
                if dataPri<9:
                     
                    # 1 Data
                    data_escrever_01 = f"0+{str(dataPri)}"
                    time.sleep(0.7)
                    pyautogui.click(x=492, y=163)
                    pyautogui.write(data_escrever_01, interval=0.1)

                    # 2 Data
                    data_escrever_02 = f"0+{str(dataSeg)}"
                    time.sleep(0.7)
                    pyautogui.click(x=628, y=162)
                    pyautogui.write(data_escrever_02, interval=0.1)
                elif dataPri==9:
                    # 1 Data
                    data_escrever_01 = f"0+{str(dataPri)}"
                    time.sleep(0.7)
                    pyautogui.click(x=492, y=163)
                    pyautogui.write(data_escrever_01, interval=0.1)
                     # 2 Data
                    data_escrever_02 = f"{str(dataSeg)}"
                    time.sleep(0.7)
                    pyautogui.click(x=628, y=162)
                    pyautogui.write(data_escrever_02, interval=0.1)
                     
                elif 9 < dataPri < 31:
                    # 1 Data
                    data_escrever_01 = f"{str(dataPri)}"
                    time.sleep(0.7)
                    pyautogui.click(x=492, y=163)
                    pyautogui.write(data_escrever_01, interval=0.1)

                    # 2 Data
                    data_escrever_02 = f"{str(dataSeg)}"
                    time.sleep(0.7)
                    pyautogui.click(x=628, y=162)
                    pyautogui.write(data_escrever_02, interval=0.1)
                else:
                    # 1 Data
                    data_escrever_01 = f"{str(dataPri)}"
                    time.sleep(0.7)
                    pyautogui.click(x=492, y=163)
                    pyautogui.write(data_escrever_01, interval=0.1)

                    # 2 Data
                    data_escrever_02 = f"01{(int(mes)+1)}+{str(ano)}"
                    time.sleep(0.7)
                    pyautogui.click(x=628, y=162)
                    pyautogui.write(data_escrever_02, interval=0.1)
                # Selecionando Imprimir
                pyautogui.click(x=909, y=703)
                time.sleep(0.7)
                time.sleep(2)

                # Alterando o zoom
                pyautogui.click(x=194, y=39)
                time.sleep(0.7)
                # Zoom 75%
                pyautogui.click(x=174, y=84)
                time.sleep(0.7)
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
                time.sleep(0.7)
                pyautogui.hotkey('alt', 'tab')

                # Fechando a tabela
                pyautogui.click(x=592, y=38)
                time.sleep(0.7)                
                # Incrementa o contador
                contador += 1
        else:
            contador=1
            for _ in range(30):
                
                dataPri = contador+1
                dataSeg = dataPri + 1
                if dataPri<9:
                     
                    # 1 Data
                    data_escrever_01 = f"0+{str(dataPri)}"
                    time.sleep(0.7)
                    pyautogui.click(x=492, y=163)
                    pyautogui.write(data_escrever_01, interval=0.1)

                    # 2 Data
                    data_escrever_02 = f"0+{str(dataSeg)}"
                    time.sleep(0.7)
                    pyautogui.click(x=628, y=162)
                    pyautogui.write(data_escrever_02, interval=0.1)
                elif dataPri==9:
                    # 1 Data
                    data_escrever_01 = f"0+{str(dataPri)}"
                    time.sleep(0.7)
                    pyautogui.click(x=492, y=163)
                    pyautogui.write(data_escrever_01, interval=0.1)
                     # 2 Data
                    data_escrever_02 = f"{str(dataSeg)}"
                    time.sleep(0.7)
                    pyautogui.click(x=628, y=162)
                    pyautogui.write(data_escrever_02, interval=0.1)
                     
                elif 9 < dataPri < 30:
                    # 1 Data
                    data_escrever_01 = f"{str(dataPri)}"
                    time.sleep(0.7)
                    pyautogui.click(x=492, y=163)
                    pyautogui.write(data_escrever_01, interval=0.1)

                    # 2 Data
                    data_escrever_02 = f"{str(dataSeg)}"
                    time.sleep(0.7)
                    pyautogui.click(x=628, y=162)
                    pyautogui.write(data_escrever_02, interval=0.1)
                else:
                    # 1 Data
                    data_escrever_01 = f"{str(dataPri)}"
                    time.sleep(0.7)
                    pyautogui.click(x=492, y=163)
                    pyautogui.write(data_escrever_01, interval=0.1)

                    # 2 Data
                    data_escrever_02 = f"01{(int(mes)+1)}+{str(ano)}"
                    time.sleep(0.7)
                    pyautogui.click(x=628, y=162)
                    pyautogui.write(data_escrever_02, interval=0.1)
                # Selecionando Imprimir
                pyautogui.click(x=909, y=703)
                time.sleep(0.7)
                time.sleep(2)

                # Alterando o zoom
                pyautogui.click(x=194, y=39)
                time.sleep(0.7)
                # Zoom 75%
                pyautogui.click(x=174, y=84)
                time.sleep(0.7)
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
                time.sleep(0.7)
                pyautogui.hotkey('alt', 'tab')

                # Fechando a tabela
                pyautogui.click(x=592, y=38)
                time.sleep(0.7)                
                # Incrementa o contador
                contador += 1
            

def botCor():
      # Começo do bot

        # Abertura do relatório
        pyautogui.click(x=722, y=111)
        time.sleep(0.7)
        time.sleep(1)

        # Click em relatório de triagens-PA
        pyautogui.click(x=352, y=155)
        time.sleep(0.7)
        time.sleep(1)

        datainicial=1
        
    
        # 1 Data
        data_escrever_01 = f"0+{str(datainicial)}+{str(mes)}+{str(ano)}"
        pyautogui.click(x=481, y=161)
        time.sleep(0.7)
        pyautogui.write(data_escrever_01, interval=0.1)

        # 2 Data
        data_escrever_02 = f"{str(ultimo_dia_do_mes)}+{str(mes)}+{str(ano)}"
        pyautogui.click(x=577, y=163)
        time.sleep(0.7)
        pyautogui.write(data_escrever_02, interval=0.1)

        # Selecionando o status
        pyautogui.click(x=1040, y=159)
        time.sleep(0.7)
        time.sleep(0.7)
        pyautogui.click(x=680, y=217)
        time.sleep(0.7)
        time.sleep(1)

        # Selecionando o tipo de relatorio
        pyautogui.doubleClick(x=544, y=202)
        time.sleep(0.7)
        pyautogui.click(x=513, y=235)
        time.sleep(0.7)
        time.sleep(0.7)

        # Selecionando o Modelo de Relatorio
        pyautogui.click(x=698, y=201)
        time.sleep(0.7)
        time.sleep(0.7)
        pyautogui.click(x=690, y=234)
        time.sleep(0.7)
        time.sleep(0.7)

        # Selecionando a unidade
        pyautogui.doubleClick(x=944, y=244)
        pyautogui.typewrite('up')
        pyautogui.click(x=487, y=334)
        time.sleep(0.7)

        # Selecionando Imprimir
        pyautogui.click(x=886, y=656)
        time.sleep(0.7)
        time.sleep(4)

        # Dando alt tab(para cada cor) para escrever na tabela 
        # Vermelho
        time.sleep(4)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.7)
        # click na tabela
        pyautogui.click(x=52, y=235)
        time.sleep(4)
        # Scroll para lado
        pyautogui.click(x=1328, y=706)
        time.sleep(0.7)
        pyautogui.hotkey('alt', 'tab')

        # Laranja
        time.sleep(4)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.7)
        # click na tabela
        pyautogui.click(x=52, y=235)
        time.sleep(4)
        # Scroll para lado
        pyautogui.click(x=1328, y=706)
        time.sleep(0.7)
        pyautogui.hotkey('alt', 'tab')

        # Amarelo
        time.sleep(4)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.7)
        # click na tabela
        pyautogui.click(x=52, y=235)
        time.sleep(4)
        # Scroll para lado
        pyautogui.click(x=1328, y=706)
        time.sleep(0.7)
        pyautogui.hotkey('alt', 'tab')

        # Verde
        time.sleep(4)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.7)
        # click na tabela
        pyautogui.click(x=52, y=235)
        time.sleep(4)
        # Scroll para lado
        pyautogui.click(x=1328, y=706)
        time.sleep(0.7)
        pyautogui.hotkey('alt', 'tab')
        
        # Azul
        time.sleep(4)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.7)
        # click na tabela
        pyautogui.click(x=52, y=235)
        time.sleep(4)
        # Scroll para lado
        pyautogui.click(x=1328, y=706)
        time.sleep(0.7)
        pyautogui.hotkey('alt', 'tab')

        # Branco
        time.sleep(4)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.7)
        # click na tabela
        pyautogui.click(x=52, y=235)
        time.sleep(4)
        



def botIdade():
      # Começo do bot

        # Abertura do relatório
        pyautogui.click(x=722, y=111)
        time.sleep(0.7)
        time.sleep(1)

        # Click em atendimento
        pyautogui.click(x=557, y=101)
        time.sleep(0.7)
        time.sleep(1)

        datainicial=1
        
    
        # 1 Data
        data_escrever_01 = f"0+{str(datainicial)}+{str(mes)}+{str(ano)}"
        pyautogui.click(x=492, y=163)
        time.sleep(0.7)
        pyautogui.write(data_escrever_01, interval=0.1)

        # 2 Data
        data_escrever_02 = f"{str(ultimo_dia_do_mes)}+{str(mes)}+{str(ano)}"
        pyautogui.click(x=628, y=162)
        time.sleep(0.7)
        pyautogui.write(data_escrever_02, interval=0.1)

        # Selecionando o status
        pyautogui.click(x=646, y=204)
        time.sleep(0.7)
        time.sleep(0.7)
        pyautogui.click(x=495, y=260)
        time.sleep(0.7)
        time.sleep(1)

        # Selecionando a unidade
        pyautogui.doubleClick(x=929, y=242)
        pyautogui.typewrite('up')
        pyautogui.click(x=497, y=321)
        time.sleep(0.7)
        time.sleep(1.2)

        contador=1
        for _ in range(5):
            # idades

            # De 0 a 1
            if contador ==1:
                pyautogui.click(x=698, y=204)
                time.sleep(0.7)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('0')

                pyautogui.click(x=760, y=203)
                time.sleep(0.7)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('1')
                contador+=1
            
            # De 1 a 4
            elif contador ==2:
                pyautogui.click(x=698, y=204)
                time.sleep(0.7)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('1')

                pyautogui.click(x=760, y=203)
                time.sleep(0.7)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('4')
                contador+=1
            # De 1 a 4
            elif contador ==3:
                pyautogui.click(x=698, y=204)
                time.sleep(0.7)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('5')

                pyautogui.click(x=760, y=203)
                time.sleep(0.7)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('9')
                contador+=1
            # De 1 a 4
            elif contador ==4:
                pyautogui.click(x=698, y=204)
                time.sleep(0.7)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('10')

                pyautogui.click(x=760, y=203)
                time.sleep(0.7)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('14')
                contador+=1
            # De 1 a 4
            elif contador ==5:
                pyautogui.click(x=698, y=204)
                time.sleep(0.7)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('15')

                pyautogui.click(x=760, y=203)
                time.sleep(0.7)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('16')
                contador+=1

           

            # Selecionando Imprimir
            pyautogui.click(x=907, y=705)
            time.sleep(0.7)
            time.sleep(4)

            # Alterando o zoom
            pyautogui.click(x=194, y=39)
            time.sleep(0.7)
            # Zoom 75%
            pyautogui.click(x=174, y=84)
            time.sleep(0.7)
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
            pyautogui.click(x=57, y=216)
            time.sleep(4)
            # Scroll para lado
            pyautogui.click(x=1331, y=709)
            time.sleep(0.7)
            pyautogui.hotkey('alt', 'tab')
            
            # fechamento
            pyautogui.click(x=599, y=40)
        # voltar na tabela
        time.sleep(0.7)
        pyautogui.hotkey('alt', 'tab')



# Adiciona manipuladores de evento para as tecla de ativação
keyboard.add_hotkey("F1", botTotal)

keyboard.add_hotkey("F2", botCor)

keyboard.add_hotkey("F3", botIdade)

keyboard.add_hotkey("F4", botDia)


# Mantenha o programa em execução
keyboard.wait("esc")
