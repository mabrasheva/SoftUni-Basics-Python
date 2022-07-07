stage_championship = input()  # “Quarter final”, “Semi final” or “Final”
ticket_type = input()  # “Standard”, “Premium” or “VIP”
ticket_count = int(input())
picture = input()  # 'Y'or 'N'
ticket_price = 0

if ticket_type == "Standard":
    if stage_championship == "Quarter final":
        ticket_price = 55.50
    elif stage_championship == "Semi final":
        ticket_price = 75.88
    elif stage_championship == "Final":
        ticket_price = 110.10

elif ticket_type == "Premium":
    if stage_championship == "Quarter final":
        ticket_price = 105.20
    elif stage_championship == "Semi final":
        ticket_price = 125.22
    elif stage_championship == "Final":
        ticket_price = 160.66

if ticket_type == "VIP":
    if stage_championship == "Quarter final":
        ticket_price = 118.90
    elif stage_championship == "Semi final":
        ticket_price = 300.40
    elif stage_championship == "Final":
        ticket_price = 400

total_sum_tickets = ticket_count * ticket_price

if total_sum_tickets > 4000:
    total_sum = 0.75 * total_sum_tickets
elif total_sum_tickets > 2500:
    total_sum = 0.90 * total_sum_tickets
else:
    total_sum = total_sum_tickets

if picture == "Y" and total_sum_tickets <= 4000:
    total_sum += ticket_count * 40

print(f"{total_sum:.2f}")
