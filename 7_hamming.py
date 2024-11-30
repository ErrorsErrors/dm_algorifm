data = "101111111111001100000110001000011001111000001010000111000111011100101110110100110011110010110000010000000"

m = len(data)
r = 0

while 2**r < m + r + 1:
    r += 1

codeword = ['0'] * (m + r)

j = 0
for i in range(m + r):
    if (i + 1) & i == 0:
        continue
    codeword[i] = data[j]
    j += 1
    
for i in range(r):
    parity_bit_position = 2**i - 1
    parity = 0
    for j in range(m + r):
        if j & (2**i - 1) == parity_bit_position:
            parity ^= int(codeword[j])
    codeword[parity_bit_position] = str(parity)
    
encoded = ''.join(codeword)
rate = len(data) / len(encoded)

print("Закодированная строка:", encoded)
print("Коэффициент избыточности:", rate)
