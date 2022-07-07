input_number = int(input())

for thousands in range(1, 10):
    for hundreds in range(1, 10):
        for tens in range(1, 10):
            for ones in range(1, 10):
                if input_number % thousands == 0 and input_number % hundreds == 0 and \
                        input_number % tens == 0 and input_number % ones == 0:
                    print(f"{thousands}{hundreds}{tens}{ones} ", end="")
