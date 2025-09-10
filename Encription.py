import string

letters = string.ascii_lowercase
print(letters)

text = input("Enter a string: ")

encripted_text = ''
for i in text:
    if i in ' .,:()#':
        encripted_text += i
    else:
        index = letters.find(i)
        if index + 3 >= len(letters):
            new_index = 0
            new_index = 3 - len(letters[index:])
            new_letter = letters[new_index]

        else:
            new_letter = letters[index + 3]

    encripted_text += new_letter

print(encripted_text)