# with open('data_prog_contest_problem_2.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
# print(content)
#
# content = content.split()
# content = list(map(int, content))
#
# count = 0
# max_mas = []
# for i in range(1, content[0]):
#     if (content[i] + 1 == content[i+1]) or (content[i] == 26 and content[i+1] == 1):
#         print(content[i])
#         count += 1
#     else:
#         max_mas.append(count)
#         count = 0
#
#
# print(max_mas)
# print(max(max_mas))

def min_alphabet_window(arr):
    """
    arr — список целых 1..26.
    Возвращает минимальную длину фрагмента,
    содержащего все числа 1..26,
    или None, если такого нет.
    """
    n = len(arr)
    if n < 26:
        return None

    count = [0] * 27 # count[i] — сколько раз i в текущем окне
    have = 0  # сколько уникальных букв из 1..26 уже есть
    need = 26

    res = None
    l = 0

    # расширяем правый конец
    for r in range(n):
        x = arr[r]
        if 1 <= x <= 26:
            if count[x] == 0:
                have += 1
            count[x] += 1

        # когда окно охватывает все буквы, сжимаем его слева
        while have == need:
            length = r - l + 1
            res = length if res is None else min(res, length)

            # убираем arr[l] из окна
            y = arr[l]
            if 1 <= y <= 26:
                count[y] -= 1
                if count[y] == 0:
                    have -= 1
            l += 1

    return res  # либо число, либо None


# читаем из файла и сразу печатаем
filename = "data_prog_contest_problem_2.txt"  # поставь своё имя файла
with open(filename, 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

answer = min_alphabet_window(arr)
print(answer if answer is not None else "NONE")
