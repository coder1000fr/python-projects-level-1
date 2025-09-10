from collections import Counter

sample_text = ('this is a sample text for test this code'
               'and this is another sample text for test this code')

words_dic = Counter(sample_text.split())

print(f'{"WORD":>10}{"COUNT":>8}')
for word, count in words_dic.items():
    print(f'{word:>10}{count:>4}')