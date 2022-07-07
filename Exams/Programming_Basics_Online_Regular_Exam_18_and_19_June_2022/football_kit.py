shirt = float(input())
needed_sum_for_ball = float(input())
the_ball_is_won = False

shorts = 0.75 * shirt
socks = 0.20 * shorts
shoes = 2 * (shirt + shorts)

total_sum = 0.85 * (shirt + shorts + socks + shoes)

if total_sum >= needed_sum_for_ball:
    the_ball_is_won = True

if the_ball_is_won:
    print(f"""Yes, he will earn the world-cup replica ball!
His sum is {total_sum:.2f} lv.
""")
else:
    diff = needed_sum_for_ball - total_sum
    print(f"""No, he will not earn the world-cup replica ball.
He needs {diff:.2f} lv. more.
""")
