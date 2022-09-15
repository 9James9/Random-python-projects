import pyinputplus as pyip
print('Please select a type of bread')
sandwich = []
totalPrice = 0
bread = pyip.inputMenu(['White','Wheat','Sourdough'])
sandwich.append(bread)
protein = pyip.inputMenu(['chicken','turkey','ham','tofu'])
sandwich.append(protein)
cheese = pyip.inputYesNo('Do you want cheese?\n')
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar','swiss','mozzarella'])
    sandwich.append(cheeseType)
else:
    cheeseType = 'None'
mayo = pyip.inputYesNo('Do you want Mayo?')
if mayo:
    sandwich.append('Mayo')
mustard = pyip.inputYesNo('Do you want Mustard?')
if mustard:
    sandwich.append('mustard')
lettuce = pyip.inputYesNo('Do you want lettuce?')
if lettuce:
    sandwich.append('lettuce')
tomato = pyip.inputYesNo('Do you want tomato')
if tomato:
    sandwich.append('tomato')
quantity = pyip.inputInt('How many sandwiches do you want?')
print(f'Your sandwich is {sandwich}')

prices = {
    'white': 2,
    'wheat': 3,
    'sourdough':5,
    'chicken': 3,
    'turkey':2,
    'ham':3,
    'tofu': 7,
    'cheddar': 1,
    'swiss': 1,
    'mozzarella': 2,
    'mayo': 0.5,
    'mustard': 0.5,
    'lettuce': 0.3,
    'tomato': 0.69,
}
for item in sandwich:
    price = prices.get(item.lower())
    totalPrice += price
print('Your sandwich has:\n')
for ingr in sandwich:
    print(ingr)
print(f'Your total price is: {totalPrice * quantity}')