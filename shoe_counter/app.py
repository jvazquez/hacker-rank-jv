# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter, deque


def can_purchase(shoe: int, stock: Counter) -> bool:
    purchase_done = False
    if stock[shoe] > 0:
        stock[shoe] -= 1
        purchase_done = True

    return purchase_done


if __name__ == "__main__":
    total_shoes = input()
    shoe_list = deque(map(int, input().split(" ")))
    total_stock = Counter(shoe_list)
    total_customers = int(input())
    customer_list = list()
    for _ in range(total_customers):
        shoe_size, shoe_price = map(int, input().split(" "))
        if can_purchase(shoe_size, total_stock):
            customer_list.append(shoe_price)

    print(sum(customer_list))