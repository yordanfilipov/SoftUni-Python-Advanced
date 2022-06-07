from collections import deque

MAX_PIZZA_ORDERS = 10

pizza_orders = [int(el) for el in input().split(", ")]
employee_capacities = [int(el) for el in input().split(", ")]

pizza_orders = deque(pizza_orders)
total_pizzas_made = 0

while pizza_orders:
    if not employee_capacities:
        print("Not all orders are completed.")
        pizza_orders_print = [str(el) for el in pizza_orders]
        print(f"Orders left: {', '.join(pizza_orders_print)}")
        exit()
    current_order = pizza_orders[0]
    if current_order > MAX_PIZZA_ORDERS or current_order <= 0:
        pizza_orders.popleft()
        continue
    current_employee_capacity = employee_capacities[-1]
    if current_order <= current_employee_capacity:
        pizza_orders.popleft()
        employee_capacities.pop()
        total_pizzas_made += current_order
    if current_order > current_employee_capacity:
        employee_capacities.pop()
        pizza_orders[0] = current_order - current_employee_capacity
        total_pizzas_made += current_employee_capacity

print("All orders are successfully completed!")
print(f"Total pizzas made: {total_pizzas_made}")
print_emp = [str(el) for el in employee_capacities]
print(f"Employees: {', '.join(print_emp)}")