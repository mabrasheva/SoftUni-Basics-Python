one_lv_count = int(input())
two_lv_count = int(input())
five_lv_count = int(input())
total = int(input())

for one in range(one_lv_count + 1):
    for two in range(two_lv_count + 1):
        for five in range(five_lv_count + 1):
            if (one * 1) + (two * 2) + (five * 5) == total:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {total} lv.")
