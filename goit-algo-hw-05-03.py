import timeit
from typing import Callable
import regex
import pyahocorasick

# визначення алгоритму Боєра-Мура
def boyer_moore(text: str, pattern: str) -> int:
    match = regex.search(pattern, text)
    return match.start() if match else -1

# визначення алгоритму Ахо-Корасіка (схожий на Кнута-Морріса-Пратта)
def aho_corasick(text: str, pattern: str) -> int:
    automaton = pyahocorasick.Automaton()
    automaton.add_word(pattern, pattern)
    automaton.make_automaton()
    for end_index, _ in automaton.iter(text):
        return end_index - len(pattern) + 1
    return -1

# визначення алгоритму Рабіна-Карпа
def rabin_karp(text: str, pattern: str) -> int:
    pattern_sum = sum(ord(c) for c in pattern)
    text_sum = sum(ord(text[i]) for i in range(len(pattern)))
    for i in range(len(pattern), len(text)):
        if pattern_sum == text_sum and text[i-len(pattern):i] == pattern:
            return i - len(pattern)
        text_sum = text_sum - ord(text[i-len(pattern)]) + ord(text[i])
    return -1

# визначення функції для вимірювання часу виконання алгоритму
def measure_time(func: Callable, text: str, pattern: str) -> float:
    start_time = timeit.default_timer()
    func(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time

# відкриття текстових файлів
with open('стаття 1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

with open('стаття 2.txt', 'r', encoding='utf-8') as file:
    text2 = file.read()

# вимірювання часу виконання алгоритмів
pattern1 = 'існуючий підрядок'
pattern2 = 'вигаданий підрядок'
algorithms = [boyer_moore, aho_corasick, rabin_karp]

for algorithm in algorithms:
    for text in [text1, text2]:
        for pattern in [pattern1, pattern2]:
            time = measure_time(algorithm, text, pattern)
            print(f'Час виконання {algorithm.__name__} для підрядка "{pattern}" в тексті: {time} секунд')