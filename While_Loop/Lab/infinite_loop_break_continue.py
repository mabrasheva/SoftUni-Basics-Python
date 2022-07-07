# print("Start of the loop")
# while True:
#     print("Before break")
#     break
#     print("After break")
# print('End of the loop')

print("Start of the loop")
number = 10
while True:
    print(f"Number = {number}")
    number += 1
    if number == 100:
        break
    else:
        continue
    print("After break")
print('End of the loop')
