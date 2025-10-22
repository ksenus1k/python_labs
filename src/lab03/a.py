def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text=text.casefold()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    text=text.replace('\t',' ').replace('\r',' ').replace('\n',' ')
    text=' '.join(text.split())
    text=text.strip()
    return text
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

import re
def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*',text)
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

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
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))
print(top_n(count_freq(["a","b","a","c","b","a"])))
print(top_n(count_freq(["bb","aa","bb","aa","cc"])))