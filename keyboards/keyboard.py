from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_rm_kb = KeyboardButton('Убрать клавиатуру')
button_menu = KeyboardButton("Меню")
button_make_order = KeyboardButton("Сделать заказ")
button_feedback = KeyboardButton("Оставить отзыв")
button_contacts = KeyboardButton("Телефоны для справки")

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.row(button_menu, button_make_order).row(button_feedback, button_contacts)

cancel_button = KeyboardButton("Отменить заказ")

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(cancel_button)