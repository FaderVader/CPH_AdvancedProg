# print(ord('A')) # ord() returns the Unicode value of the input char
# chr() returns the Unicode char defined by int-arg (0 - 1,114,111)

def cypherize(input, offset=1): # offset: default value
    result = ''.join([chr(ord(char) + offset) for char in input])
    return result

key = 20
sentence = "½1'ø¨¨^'*}]@£$"
encoded = cypherize(sentence, key)
decoded = cypherize(encoded, -key)

print(encoded)
print (f'Decode was successfull: {decoded == sentence}') #  == sentence
