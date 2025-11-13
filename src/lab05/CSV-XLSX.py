from openpyxl import Workbook
import csv
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")  
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    try:
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader) 
            if not rows:
                raise ValueError("CSV файл пуст")
            for row in rows:
                ws.append(row)
            for column in ws.columns:
                if column:
                    mx = max(len(str(cell.value)) for cell in column)
                    ws.column_dimensions[column[0].column_letter].width = max(mx + 2, 8)
        wb.save(xlsx_path)
    except csv.Error as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
csv_to_xlsx('C:/Users/ksen/Desktop/python_labs/src/data/samples/cities.csv', 'C:/Users/ksen/Desktop/python_labs/src/data/out/cities.xlsx')
csv_to_xlsx('C:/Users/ksen/Desktop/python_labs/src/data/samples/people.csv', 'C:/Users/ksen/Desktop/python_labs/src/data/out/people.xlsx')