import csv
from pathlib import Path
from datetime import datetime

CSV_FILE_NAME = "dataset1_Python+P7.csv"
CSV_DELIMITER = ";"
MAX_SPENDING = 500  # Maximum amount of money the client is willing to spend


def get_shares_sorted_by_profit_rate():
    """Gets all shares from the csv file and sorts them by profit rate.
       Each share is a dictionary with a name, a price, a profit rate (%) and a profit (euros).

    Returns:
        A list of shares sorted by profit rate.
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
    return sorted(shares, key=lambda share: -share["profit_rate"])


def get_purchased_shares(shares):
    """Gets the purchased shares.
       Shares are purchased one by one until the client has no more money.

    Arguments:
        shares -- list of shares

    Returns:
        A list of purchased shares.
    """
    spending_left = MAX_SPENDING
    purchased_shares = []
    while shares != [] and spending_left > 0:
        share = shares.pop(0)
        if spending_left >= share["price"]:
            purchased_shares.append(share)
            spending_left -= share["price"]
    return purchased_shares


if __name__ == "__main__":

    start = datetime.now()

    shares = get_shares_sorted_by_profit_rate()
    purchased_shares = get_purchased_shares(shares)
    total_cost = 0
    total_profit = 0
    for share in purchased_shares:
        total_cost += share["price"]
        total_profit += share["profit"]
        print(f"{share['name']} : {share['price']:.2f} € x {share['profit_rate']:.2f} % = {share['profit']:.2f} €")
    print(f"\nTotal cost : {total_cost:.2f} €")
    print(f"Total profit : {total_profit:.2f} €")

    end = datetime.now()

    print(f"\n{(end - start).total_seconds():.3f} seconds")
