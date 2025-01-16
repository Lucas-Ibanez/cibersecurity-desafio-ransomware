import os ## Bibiloteca que nos permite acessar comandos do Sistema Operacional
import pyaes ## Biblioteca responsável por fazer a descriptografia dos dados

## abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll" ## Vamos colocar entre "" o nome do arquivo que desejamos descriptografar
file = open(file_name, "rb") ## Vamos abrir esse arquivo com o comando "open", e insinuar que vamos lê-lo, usando o "rb"
file_data = file.read() ## Vamos ler todo o conteúdo do arquivo com o comando "read"
file.close() ## Vamos fechar o arquivo

## chave para descriptografia
key = b"testeransomwares" ## Vamos passar a chave de descriptografia (ela tem que ser a mesma usada para criptografar o arquivo)
aes = pyaes.AESModeOfOperationCTR(key) ## Vamos iniciar a função de descriptografia com base na nossa chave
decrypt_data = aes.decrypt(file_data) ## Vamos descriptografar o arquivo desejado, usando o comando "decrypt"

## remover o arquivo criptografado
os.remove(file_name) ## Vamos remover o arquivo criptografado do sistema

## criar o arquivo descriptografado
new_file = "teste.txt" ## Vamos criar um novo arquivo
new_file = open(f'{new_file}', "wb") ## Vamos abrir esse novo arquivo com o comando "open", e insinuar que vamos escrever nele, usando o "wb"
new_file.write(decrypt_data) ## Vamos passar o conteúdo descriptografado para esse novo arquivo, usando o comando "write"
new_file.close() ## Vamos fechar esse arquivo
