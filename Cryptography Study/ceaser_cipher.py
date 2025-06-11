def ceaser_cipher(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)


    return result 

text = "apple"
s = -2

print("Text : " + text)
print("Shift : " + str(s))
print("Code: " + ceaser_cipher(text,s))
print("De-Code: " + ceaser_cipher(text,s+4))


