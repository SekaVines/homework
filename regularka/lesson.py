import re

my_text = 'Vasya, 1998, vasy@gmail.com,' \
          'Adi, 1998, adi@gmail.com,' \
          'Aid, 1998, aidy@gmail.com,' \
          'Dilara, 1998, dilara@gmail.com,' \
          'Mika, 1998, mika@gmail.com,' \
          'Aibek, 1998, aibek@gmail.com,' \
          'Adilet, 2000, adilet@yandex.ru'

"""

\d = Он ищет любые подряд стоящие числа [0-9]


[0-9]{любой порядок который вам нужен} = аналог \d
\D =  Он ищет любые не числа
\w = Любой алфавитный символ [A-Z a-z]
\W
[A-Z a-z]+ = ищем алфавитный порядок + это любая последовательность
# """
#
# searching = r'@(?!gmail.com)(?!yandex.ru)\w+.\w+'
# results = re.findall(searching, my_text)
# print(results)

file_path = 'sdfg.txt'
result_file_path = 'result.txt'
file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_1 = file_reader.read()

searching = r'[\w+_-]+@[\w+_-]+.[\w+]+'
results_all = re.findall(searching, my_text_1)

for item in results_all:
    print(item)
    result_file.write(item + '\n', ), 'f Total : {str(len(results_all))})'

print(f'Total : {str(len(results_all))}')
