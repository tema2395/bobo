from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from fsm import Menu, Order
from aiogram.fsm.context import FSMContext
import keyboards
from pictures import *


rt2 = Router()


@rt2.callback_query(F.data == "calculate")
async def calc(callback: CallbackQuery, state: FSMContext):
    "Calculator button handler"
    await callback.message.answer_media_group(media=calc_photo.build())
    await callback.message.answer(f"Введите стоимость товара в <b>ЮАНЯХ</b>")
    await callback.answer()
    await state.set_state(Menu.calc)


@rt2.callback_query(F.data == "main_menu", Menu.end_calc)
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    "Main menu return button handler"
    await callback.message.answer_photo(
        start_photo,
        caption="Добро пожаловать в бота группы <b>bobolink</b>",
        reply_markup=keyboards.START_KEYS,
    )
    await state.set_state(Menu.start)


@rt2.callback_query(F.data == "repeat", Menu.end_calc)
async def calc(callback: CallbackQuery, state: FSMContext):
    "Repeat calculation button handler"
    await callback.message.answer_media_group(media=calc_photo.build())
    await callback.message.answer(f"Введите стоимость товара в <b>ЮАНЯХ</b>")
    await callback.answer()
    await state.set_state(Menu.calc)


@rt2.callback_query(F.data == "make_order")
async def make_order(callback: CallbackQuery, state: FSMContext):
    "Make order button handler"
    await callback.message.answer_media_group(media=order_photo.build())
    await state.set_state(Order.fullname)


@rt2.callback_query(F.data == "accept")
async def accept(callback: CallbackQuery):
    "Accept button handler"
    await callback.message.answer(
        f"<b>Ваш заказ находится в обработке</b>\n\nДля оплаты заказа и уточнениня мелочей:\n\n@A4tonetak1"
    )
