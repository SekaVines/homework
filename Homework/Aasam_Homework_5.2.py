import re

file_path = 'MOCK_DATA.txt'
fullname_results_path = 'fullname_result.txt'
file_reader = open(file_path, mode='r', encoding='Latin-1')
fullname_results = open(fullname_results_path, mode='w', encoding='Latin-1')
my_text_1 = file_reader.read()

searching = r"[A-Z][a-z]+\W+\w+\s[A-Z]\w+|[A-Z]+\w+\s[A-Z]+\w+|[A-Za-z][A-Za-z]+\s[A-Za-z][']?[A-Z]\w+"
results_all = re.findall(searching, my_text_1)

for item in results_all:
    print(item)
    fullname_results.write(item + '\n', ), 'f Total : {str(len(results_all))})'

print(f'Total : {str(len(results_all))}')

file_path_1 = 'MOCK_DATA.txt'
email_results_path = 'email_result.txt'
file_reader_1 = open(file_path_1, mode='r', encoding='Latin-1')
email_results = open(email_results_path, mode='w', encoding='Latin-1')
my_text_2 = file_reader_1.read()

searching = r'[\w+_-]+@[\w+_-]+.[\w+]+'
results_all_1 = re.findall(searching, my_text_2)

for item in results_all_1:
    print(item)
    email_results.write(item + '\n', )
print(f'Total : {str(len(results_all_1))}')

file_path_2 = 'MOCK_DATA.txt'
results_2 = 'result_2.txt'
file_reader_2 = open(file_path_2, mode='r', encoding='Latin-1')
results__2 = open(results_2, mode='w', encoding='Latin-1')
my_text_3 = file_reader_2.read()

searching = f"[A-Z]+[a-z]+[A-Z]+[a-z]+[A-Z]+[a-z]+[.]+[a-z]+[0-9]|[A-Z]+[a-z]+[A-Z]+[a-z]+[A-Z]+[a-z]+[.]+[a-z]+|[" \
            f"A-Z]+[a-z]+[A-Z]+[a-z]+[.]+[a-z]+[0-9]|[A-Z]+[a-z]+[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+[0-9]|[" \
            f"A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+[0-9] "
results_all_2 = re.findall(searching, my_text_3)

for item in results_all_2:
    print(item)
    results__2.write(item + '\n', )
print(f'Total : {str(len(results_all_2))}')

file_path_3 = 'MOCK_DATA.txt'
results_3 = 'result_3.txt'
file_reader_4 = open(file_path_3, mode='r', encoding='Latin-1')
results__3 = open(results_3, mode='w', encoding='Latin-1')
my_text_4 = file_reader_4.read()

searching = f'#\w+'
results_all_3 = re.findall(searching, my_text_4)

for item in results_all_3:
    print(item)
    results__3.write(item + '\n', )
print(f'Total : {str(len(results_all_3))}')
