from decimal import Decimal, getcontext, ROUND_CEILING
from collections import Counter

getcontext().prec = 100

input_string = "остапчукалександрдмитриевич"

total_count = len(input_string)
frequencies = Counter(input_string)
probabilities = {char: Decimal(freq) / Decimal(total_count) for char, freq in frequencies.items()}
sorted_probabilities = dict(sorted(probabilities.items(), key=lambda x: x[1], reverse=True))

intervals = {}
low = Decimal(0)
for symbol, prob in sorted_probabilities.items():
    high = low + prob
    intervals[symbol] = (low, high)
    low = high

print("Таблица интервалов:")
for symbol, (low, high) in intervals.items():
    print(f"{symbol}: [{float(low):.6f}, {float(high):.6f})")

print("")
print("Кодирование:")
low, high = Decimal(0), Decimal(1)
print(f"  : [{low}, {high})")
for symbol in input_string:
    symbol_low, symbol_high = intervals[symbol]
    range_width = high - low
    high = low + range_width * Decimal(symbol_high)
    low = low + range_width * Decimal(symbol_low)
    print(f"{symbol} : [{low}, {high})")

print("")
k = (-(high - low).ln() / Decimal(2).ln()).quantize(Decimal('1'), rounding=ROUND_CEILING)
k_int = int(str(k).split('.')[0])
ch = 2 ** k_int
left, right = 0, ch - 1
while (right - left > 1):
    middle = (right + left) // 2
    if Decimal(middle) / Decimal(ch) < low:
        left = middle
    else:
        right = middle

if Decimal(right) / Decimal(ch) >= low and Decimal(right) / Decimal(ch) < high:
    ii = int(str(left).split('.')[0])
    ib = bin(ii)[2:].zfill(k_int)
    print("Закодированная:", ib)
else:
    print("Ошибка")
