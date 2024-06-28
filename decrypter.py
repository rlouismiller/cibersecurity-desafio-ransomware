import os
import pyaes

#abrir

file_name = 'teste.txt.trolado'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#chave

key = b'0123456789ABCDEF'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#remover
os.remove(file_name)

#criar novo arquivo
new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
