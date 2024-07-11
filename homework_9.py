from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider
from pywebio.output import put_success, put_error, put_warning, put_image, put_html
from pywebio.session import run_js
from pywebio import start_server



revierwers_info = []
movie_genres = ['Комедія', 'Драма', 'Екшн', 'Жахи', 'Наукова фантастика', 'Інший']
emotions = ['Захоплений', 'Розчарований', 'Вражений', 'Нейтральний']


def main():
    name = input_pw("Введіть ваше ім'я:")
    movie = input_pw("Введіть назву фільму:")
    movie_genre = select("Виберіть жанр", options=movie_genres)
    review_movie = input_pw("Введіть короткий відгук про цей фільм:")
    review_scale = slider("Рейтинг фільму від 1 до 10", min_value=1, max_value=10)
    movie_emotions = select("Виберіть свої емоції після просмотру цього фільма", options=emotions)
    movie_reccomendation = radio("Чи рекомундуєте ви цей фільм іншим людям",options=[True, False])
    if review_scale >= 8:
        put_success("Радий ,що вам подобається цей фільм")
    revierwers_info.append([name, movie, movie_genre, review_movie, review_scale, movie_emotions, movie_reccomendation])
    run_js('setTimeout(function(){location.reload();}, 4000)')
    return

if __name__ == '__main__':
    start_server(main, port=14000)



