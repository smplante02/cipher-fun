import enchant

# Fun with cipher encoding and decoding (Caesar and ROT13)

def encodeCaesar(string, shiftNum):
    finalString = ''
    for c in string:
        if c.isupper():
            unicodeVal = ord(c)
            new = (unicodeVal - 65 + shiftNum) % 26 + 65
            finalString = finalString + chr(new)
        elif c.islower():
            unicodeVal = ord(c)
            new = (unicodeVal - 97 + shiftNum) % 26 + 97
            finalString = finalString + chr(new)
        else:
            finalString = finalString + c

    return finalString


def decodeCaesarSimple(string, shiftNum):
    finalString = ''
    for c in string:
        if c.isupper():
            unicodeVal = ord(c)
            new = (unicodeVal - 65 - shiftNum) % 26 + 65
            finalString = finalString + chr(new)
        elif c.islower():
            unicodeVal = ord(c)
            new = (unicodeVal - 97 - shiftNum) % 26 + 97
            finalString = finalString + chr(new)
        else:
            finalString = finalString + c

    return finalString

def decodeCaesarComplex(str):
    result = ''
    # setting up a dictionary to compare words to
    englishWords = enchant.Dict("en_US")

    # brute force method to decode the caesar cipher
    for i in range(26):
        potentialString = decodeCaesarSimple(str, i)
        divide = potentialString.split()
        if divide == '':
            return ''
        else:
            for word in divide:
                # if not an english word, break
                if not englishWords.check(word):
                    result = ''
                    break
                else:
                    if not result == '':
                        # not the first word
                        result = result + ' ' + word
                    else:
                        # first word
                        result = result + word
            if not result == '':
                return result


def encodeROT13(str):
    # ROT13 (rotate 13) is a special Caesar cipher that only shifts by 13
    return encodeCaesar(str, 13)

def decodeROT13(str):
    return decodeCaesarSimple(str, 13)

# examples inspired by resident geckos
print('Caesar Cipher Shift 5')
print('Encoding:', encodeCaesar('Gandalf the Leopard Gecko', 5))
print('Decoding:', decodeCaesarComplex('Lfsifqk ymj Qjtufwi Ljhpt'))

print('\nROT13 Cipher')
print('Encoding:', encodeROT13('Dot the Crested Gecko'))
print('Decoding:', decodeROT13('Qbg gur Perfgrq Trpxb'))

