'''6.4 Из заданной строки получить список слов,
у которых третья с конца буква согласная, а предпоследняя – гласная.'''

import re

line = input("Введите строку: ")

pattern = r"\b\w*[^аоуыэеёюяиaeiouy\s][аоуыэеёюяиaeiouy]\w\b"
print(re.findall(pattern, line, flags=re.IGNORECASE))
