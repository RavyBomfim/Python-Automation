# Steps for building the code (Passos para a construção do código)

# Step 1 - Access the registration system/page (Passo 1 - Acessar o sistema de cadastro)
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Step 2 - Log in (Passo 2 - Fazer login)
# Step 3 - Import the database (Passo 3 - Importar a base de dados)
# Step 4 - Register a product (Passo 4 - Cadastrar um produto)
# Step 5 - Repeat the process until all products in the database are registered (Passo 5 - Repetir o processo até cadastrar todos os produtos da base de dados)

# Import libraries (Importar bibliotecas)
import pyautogui, time

# Pausa de 1 segundo entre cada comando
pyautogui.PAUSE = 1
# Aperta a tecla do windows
pyautogui.press('win')
# Escreve o nome chrome na barra de pesquisa
pyautogui.write('chrome')
# Pressina a tecla ENTER para abrir o google chrome
pyautogui.press('enter')
# Utilizando o método sleep para aguardar a tela carregar antes do próximo comando
time.sleep(3)
# Dando click na posição da tela onde se encontra a conta do google escolhida para navegar
pyautogui.click(x=598, y=320)
# Utilizando o método sleep novamente
time.sleep(3)
# Pegando a janela pelo título dela e armazenando na variável window
window = pyautogui.getWindowsWithTitle('Nova guia')[0]
# O método maximize irá maximizar a janela caso ela esteja minimizada
window.maximize()
# Amazenando o link de acesso à página de login do sistema de cadastro de produtos em uma variável
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
# Digitando o link de login
pyautogui.write(link)
# Pressionando a tecla enter para acessar a página
pyautogui.press('enter')
# Utilizando o método sleep novamente para aguardar o carregamento da página
time.sleep(5)
# Clicando na posição da tela onde o campo de email se encontra
pyautogui.click(x=437, y=410)
# Escrevendo o email de login
pyautogui.write('test@gmail.com')
# Pressionando a tecla TAB para o focus mudar para o campo de senha
pyautogui.press('tab')
# Escrevendo a senha de login
pyautogui.write('test7357')
# Pressionando a tecla ENTER para efetuar login
pyautogui.press('enter')