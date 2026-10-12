"""
Программа 1 (worker1) — вариант 8.

Ищет в каталоге /var/data самый большой по объёму файл
и перекладывает его содержимое в /var/result/data.txt.
"""
import os
import shutil

DATA_DIR = "/var/data"
RESULT_DIR = "/var/result"
RESULT_FILE = os.path.join(RESULT_DIR, "data.txt")


def find_largest_file(directory: str) -> str:
    """Возвращает путь к самому большому по размеру файлу в каталоге."""
    files = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]
    if not files:
        raise FileNotFoundError(f"В каталоге {directory} нет файлов")

    largest = max(files, key=os.path.getsize)
    return largest


def main() -> None:
    os.makedirs(RESULT_DIR, exist_ok=True)

    print(f"[worker1] Сканирую каталог: {DATA_DIR}")
    files = os.listdir(DATA_DIR)
    print(f"[worker1] Найдено файлов: {len(files)}")

    for f in files:
        path = os.path.join(DATA_DIR, f)
        if os.path.isfile(path):
            print(f"  - {f}: {os.path.getsize(path)} байт")

    largest = find_largest_file(DATA_DIR)
    print(f"[worker1] Самый большой файл: {largest} ({os.path.getsize(largest)} байт)")

    shutil.copyfile(largest, RESULT_FILE)
    print(f"[worker1] Скопирован в: {RESULT_FILE}")

    with open(RESULT_FILE, "r", encoding="utf-8") as fp:
        content = fp.read()
    print(f"[worker1] Содержимое результата: {content.strip()}")


if __name__ == "__main__":
    main()
