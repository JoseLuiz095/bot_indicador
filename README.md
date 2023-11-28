# Bot Semi-Automático para Busca e Transcrição de Relatórios

Bem-vindo ao repositório do Bot Semi-Automático desenvolvido para buscar relatórios diários no sistema RGS (rgsystem) e transcrever os dados de forma escrita. Este bot é útil especialmente quando o sistema RGS não permite a cópia direta dos dados, apenas a visualização.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o bot:

- pyautogui
- keyboard
- python

Você pode instalá-las utilizando o seguinte comando:

```bash
pip install pyautogui keyboard
```

## Modo de Uso

1. Clone este repositório para o seu ambiente local.

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto.

   ```bash
   cd nome-do-repositorio
   ```

3. Execute o script via prompt de comando.

   ```bash
   python bot.py
   ```

4. Inicie o sistema pressionando a tecla "F1". O bot realizará a busca dos relatórios do dia no sistema RGS e transcreverá os dados de forma escrita.

Lembre-se de que este bot está atualmente configurado para buscar relatórios do dia. No entanto, há planos futuros para aprimorar o bot, permitindo que ele realize buscas mais abrangentes para atender a todos os dados necessários para seus indicadores.

### Bot de Indicadores - Manual de Uso

Certifique-se SEMPRE de:

1. O RGsystem deve estar logado e aberto na aba de atendimento.
2. O arquivo do Excel deve estar aberto como segundo plano para que o atalho Alt + Tab vá até ele.

Digite o mês da pesquisa (01=janeiro, 02=fevereiro, ..., 12=dezembro): 11
Digite o último dia deste mês: 30

**LEMBRANDO DA RESOLUÇÃO PADRÃO DEVE SER 1920 X 1080**

- Pressione 'F1' para iniciar o BOT_TOTAL.
- Pressione 'F2' para encerrar o BOT_COR.
- Pressione 'F3' para encerrar o BOT_IDADE.
- Pressione 'F4' para encerrar o BOT_DIAS.

Certifique-se de verificar e instalar as dependências antes de executar o bot.

Fique à vontade para contribuir com melhorias, sugestões ou relatar problemas abrindo uma issue neste repositório.

Divirta-se automatizando suas tarefas diárias! 😊
