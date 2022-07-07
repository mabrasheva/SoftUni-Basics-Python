detergent_bottles = int(input())
detergent_total = detergent_bottles * 750
detergent_used = 0
counter = 0
dishes = 0
pots = 0

while detergent_total >= 0:
    command = input()

    if command == "End":
        break
    else:
        command = int(command)
        counter += 1
        if counter % 3 == 0:
            detergent_used = command * 15
            pots += command
        else:
            detergent_used = command * 5
            dishes += command
        detergent_total -= detergent_used

if detergent_total >= 0:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent_total} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_total)} ml. more necessary!")
