import requests


def get_exchange_rate(base: str, target: str) -> float:
    url = f"https://open.er-api.com/v6/latest/{base.upper()}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if target.upper() not in data["rates"]:
        raise ValueError(f"Currency '{target}' not found.")
    return data["rates"][target.upper()]


def convert_currency(amount: float, base: str, target: str) -> float:
    rate = get_exchange_rate(base, target)
    return round(amount * rate, 2)


if __name__ == "__main__":
    base = input("From currency (e.g., USD): ").upper()
    target = input("To currency (e.g., EUR): ").upper()
    amount = float(input("Amount to convert: "))
    result = convert_currency(amount, base, target)
    print(f"{amount} {base} = {result} {target}")
