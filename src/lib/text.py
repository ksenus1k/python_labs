import re
import unicodedata


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result = text
    if yo2e:
        result = result.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        result = result.casefold()
    result = "".join(
        char if not unicodedata.category(char).startswith("C") or char == "\n" else " "
        for char in result
    )
    result = re.sub(r"\s+", " ", result)
    return text


def tokenize(text: str) -> list[str]:
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
