cargo_count = int(input())

total_weight = 0
total_price = 0
cargos_by_bus = 0
cargos_by_trunk = 0
cargos_by_train = 0

for number in range(cargo_count):
    weight = int(input())
    if weight <= 3:
        total_weight += weight
        total_price += weight * 200
        cargos_by_bus += weight
    elif 4 <= weight <= 11:
        total_weight += weight
        total_price += weight * 175
        cargos_by_trunk += weight
    else:
        total_weight += weight
        total_price += weight * 120
        cargos_by_train += weight

average_price_per_ton = total_price / total_weight
percent_cargos_by_bus = (cargos_by_bus / total_weight) * 100
percent_cargos_by_trunk = (cargos_by_trunk / total_weight) * 100
percent_cargos_by_train = (cargos_by_train / total_weight) * 100

print(f"{average_price_per_ton:.2f}")
print(f"{percent_cargos_by_bus:.2f}%")
print(f"{percent_cargos_by_trunk:.2f}%")
print(f"{percent_cargos_by_train:.2f}%")
