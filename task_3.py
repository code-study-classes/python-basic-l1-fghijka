prices = [1500, 6000, 4999, 12000, 800]
new_prices = [p * 0.8 if p > 5000 else p for p in prices]

print("Старые цены:", prices)
print("Новые цены:", new_prices)
