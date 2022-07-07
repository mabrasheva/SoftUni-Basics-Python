from math import floor

change_lv = float(input())
coins_count = 0
change_st = floor(change_lv * 100)

while change_st > 0:
    if change_st >= 200:
        change_st -= 200
        coins_count += 1
    elif 200 > change_st >= 100:
        change_st -= 100
        coins_count += 1
    elif 100 > change_st >= 50:
        change_st -= 50
        coins_count += 1
    elif 50 > change_st >= 20:
        change_st -= 20
        coins_count += 1
    elif 20 > change_st >= 10:
        change_st -= 10
        coins_count += 1
    elif 10 > change_st >= 5:
        change_st -= 5
        coins_count += 1
    elif 5 > change_st >= 2:
        change_st -= 2
        coins_count += 1
    elif 2 > change_st >= 1:
        change_st -= 1
        coins_count += 1

print(coins_count)