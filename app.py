from menu import MENU,COIN_AMOUNT

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
    
}


def give_report():
    print(resources)

def check_if_have_enough(coffee_to_check):
    if coffee_to_check:
        dont_have_enough = []
        for ingredients in MENU[coffee_to_check]['ingredients']:
        
            if MENU[coffee_to_check]['ingredients'][ingredients] > resources[ingredients]:
                dont_have_enough.append(ingredients)
        if dont_have_enough == []:
                return True
        else:
            return dont_have_enough

while True: 
    what_user_wants = input('What would you like? (espresso/latte/cappuccino):')
    if what_user_wants == 'report':
        give_report()
    else:
        if check_if_have_enough(what_user_wants) == True:
            print('Please insert coins.')
            amount_in_quaters = int(input('How many quarters?:')) * COIN_AMOUNT['quater']
            amount_in_dimes = int(input('How many dimes?:')) * COIN_AMOUNT['dime']
            amount_in_nickles = int(input('How many nickles?:')) * COIN_AMOUNT['nickle']
            amount_in_pennies = int(input('How many pennies?:')) * COIN_AMOUNT['penny']
            full_amount_given = round(amount_in_quaters + amount_in_dimes + amount_in_nickles + amount_in_pennies,2)
            if MENU[what_user_wants]['cost'] > full_amount_given:
                print('Sorry you dont enough, your money was refunded.')
            else:
                resources['money'] += MENU[what_user_wants]['cost']
                for ingredients in MENU[what_user_wants]['ingredients']:
                    resources[ingredients] -= MENU[what_user_wants]['ingredients'][ingredients]
                print(f'Here is your change {round(full_amount_given - MENU[what_user_wants]['cost'],2)}')
                print(f'Thank you, here is your {what_user_wants} ')
                
        else:
            print(f'Sorry we dont have enough {' and '.join(check_if_have_enough(what_user_wants))}')
    




