company = input()
adult_ticket_count = int(input())
kid_ticket_count = int(input())
adult_ticket_price = float(input())
tax = float(input())

kid_ticket_price = 0.3 * adult_ticket_price
total_price_tickets = adult_ticket_count * (adult_ticket_price + tax) + kid_ticket_count * (kid_ticket_price + tax)
profit = 0.20 * total_price_tickets

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")
