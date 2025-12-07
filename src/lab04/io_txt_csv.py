import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    try:
        p = Path(path)
        return p.read_text(encoding=encoding)
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return ""
    except UnicodeDecodeError:
        print(f"Ошибка кодировки: {path}")
        return ""
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return ""


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    p = Path(path)
    with p.open("w", newline="", encoding="utf-8") as file:
        f = csv.writer(file)
        if header is None and rows == []:
            file_c.writerow(("a", "b"))
        if header is not None:
            f.writerow(header)
        if rows != []:
            const = len(rows[0])
            for i in rows:
                if len(i) != const:
                    return ValueError
        f.writerows(rows)


def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


print(read_text(r"C:\Users\ksen\Desktop\python_labs\src\data\input.txt"))
write_csv(
    [("word", "count"), ("test", 3)],
    r"C:\Users\ksen\Desktop\python_labs\src\data\check.csv",
)
