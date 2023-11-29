@echo off
echo                                             Bem-vindo ao Bot de Indicadores!
echo.
echo.
echo                                                      Manual de uso
echo                                                  Cetifique-se SEMPRE! 
echo                              1 - O RGsystem deve esta logado e aberto na aba de atendimento.
echo                    2 - Arquivo do exel deve esta aberto como segundo plano para que o alt - tab va ate ele.  
echo.
echo.

REM Obtém o diretório do script atual
set "script_dir=%~dp0"

REM Solicita as informações diretamente do usuário
set /p mes="Didite o mes da pesquisa? OBS.: 01=janeiro 02=fevereiro ... 12=Dezembro: "
set /p ultimo_dia_do_mes="Digite o ultimo dia deste mes? "
set /p ano="Digite o ano? "
echo.
echo                                       ** LEMBRANDO DA RESOLUCAO PADRAO DEVE SER **
echo                                                    ** 1920 X 1080 **

echo                                        - Pressione 'F1' para iniciar o BOT_TOTAL.
echo                                         - Pressione 'F2' para encerrar o BOT_COR.
echo                                        - Pressione 'F3' para encerrar o BOT_IDADE.
echo                                         - Pressione 'F4' para encerrar o BOT_DIAS.
echo.
REM Chama o script Python passando os parâmetros
call python "%script_dir%scripts\botIndicadores.py" %mes% %ultimo_dia_do_mes% %ano%

rem Pausa o script para visualizar mensagens antes de fechar
pause > nul
