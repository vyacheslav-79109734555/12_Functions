def decision(txt):
    letter_low = txt[0]
    letter_big = chr(ord(letter_low) - ord('a') + ord('A'))
    return letter_big + txt[1:]


word = input('Введите предложение: ').split()
text = []

for t in word:
    text.append(decision(t))
print(' '.join(text))
