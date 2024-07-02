from pywebio.input import input as input_pw
from pywebio.input import NUMBER, FLOAT
from pywebio.output import put_text, put_html, put_image
from pywebio import start_server
from pywebio.session import run_js


def main():
    user_name = input_pw("Введіть ваше ім'я")
    total_score = 0
    question_1 = input_pw("Яка столиця України?")
    question_2 = input_pw("Скільки місяців у році?", type=NUMBER)
    question_3 = input_pw("Коли відбувся вибух на Чорнобильській АЕС?",type=NUMBER)
    question_4 = input_pw("Яка сама небезпечна медуза в Oдесі?")
    question_5 = input_pw("яка столиця Східної Римської імперії?")
    if question_1 == "Київ":
        total_score += 1
    if question_2 == 12:
        total_score += 1
    if question_3 == 1986:
        total_score += 1
    if question_4 == "корнерот":
        total_score += 1
    if question_5 == "константинополь":
        total_score += 1
    put_text(f"{user_name}, ваш результат: {total_score}/5")
    if total_score == 5:
        img = open('five_stars.jpeg','rb').read()
        put_image(img,width='500px')
    run_js('setTimeout(function(){location.reload();}, 6000)')
if __name__ == '__main__':
     start_server(main, port=11000)






