n_number = int(input())
l_number = int(input())

# Символ 1: цифра от 1 до n.
# Символ 2: цифра от 1 до n.
# Символ 3: малка буква измежду първите l букви на латинската азбука.
# Символ 4: малка буква измежду първите l букви на латинската азбука.
# Символ 5: цифра от 1 до n, по-голяма от първите 2 цифри.

for symbol_one in range(1, n_number):

    for symbol_two in range(1, n_number):

        counter_symbol_three = 0
        for symbol_three in range(97, 122):
            counter_symbol_three += 1
            if counter_symbol_three <= l_number:

                counter_symbol_four = 0
                for symbol_four in range(97, 122):
                    counter_symbol_four += 1
                    if counter_symbol_four <= l_number:

                        for symbol_five in range(1, n_number + 1):
                            if symbol_five > symbol_one and symbol_five > symbol_two:
                                print(f"{symbol_one}{symbol_two}{chr(symbol_three)}{chr(symbol_four)}{symbol_five} ",
                                      end="")
