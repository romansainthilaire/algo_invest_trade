import csv
from pathlib import Path
from datetime import datetime
from itertools import combinations

CSV_FILE_NAME = "dataset_20.csv"
CSV_DELIMITER = ","
MAX_SPENDING = 500  # Maximum amount of money the client is willing to spend


def get_shares():
    """Gets all shares from the csv file.
       Each share is a dictionary with a name, a price, a profit rate (%) and a profit (euros).

    Returns:
        A list of shares.
    """
    shares = []
    with open(Path(__file__).parent / CSV_FILE_NAME, mode="r", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=CSV_DELIMITER)
        lines = list(csv_data)
        for line in lines:
            try:
                name = line[0]
                price = float(line[1])
                profit_rate = float(line[2])
                if 0 < price <= MAX_SPENDING and profit_rate > 0:
                    shares.append({
                        "name": name,
                        "price": price,
                        "profit_rate": profit_rate,
                        "profit": price * profit_rate / 100
                    })
            except ValueError:
                continue
    return shares


def get_combinations_of_shares(shares):
    """Gets all the possible combinations of shares.

    Arguments:
        shares -- list of shares

    Returns:
        A list of all possible combinations of shares.
    """
    combinations_of_shares = []
    for i in range(1, len(shares) + 1):
        for combination_of_shares in list(combinations(shares, i)):
            combinations_of_shares.append(list(combination_of_shares))
    return combinations_of_shares


def get_combinations_of_purchased_shares(combinations_of_shares):
    """Gets all the possible combinations of purchased shares.
       For each combination of shares, shares are purchased one by one until the client has no more money.

    Arguments:
        combinations_of_shares -- list of combinations of shares

    Returns:
        A list of combinations of purchased shares.
    """
    combinations_of_purchased_shares = []
    for combination_of_shares in combinations_of_shares:
        spending_left = MAX_SPENDING
        combination_of_purchased_shares = []
        while combination_of_shares != [] and spending_left > 0:
            share = combination_of_shares.pop(0)
            if spending_left >= share["price"]:
                combination_of_purchased_shares.append(share)
                spending_left -= share["price"]
            else:
                break
        combinations_of_purchased_shares.append(combination_of_purchased_shares)
    return combinations_of_purchased_shares


def get_strategies_sorted_by_total_profit(combinations_of_purchased_shares):
    """Gets all strategies sorted by total profit.
       A stragtegy is a combination of purchased shares with a total profit.

    Arguments:
        combinations_of_purchased_shares -- list of combinations of purchased shares

    Returns:
        A list of strategies sorted by total profit.
    """
    strategies = []
    for combination_of_purchased_shares in combinations_of_purchased_shares:
        strategy = dict()
        strategy["shares"] = []
        strategy["total_profit"] = 0
        for share in combination_of_purchased_shares:
            strategy["shares"].append(share)
            strategy["total_profit"] += share["profit"]
        strategies.append(strategy)
    return sorted(strategies, key=lambda strategy: -strategy["total_profit"])


if __name__ == "__main__":

    start = datetime.now()

    shares = get_shares()
    combinations_of_shares = get_combinations_of_shares(shares)
    combinations_of_purchased_shares = get_combinations_of_purchased_shares(combinations_of_shares)
    strategies_sorted_by_total_profit = get_strategies_sorted_by_total_profit(combinations_of_purchased_shares)
    best_strategy = strategies_sorted_by_total_profit[0]
    total_cost = 0
    for share in best_strategy["shares"]:
        print(f"{share['name']} : {share['price']:.2f} € x {share['profit_rate']:.2f} % = {share['profit']:.2f} €")
        total_cost += share["price"]
    print(f"\nTotal cost : {total_cost:.2f} €")
    print(f"Total profit : {best_strategy['total_profit']:.2f} €")

    end = datetime.now()

    print(f"\n{len(strategies_sorted_by_total_profit):,} combinations analized".replace(",", " "))
    print(f"{(end - start).total_seconds():.2f} seconds")
