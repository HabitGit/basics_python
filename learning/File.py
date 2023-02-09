#data = input('Введите текст: ')

#file = open('data/text.txt', 'a')
#r- для чтения
#w- режим для чтения и перезаписи
#a - для добавления информации к текущему предидущему знацению
#file.write(data + '\n')
#file.close()

file = open('../data/text.txt', 'r')
#print(file.read())

for line in file:
    print(line, end="")
file.close()