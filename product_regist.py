# Steps for building the code (Passos para a construção do código)

# Step 1 - Access the registration system/page (Passo 1 - Acessar o sistema de cadastro)
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Step 2 - Log in (Passo 2 - Fazer login)
# Step 3 - Import the database (Passo 3 - Importar a base de dados)
# Step 4 - Register a product (Passo 4 - Cadastrar um produto)
# Step 5 - Repeat the process until all products in the database are registered (Passo 5 - Repetir o processo até cadastrar todos os produtos da base de dados)

#########################################################################################################

##### Step 1 - Access the registration system/page (Passo 1 - Acessar o sistema de cadastro)

# Import libraries (Importar bibliotecas)
import pyautogui, time

# 1 second pause between each command (Pausa de 1 segundo entre cada comando)
pyautogui.PAUSE = 0.5

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

#########################################################################################################

##### Step 2 - Log in (Passo 2 - Fazer login)

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

# 3 second pause to wait for the page to load (Pausa de 3 segundos para aguardar carregamento da página)
time.sleep(3)

#########################################################################################################

##### Step 3 - Import the database (Passo 3 - Importar a base de dados)

# Installation of pandas, numpy and openpyxl with the following command in the terminal (Instalação do pandas, numpy e openpyxl com o seguinte comando no terminal): 
''' pip install pandas numpy openpyxl '''

# Importing the pandas library (Importando a biblioteca pandas)
import pandas

# Reading the csv file and saving the information in a variable (Lendo o arquivo csv e guardando as informações em uma variável)
table = pandas.read_csv('products.csv')

# Prints the file information stored in the table variable (Imprime as informações do arquivo armazenado na variável table)
print(table)

#########################################################################################################

##### Step 4 - Register a product (Passo 4 - Cadastrar um produto)

''' # Clicking on the position on the screen where the Product code field is located (Clicando na posição da tela onde está o campo Código do produto)
pyautogui.click(x=384, y=296)

# Entering the product code (Inserindo o código do produto)
pyautogui.write('MOLO000251')

# Pressing the tab key to move to the next field (Pressionando a tecla tab para mudar para o próximo campo)
pyautogui.press('tab')

# Entering the product brand (Inserindo a marca do produto)
pyautogui.write('Logitech')

# Move to the next field (Passar para o próximo campo)
pyautogui.press('tab')

# Entering the product type (Inserindo o tipo do produto)
pyautogui.write('Mouse')

# Move to the next field (Passar para o próximo campo)
pyautogui.press('tab')

# Entering the category (Inserindo a categoria)
pyautogui.write('1') # or pyautogui.write(str(1))

# Move to the next field (Passar para o próximo campo)
pyautogui.press('tab')

# Entering the unit price (Inserindo o preço unitário)
pyautogui.write('25.95') # or pyautogui.write(str(25.95))

# Move to the next field (Passar para o próximo campo)
pyautogui.press('tab')

# Entering the cost of the product (Inserindo o custo do produto)
pyautogui.write('6.5') # or pyautogui.write(str(6.5))

# Move to the next field (Passar para o próximo campo)
pyautogui.press('tab')

# Entering a note, if any (Inserindo uma observação, se houver)
# Entering a note (Inserindo uma observação)
pyautogui.write('')

# Pressing the tab key to move to the send button (Pressionando a tecla Tab para ir para o botão enviar)
pyautogui.press('tab')

# Pressing the enter key to send the product registration information (Apertando a tecla Enter para enviar as informações de cadastro do produto)
pyautogui.press('enter') '''

#########################################################################################################

##### Step 5 - Repeat the process until all products in the database are registered (Passo 5 - Repetir o processo até cadastrar todos os produtos da base de dados)

# The table.index accesses the table rows, if I wanted to access the columns, I would use table.column instead of index. (O table.index acessa as linhas da tabela, se eu quisesse acessar as colunas, utilizaria o table.column ao invés do index.)

for row in table.index:
    # Position on the screen where the Product code field is located (Posição da tela onde está o campo Código do produto)
    pyautogui.click(x=384, y=296)

    # Product code (Código do produto)
    code = table.loc[row, 'codigo']
    pyautogui.write(code)
    pyautogui.press('tab')

    # Product brand (Marca do produto)
    pyautogui.write(table.loc[row, 'marca'])
    pyautogui.press('tab')

    # Product type (Tipo do produto)
    pyautogui.write(table.loc[row, 'tipo'])
    pyautogui.press('tab')

    # Category (Categoria)
    pyautogui.write(str(table.loc[row, 'categoria']))
    pyautogui.press('tab')

    # Unit price (Preço unitário)
    pyautogui.write(str(table.loc[row, 'preco_unitario']))
    pyautogui.press('tab')

    # Cost of the product (Custo do produto)
    pyautogui.write(str(table.loc[row, 'custo'])) # or pyautogui.write(str(6.5))
    pyautogui.press('tab')

    # Entering a note, if any (Inserindo uma observação, se houver)
    note = table.loc[row, 'obs']
    if not pandas.isna(note):
        pyautogui.write(note)

    # Pressing the tab key to move to the send button (Pressionando a tecla Tab para ir para o botão enviar)
    pyautogui.press('tab')

    # Pressing the enter key to send the product registration information (Apertando a tecla Enter para enviar as informações de cadastro do produto)
    pyautogui.press('enter')

    # Scroll the page up (Rola a página para cima)
    pyautogui.scroll(5000)