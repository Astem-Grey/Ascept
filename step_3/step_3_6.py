s = ''

def pull_letters(word):
    """ Функция чисто под задачу этого задания(универс = 0)"""
    primer = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
              'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
              'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    word = list(word)
    perm = word[0]
    word.pop(0)
    word.insert(0, primer.get(perm))
    word = ''.join(word)
    return word




    #return word.capitalize()
sentence2 = []
sentence = input('Введите предложение маленькими латинскими буквами').split(' ')
# sentence = input('Введите предложение маленькими латинскими буквами')

for i in sentence:
    sentence2.append(pull_letters(i))

print(' '.join(sentence2))

# print(sentence.title())
# Времени оставалось мало поэтому основаной лист не стал перезаписывать(с целью сохрениения оперативной памяти)
# А просто создал новый. И так опоздал со здачей работы