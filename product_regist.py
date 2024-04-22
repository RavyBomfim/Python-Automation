# Steps for building the code (Passos para a construção do código)

# Step 1 - Access the registration system/page (Passo 1 - Acessar o sistema de cadastro)
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Step 2 - Log in (Passo 2 - Fazer login)
# Step 3 - Import the database (Passo 3 - Importar a base de dados)
# Step 4 - Register a product (Passo 4 - Cadastrar um produto)
# Step 5 - Repeat the process until all products in the database are registered (Passo 5 - Repetir o processo até cadastrar todos os produtos da base de dados)

# Import libraries (Importar bibliotecas)
import pyautogui, time

# 1 second pause between each command (Pausa de 1 segundo entre cada comando)
pyautogui.PAUSE = 1

# Press the Windows key (Aperta a tecla do windows)
pyautogui.press('win') 

# Write the name chrome in the search bar (Escreve o nome chrome na barra de pesquisa)
pyautogui.write('chrome')

# Press the ENTER key to open Google Chrome (Pressiona a tecla ENTER para abrir o google chrome)
pyautogui.press('enter')

# Using the sleep method to wait for the screen to load before the next command (Utilizando o método sleep para aguardar a tela carregar antes do próximo comando)
time.sleep(3)

# Clicking on the position on the screen where the Google account chosen to browse is located (Dando click na posição da tela onde se encontra a conta do google escolhida para navegar)
pyautogui.click(x=598, y=320)

# Using the sleep method again (Utilizando o método sleep novamente)
time.sleep(3)

# Taking the window by its title and storing it in the window variable (Pegando a janela pelo título dela e armazenando na variável window)
window = pyautogui.getWindowsWithTitle('Nova guia')[0]

# The maximize method will maximize the window if it is minimized (O método maximize irá maximizar a janela caso ela esteja minimizada)
window.maximize()

# Storing the access link to the product registration system login page in a variable (Amazenando o link de acesso à página de login do sistema de cadastro de produtos em uma variável)
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# Entering the login link (Inserindo o link de login)
pyautogui.write(link)

# Pressing the enter key to access the page (Pressionando a tecla enter para acessar a página)
pyautogui.press('enter')

# Using the sleep method again to wait for the page to load (Utilizando o método sleep novamente para aguardar o carregamento da página)
time.sleep(5)

# Clicking on the position on the screen where the email field is located (Clicando na posição da tela onde o campo de email se encontra)
pyautogui.click(x=437, y=410)

# Writing the login email (Escrevendo o email de login)
pyautogui.write('test@gmail.com')

# Pressing the TAB key causes the focus to change to the password field (Pressionando a tecla TAB para o focus mudar para o campo de senha)
pyautogui.press('tab')

# Entering password to login (Digitando a senha de login)
pyautogui.write('test7357')

# Pressing the ENTER key to log in (Pressionando a tecla ENTER para efetuar login)
pyautogui.press('enter')