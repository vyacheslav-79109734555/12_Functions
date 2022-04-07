def decision(txt):
    return chr(ord(txt[0]) + ord('A') - ord('a')) + txt[1:]


word = [str(word) for word in input('Введите предложение: ').lower().split()]
for i in range(len(word)):
    word[i] = decision(word[i])
print(' '.join(str(i) for i in word))
