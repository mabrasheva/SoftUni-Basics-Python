total_sum = int(input())
current_sum = 0
counter_all_payments = 0
sum_cs_payments = 0
counter_cs_payments = 0
sum_cc_payments = 0
counter_cc_payments = 0

while current_sum < total_sum:
    command = input()
    if command == "End":
        break
    else:
        command = int(command)

        counter_all_payments += 1

        if counter_all_payments % 2 == 1:
            payment_method = "cash"
        else:
            payment_method = "card"

        if command > 100:
            payment_method = "card"
        elif command < 10:
            payment_method = "cash"

        if counter_all_payments % 2 == 1:
            if payment_method == "cash":
                print("Product sold!")
                current_sum += command
                sum_cs_payments += command
                counter_cs_payments += 1
            else:
                print("Error in transaction!")
        else:
            if payment_method == "card":
                print("Product sold!")
                current_sum += command
                sum_cc_payments += command
                counter_cc_payments += 1
            else:
                print("Error in transaction!")

if current_sum >= total_sum:
    print(f"Average CS: {sum_cs_payments / counter_cs_payments:.2f}")
    print(f"Average CC: {sum_cc_payments / counter_cc_payments:.2f}")
else:
    print("Failed to collect required money for charity.")
