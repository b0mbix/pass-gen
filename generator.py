import random

def generating_pass(number, options):
    #all chars that can be in pass
    possible = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['!', '@', '#', '$', '%', '^', '&', '*', '?', '+', '=', '-']]

    #defining all chars that'll be in this pass
    symbols = []
    for i in range(4):
        if options[i] == 'y':
            for j in possible[i]:
                symbols.append(j)

    #generating and returning pass
    chars = []
    for i in range(number):
        chars.append(symbols[random.randint(0, len(symbols)-1)])
    result = ''.join(chars)

    return result
