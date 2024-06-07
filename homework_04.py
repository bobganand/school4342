head = '~' * 50
print(head)

MSG_INPUT_FOOD_RECIPE = 'Введіть рецепт вашої улюбленої страви🥐'
food = input('**********Введіть вашу улюблену страву**********: ').upper().strip()
food_recipe = input(MSG_INPUT_FOOD_RECIPE).lower().strip()

print(food)

result = f'{food} {food_recipe}'.count('мясо')
print(result)

head = '~' * 50
print(head)
