destination = input()
suma = 0

while destination != "End":
    min_budget = float(input())
    # if min_budget == "End":
    #     break
    # if min_budget < 0:
    #     break

    while suma < min_budget:
        spesteni = float(input())
        if spesteni == "End":
            break
        suma = spesteni + suma

        if suma >= min_budget:
            print(f"Going to {destination}!")
            destination = input()
            suma = 0
            break