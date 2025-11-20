import argparse
import sys
import os
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", "--number", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество наиболее частых слов")

    args = parser.parse_args()
    filepath = Path(args.input)

    if not filepath.exists():
        raise FileNotFoundError(f"Файл не найден: {filepath}")

    if args.command == "cat":
        """ Реализация команды cat """
        with filepath.open("r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, 1):
                line = line.rstrip("\n")
                if args.number:
                    print(f"{line_number}: {line}")
                else:
                    print(line)
                    
    elif args.command == "stats":
        """ Реализация команды stats """
        with filepath.open("r", encoding="utf-8") as file:
            text = file.read()

        tokens = tokenize(text=text)
        freq = count_freq(tokens=tokens)
        top_words = top_n(freq=freq, n=args.top)
        
        print(f"Топ-{args.top} самых частых слов:")
        for word, count in top_words:
            print(f"{word} - {count}")

if __name__ == "__main__":
    main()