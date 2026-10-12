"""
Программа 2 (worker2) - вариант 8.
"""
import os

DATA_FILE = "/var/data/data.txt"
RESULT_DIR = "/var/result"
RESULT_FILE = os.path.join(RESULT_DIR, "result.txt")


def parse_numbers(path: str):
    with open(path, "r", encoding="utf-8-sig") as fp:
        content = fp.read()
    return [int(x) for x in content.split() if x.strip()]


def main() -> None:
    os.makedirs(RESULT_DIR, exist_ok=True)
    print(f"[worker2] Читаю файл: {DATA_FILE}")
    numbers = parse_numbers(DATA_FILE)
    print(f"[worker2] Получено чисел: {len(numbers)}")

    if not numbers:
        print("[worker2] Файл пустой, нет чисел.")
        return

    minimum = min(numbers)
    count = numbers.count(minimum)

    print(f"[worker2] Наименьшее число: {minimum}")
    print(f"[worker2] Количество таких чисел: {count}")

    with open(RESULT_FILE, "w", encoding="utf-8") as fp:
        fp.write(str(count))

    print(f"[worker2] Результат записан в: {RESULT_FILE}")
    print(f"[worker2] Содержимое: {count}")


if __name__ == "__main__":
    main()