from aiogram import types


"""Кнопки на приветсвенном сообщении"""
buttons_start = [
    [
        types.InlineKeyboardButton(
            text="Основной канал", url="https://t.me/bobolinktransfers"
        )
    ],
    [
        types.InlineKeyboardButton(
            text="Канал с отзывами", url="https://t.me/bobolinktraswersreviews"
        )
    ],
    [
        types.InlineKeyboardButton(
            text="Калькулятор стоимости💸", callback_data="calculate"
        )
    ],
    [types.InlineKeyboardButton(text="Оформить заказ🚚", callback_data="make_order")],
]


"""Кнопки в сообщении после рассчета стоимости"""
buttons_calc = [
    [types.InlineKeyboardButton(text="🔁Повторить расчет", callback_data="repeat")],
    [
        types.InlineKeyboardButton(
            text="⏪Вернуться в главное меню", callback_data="main_menu"
        )
    ],
]


###Кнопки после полного вывода заказа
buttons_order = [
    [types.InlineKeyboardButton(text="Да, все верно✅", callback_data='accept')],
    [types.InlineKeyboardButton(text="Изменить✏️", callback_data='make_order')],
]


START_KEYS = types.InlineKeyboardMarkup(inline_keyboard=buttons_start)
CALC_KEYS = types.InlineKeyboardMarkup(inline_keyboard=buttons_calc)
ORDER_KEYS = types.InlineKeyboardMarkup(inline_keyboard=buttons_order)

                                        