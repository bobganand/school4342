def greetings(username):
    return f'<h1>Вітаємо тебе, шановний {username}</h1>'


username = "Bogdan"
html_header = greetings(username)
print(html_header)


def calculate_rectangle_area(length, width):
    result = length * width
    return result


lenght = 40
width = 20
area = calculate_rectangle_area(lenght, width)
print(f"Площа прямокутника: {area}")
