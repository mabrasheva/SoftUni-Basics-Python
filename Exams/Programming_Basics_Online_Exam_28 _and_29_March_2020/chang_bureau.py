count_bitcoin = int(input())
count_chinese = float(input())
tax = float(input())

bitcoin_to_lv = count_bitcoin * 1168
chinese_to_usd = count_chinese * 0.15
chinese_to_lv = chinese_to_usd * 1.76

total_euro = (bitcoin_to_lv + chinese_to_lv) / 1.95
total = total_euro - (tax / 100 * total_euro)

print(f"{total:.2f}")
