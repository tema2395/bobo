from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from fsm import Menu
from aiogram.fsm.context import FSMContext
import keyboards
from pictures import *


rt2 = Router()


###обработчик кнопки калькулятора###
@rt2.callback_query(F.data == "calculate")
async def calc(callback: CallbackQuery, state: FSMContext):
    'Обработчик кнопки калькулятора'
    await callback.message.answer_media_group(media=calc_photo.build())
    await callback.message.answer(f"Введите стоимость товара в <b>ЮАНЯХ</b>")
    await callback.answer()
    await state.set_state(Menu.calc)


###обработчик кнопки возврата в главное меню###
@rt2.callback_query(F.data == "main_menu", Menu.end_calc)
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(
        start_photo,
        caption="Добро пожаловать в бота группы <b>bobolink</b>",
        reply_markup=keyboards.START_KEYS,
    )
    await state.set_state(Menu.start)


###обработчик кнопки повторить рассчет###
@rt2.callback_query(F.data == "repeat", Menu.end_calc)
async def calc(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_media_group(media=calc_photo.build())
    await callback.message.answer(f"Введите стоимость товара в <b>ЮАНЯХ</b>")
    await callback.answer()
    await state.set_state(Menu.calc)


###обработчик кнопки сделать заказ###
@rt2.callback_query(F.data == "make_order")
async def make_order(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_media_group(media = order_photo.build())
    await state.set_state(Menu.photo_id)
