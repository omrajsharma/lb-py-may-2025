def apply_discount(price, percentage):
    return price - (price * percentage / 100)

def new_user(price):
    return price - (price * 30 / 100)

def card_discount(price, cardCompany):
    if cardCompany == "HDFC":
        return price - (price * 15 / 100)
    elif cardCompany == "ICICI":
        return price - (price * 20 / 100)
    else:
        return price - (price * 5 / 100)
