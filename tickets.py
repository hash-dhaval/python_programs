adult_ticket_cost = 5
children_ticket_cost = 2
senior_ticket_cost = 3
total_sales = y

x= total_sales / (7*x + 12)
y = total_sales / (10*y + 12)

children_tickets_sold = round(x)
adult_tickets_sold = round(x + X)
senior_tickets_sold = round(2*x)

print("Number of children tickets sold:", children_tickets_sold)
print("Number of adult tickets sold:", adult_tickets_sold)
print("Number of senior tickets sold:", senior_tickets_sold)
