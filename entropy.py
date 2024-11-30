from decimal import Decimal, getcontext, ROUND_CEILING
from collections import Counter

getcontext().prec = 100

input_string = "остапчукалександрдмитриевич"

total_count = len(input_string)
frequencies = Counter(input_string)
probabilities = {char: Decimal(freq) / Decimal(total_count) for char, freq in frequencies.items()}
sorted_probabilities = dict(sorted(probabilities.items(), key=lambda x: x[1], reverse=True))
print("Таблица вероятностей:")
summ = Decimal(0)
for symbol, prob in sorted_probabilities.items():
    print(f"{symbol}: {float(prob):.6f}")
    summ += prob * (prob.ln() / Decimal(2).ln())
summ = -summ

print("Энтропия:", summ)
