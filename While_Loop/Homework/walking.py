goal = 10000
steps = "0"
total_steps = 0
goal_is_reached = True

while total_steps < goal:
    steps = input()
    if steps != "Going home":
        total_steps += int(steps)
    else:
        steps = input()
        total_steps += int(steps)
        if total_steps < goal:
            goal_is_reached = False
        break
diff_steps = abs(goal - total_steps)
if goal_is_reached:
    print(f"Goal reached! Good job!\n{diff_steps} steps over the goal!")
else:
    print(f"{diff_steps} more steps to reach goal.")
