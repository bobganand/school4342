from pywebio.input import input as input_pw
from pywebio.output import put_text, put_html, put_image

put_html('<h1>УРА, ЛІТО</h1>')

poem = """
Вже йде літо -
Море, сонце, вітер, -
Я радий! 😎
"""

put_text(poem)

plans_for_summer = input_pw("Введіть свої плани на літо")
formatted_plans_for_summer = f'{plans_for_summer}'
put_text(formatted_plans_for_summer)

img = open('wave-homework.jpg', 'rb').read()
put_image(img, width='500px')
