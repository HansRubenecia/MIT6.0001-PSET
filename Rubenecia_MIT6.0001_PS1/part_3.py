annual_salary = float(input("Enter your starting salary: "))
total_cost = float(1000000)
semi_annual_raise = float(.07)
r = 0.04
portion_down_payment = 0.25 * total_cost
current_savings = 0
final_months = 36
current_months = 0
monthly_salary = annual_salary/12

while current_months < final_months:
    if current_months % 6 == 0 and current_months != 0:
        monthly_salary += monthly_salary * semi_annual_raise
    current_savings += (current_savings*r/12)+monthly_salary
    current_months += 1
portion_saved = 0
epsilon = 100
steps = 1
low = 0
high = 10000
mid = (high+low)//2
while abs((mid/10000*current_savings) - portion_down_payment) >= epsilon:

    if ((mid/10000)*current_savings) > portion_down_payment:
        high = mid
    else:
        low = mid
    mid = (high+low)//2
    portion_saved = mid / 10000
    steps += 1

if portion_saved*current_savings < portion_down_payment:
    print("It is not possible to pay the down payment in three years")
else:
    print("best saving rate: " + str(portion_saved))
    print("Steps in bisection search: " + str(steps))