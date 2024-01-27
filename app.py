from menu import MENU,COIN_AMOUNT

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def give_report():
    print(resources)

def check_if_have_enough(coffee_to_check):
    dont_have_enough = []
    for ingredients in MENU[coffee_to_check]['ingredients']:
      
       if MENU[coffee_to_check]['ingredients'][ingredients] > resources[ingredients]:
          dont_have_enough.append(ingredients)
    if dont_have_enough == []:
        return True
    else:
        return dont_have_enough

while True: 
    what_user_wants = input('What would you like? (e)')
    




