from datetime import datetime



def get_days_from_today(date):
    current_date = datetime.today()
    try:
        difference_in_days = datetime.strptime(date, "%Y-%m-%d") - current_date
    except ValueError:
        difference_in_days = datetime.strptime(date, "%Y.%m.%d") - current_date
    return difference_in_days.days

print(get_days_from_today("2021.10.09"))



from random import randint

min_value = 1
max_value = 1000

def get_numbers_ticket(min, max, quantity):
    ticket_numbers = set()
    if min < min_value:
        print(f"Мінімальне значення не повинно бути менше 1")
    elif max > max_value:
        print(f"Максимальне значення не повинно бути більше 1000")
    elif min_value > quantity:
        print(f"Кількість не повинна бути менше 1")
    elif max_value < quantity:
        print(f"Кількість не повинна бути більша 1000")
    else:
        while len(ticket_numbers) != quantity:
            ticket_numbers.add(randint(min, max))
    return sorted(set(ticket_numbers))

print("Ваші лотерейні числа:", get_numbers_ticket(1,100,6))


import re


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    sanitized_numbers = []
    for phone in raw_numbers:
        cleaned_number = re.sub(r"\D", "", phone)
        if not cleaned_number.startswith("+"):
            if cleaned_number.startswith("380"):
                cleaned_number = "+" + cleaned_number
            else:
                cleaned_number = "+38" + cleaned_number
        sanitized_numbers.append(cleaned_number)
    return sanitized_numbers

print(normalize_phone(raw_numbers))


