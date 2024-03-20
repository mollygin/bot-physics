from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton

def build_films_keyboard(films: list):
    builder = InlineKeyboardBuilder()
    for index, film in enumerate(films):
        builder.button(text=film.get("title"),
                        callback_data=f"film_{index}")
    return builder.as_markup()

def build_film_details_keyboard(url):
    builder = InlineKeyboardBuilder()
    builder.button(text="Посилання на сайт: ", url=url)
    builder.button(text="Назад", callback_data="back")
    #builder.button(text="Сайт: ", url="https://brain-school.com.ua/category/formuly-fizyka/")
    return builder.as_markup()

def build_menu_keyboard(link_button):
    builder = KeyboardButton()
    link_button = KeyboardButton("Сайт з інформацією", url="https://brain-school.com.ua/category/formuly-fizyka/")
    builder.button(link_button)
    return builder.as_markup()
