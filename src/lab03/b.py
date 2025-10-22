import sys
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text=text.casefold()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    text=text.replace('\t',' ').replace('\r',' ').replace('\n',' ')
    text=' '.join(text.split())
    text=text.strip()
    return text

import re
def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*',text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    dictionary={}
    for i in tokens:
        value=dictionary.get(i,0)
        dictionary[i]=value+1
    return dictionary

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    s=[]
    for word, count in freq.items():
        s.append((-count,word))
    s.sort()
    result=[]
    for neg_count, word in s:
        result.append((word,-neg_count))
    return result[:n]
a = "Привет, мир! Привет!!!"
nt=normalize(a)
allwords=tokenize(nt)
uw=count_freq(allwords)
top=top_n(uw,5)
print(f'Всего слов: {len(allwords)}')
print(f"Уникальных слов: {len(uw)}")
print("Топ-5:")
for y in top:
    print(y[0] + ': ' + str(y[1]))
