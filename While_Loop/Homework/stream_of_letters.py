word = ""
result = ""
counter_c = False
counter_o = False
counter_n = False

while True:
    command = input()

    if counter_c and counter_n and counter_o:
        result += word + " "
        word = ""
        counter_c = False
        counter_o = False
        counter_n = False

    if command == "End":
        break

    command = ord(command)

    if 65 <= command <= 90 or 97 <= command <= 122:  # A - Z or a - z

        if command == 99:  # c
            if counter_c:
                word += chr(command)
            else:
                counter_c = True
        elif command == 111:  # o
            if counter_o:
                word += chr(command)
            else:
                counter_o = True
        elif command == 110:  # n
            if counter_n:
                word += chr(command)
            else:
                counter_n = True
        else:
            word += chr(command)

print(result)
