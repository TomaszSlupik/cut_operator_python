# wydrukuj całą listę, pierwsze trzy elementy i ostatnie trzy elementy tej listy

original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_three = original_list[:3]
last_three = original_list[7:]
second_last_three = original_list[-3:]

print(f"Original list: {original_list}")
print(f"First three elements: {first_three}")
print(f"Last three elements: {last_three}")
print(f"Second choice: {second_last_three}")

print('---')

# wyodrębnić imię i nazwisko osoby ze stopniem 'Sergent'
personnel = [
    'John Smith, Private First Class',
    'Jane Doe, Captain',
    'Bob Johnson, Sergeant'
]

len_first_second_name = len('Bob Johnson')
print(personnel[2][:len_first_second_name])

print('---')

# obliczyć średnią cenę dla pierwszego i ostatniego tygodnia miesiąca.
# Pierwszy tydzień to pięć pierwszych elementów podanej listy.
# Ostatni tydzień to ostatnie pięć elementów podanej listy
stock_prices = [
    102.3,
    103.4,
    105.6,
    108.2,
    109.7,
    112.4,
    113.6,
    115.2,
    116.8,
    119.1,
    121.3,
    122.5,
    124.7,
    126.1,
    127.4,
    129.2,
    130.4,
    132.6,
    133.8,
    135.1,
    136.3,
]

first_week = stock_prices[:5]
avg_first_week = round(sum(first_week) / 5, 2)

last_week = stock_prices[-5:]
avg_last_week = round(sum(last_week) / 5, 2)

print(f"Average stock price for the first week: ${avg_first_week}")
print(f"Average stock price for the last week: ${avg_last_week}")

print('---')

# Wybrać length, width oraz height
dimensions = '10x5x2'
length = int(dimensions[:2])
width = int(dimensions[3])
height = int(dimensions[-1:])

print(f"length = {length}")
print(f"width = {width}")
print(f"height = {height}")

print('---')

# Wyciąć poniższe wymiary: ['55x22x1.8']
parts = [
    ['50x20x1.5', '25x10x1.0'],
    ['55x22x1.8', '30x15x1.2'],
    ['60x24x2.0', '35x20x1.5'],
]

my_dimensions = parts[1][0]
my_dimensions_length = round(float(my_dimensions[:2]), 2)
my_dimensions_width = round(float(my_dimensions[3:5]), 2)
my_dimensions_height = round(float(my_dimensions[-3:]), 2)


print(f"length = {my_dimensions_length}")
print(f"width = {my_dimensions_width}")
print(f"height = {my_dimensions_height}")
