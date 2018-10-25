# this script takes an integer and converts it into binary


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


print(int2bin(25642))
print(len(int2bin(25642)))
