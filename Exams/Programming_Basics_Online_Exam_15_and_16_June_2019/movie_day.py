total_time = int(input())
scenes_count = int(input())
scene_duration = int(input())

shooting_time = scenes_count * scene_duration + 0.15 * total_time

diff = round(abs(total_time - shooting_time))
if shooting_time <= total_time:
    print(f"You managed to finish the movie on time! You have {diff} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {diff} minutes.")