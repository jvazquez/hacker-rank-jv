import statistics


class OperatorMachine:
    def buy(self, share_price, balance_point):
        return share_price < round(balance_point)

    def sell(self, share_price, balance_point):
        return share_price > round(balance_point)


def maximumProfit(price):
    if len(price) == 0:
        return 0

    operator = OperatorMachine()
    balance_point = sum(price) / len(price)
    shares = 0
    income = 0
    outcome = 0

    def is_not_last_element(share_price):
        return price.index(share_price) == len(price) - 1

    for share_price in price:
        should_sell = operator.sell(share_price, balance_point)
        should_buy = operator.buy(share_price, balance_point)
        is_last_operation = is_not_last_element(share_price) is False
        if should_sell and shares > 0:
            income = shares * share_price
            shares = 0
        elif should_buy and is_last_operation:
            outcome = outcome + share_price * -1
            shares += 1
    return income + outcome


if __name__ == "__main__":
    case_one = maximumProfit([5, 3, 2])
    assert case_one == 0
    case_two = maximumProfit([1, 2, 100])
    assert case_two == 197
    case_three = maximumProfit([6, 5, 4, 5, 3])
    print("Case three", case_three)
    assert case_three == 1
