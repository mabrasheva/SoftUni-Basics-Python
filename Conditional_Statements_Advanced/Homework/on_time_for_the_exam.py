exam_hour = int(input())  # 0 to 23
exam_minute = int(input())  # 0 to 59
arrival_hour = int(input())  # 0 to 23
arrival_minute = int(input())  # 0 to 59

exam = exam_hour * 60 + exam_minute
arrival = arrival_hour * 60 + arrival_minute
diff_time = abs(arrival - exam)
diff_hour = diff_time // 60
diff_minutes = diff_time % 60

if arrival <= exam and diff_time <= 30:
    print("On time")
elif arrival < exam and diff_time > 30:
    print("Early")
elif arrival > exam:
    print("Late")

if diff_time >= 1:
    if diff_time >= 60:
        if arrival < exam:
            if diff_minutes >= 10:
                print(f"{diff_hour}:{diff_minutes} hours before the start")
            else:
                print(f"{diff_hour}:0{diff_minutes} hours before the start")
        else:
            if diff_minutes >= 10:
                print(f"{diff_hour}:{diff_minutes} hours after the start")
            else:
                print(f"{diff_hour}:0{diff_minutes} hours after the start")
    else:
        if arrival < exam:
            print(f"{diff_time} minutes before the start")
        else:
            print(f"{diff_time} minutes after the start")