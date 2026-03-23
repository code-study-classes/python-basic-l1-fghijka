curriculum = []

for week in range(1, 17):
    if week % 4 == 0:
        curriculum.append("Контроль")
    else:
        curriculum.append(4)

print("Учебный план на семестр:")
print(curriculum)
