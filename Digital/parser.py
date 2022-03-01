#Python Parser converting bits to bytes

import os

file = open("Byte-Test-B.raw", 'rb')
byte = file.read(1)
bit_list = []
file_size = os.path.getsize("Byte-Test-B.raw")
print(file_size)

for i in range (0, file_size):
	if file.read(1) == b'\x00':
		bit_list.append(0)
	else:
		bit_list.append(1)
					
file.close()
#print("Bit List: " , bit_list)

# ->shift bits

# ->go from bits to bytes
bit_str = ""
for b in bit_list:
	bit_str += str(b)

#print(bit_str)
shift_amount = bit_str.find('0100000101000010')
print("Shifted by: ", shift_amount)
shifted_str = bit_str[shift_amount :]
#print(shifted_str)

file = open("parser_output.raw", 'w')
file.write("")
file.close()

file = open("parser_output.raw", 'a')

while len(bit_str) >= 8:
	file.write(chr(int(shifted_str[0 : 8], 2)))
	shifted_str = shifted_str[8 :]
file.close()
#byte = int("10100101", 2)
