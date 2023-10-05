# Task One
# Make a template using the dictionary data.
# Your Template must have at least two sentences.
# USD must be converted to BDT
# example Output: Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT

mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }



phones = mobile_data.get('data')

for phone in phones:
    name = phone.get('name')
    price = float(phone.get('price').replace('USD', '')) * 107.25
    country = phone.get('made')
    template = f"The {name} is made in {country}. The price is {price} USD, which is almost equal to BDT {price}."
    print(template)

