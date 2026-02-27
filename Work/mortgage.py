# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

for i in range(12):
    principal = principal * (1 + rate / 12) - payment - 1000
    total_paid = total_paid + payment + 1000

months = months + 12

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    months = months + 1

print('Total paid', round(total_paid, 2))
print('Months', months)

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    months = months + 1
    if principal > payment:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    else:
        total_paid = total_paid + principal
        principal = 0

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    print(f'{months} {round(total_paid, 2):0.0f} {round(principal, 2):0.0f}')

print('Total paid with extra payments', round(total_paid, 2))
print('Months with extra payments', months)