# this function takes an integer and converts it into binary
def int2bin(integer):
    if integer == 0:
        return "00000000"
    binString = ""
    while integer:
        if integer % 2 == 1:
            binString = "1" + binString
        else:
            binString = "0" + binString
        integer //= 2
        
    while (len(binString)% 8) != 0:
        binString = "0" + binString
    return binString


def xorbit(binary, key):
    cyphertext = ""
    for i in range(len(binary)):
        cyphertext = cyphertext + str(int(binary[i]) ^ int(key[i % len(key)]))
    return cyphertext


def bin2int(binary):
    return int(binary, 2)

key1 = int2bin(25642)
binary1 = "0100011101001111"
print(xorbit(binary1, key1))

print(bin2int(binary1))

binary2 = "0100110101011010"
key2 = int2bin(44867)
cyphertext2 = xorbit(binary2, key2)
print(cyphertext2)
