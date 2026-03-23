import random
import statistics

n = random.randint(7, 10)
scores = [random.randint(1, 100) for _ in range(n)]

print(f"Исходные баллы: {scores}")

min_score = min(scores)
max_score = max(scores)
print(f"Удаляем минимум ({min_score}) и максимум ({max_score}).")

remaining = scores.copy()
remaining.remove(min_score)
remaining.remove(max_score)

print(f"Оставшиеся баллы: {remaining}")

if remaining:
    avg = statistics.mean(remaining)
    print(f"Средний рейтинг: {round(avg, 1)}")
else:
    print("После удаления экстремумов не осталось оценок для расчёта среднего.")
