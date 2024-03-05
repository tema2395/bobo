from aiogram import Router, F
from aiogram.types import Message, URLInputFile
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from fsm import Menu, Order
import keyboards
from pictures import *
from db_function import add_user_to_db, get_user_data

rt1 = Router()


@rt1.message(F.text, Command("start"))
async def start(message: Message, state: FSMContext) -> None:
    'Greetings'
    await message.answer_photo(
        start_photo,
        caption="Добро пожаловать в бота группы <b>bobolink</b>",
        reply_markup=keyboards.START_KEYS,
    )
    await state.set_state(Menu.start)


@rt1.message(Menu.calc)
async def calc(message: Message, state: FSMContext):
    'Price calculation'
    await message.answer(
        f"💰Стоимость товара - {(str(int(message.text)*13.5 + 400))} руб(<b>без учета доставки</b>).\n\n❗<i>Доставка зависит от веса товара, поэтому она оплачивается отдельно</i>",
        reply_markup=keyboards.CALC_KEYS,
    )
    await state.set_state(Menu.end_calc)

    
@rt1.message(Order.fullname)
async def fullname(message: Message, state: FSMContext):
    'Registration'
    await message.answer(f"Введите ваше ФИО<b>(как в паспорте):</b> и имя пользователя Telegram\n\n<i>Это нужно для получения товара</i>\n\n<b>Пример</b>\n<i>Иванов Иван Иванович @1234</i>")
    await state.set_state(Order.link)


@rt1.message(Order.link)
async def link(message: Message, state: FSMContext):
    'Product link'
    await message.answer(f"Отправьте ссылку на ваш товар")
    await state.update_data(fullname = message.text)
    await state.set_state(Order.address)


@rt1.message(Order.address)
async def address(message: Message, state: FSMContext):
    'Clients address'
    await message.answer(
        f"🚚Введите адрес доставки <b>близлежащего</b> СДЕКА🚚\nНапример:\n<i>г.Москва, Можайский переулок 3</i>"
    )
    await state.update_data(link = message.text)
    await state.set_state(Order.size)


@rt1.message(Order.size)
async def item_size(message: Message, state: FSMContext):
    'Product size'
    await message.answer(
        f"Напишите ваш размер выбранного товара\n<i>Если это одежда, то размер указывать в формате: S,M,L,XL...\nЕсли это обувь, то в формате: 42.5,43,44,38....</i>"
    )
    await state.update_data(address = message.text)
    await state.set_state(Order.price)
    

@rt1.message(Order.price)
async def price(message: Message, state: FSMContext):
    'Product price'
    await message.answer(f"Напишите цену вашего товара в юанях")
    await state.update_data(size = message.text)
    await state.set_state(Order.end_order)
    

@rt1.message(Order.end_order)
async def add_process(message: Message, state: FSMContext):
    'Adding to the database'
    await state.update_data(price = message.text)
    
    data = await state.get_data()
    fullname = data.get('fullname')
    link = data.get('link')
    address = data.get('address')
    size = data.get('size')
    price = data.get('price')
    
    await add_user_to_db(message.from_user.id, fullname, link, address, size, price)
    await state.clear()
    
    user_data = await get_user_data(message.from_user.id)
    if user_data:
        user_order = f"Ваше ФИО: {user_data['fullname']}\nСсылка на ваш товар: {user_data['link']}\nАдрес доставки: {user_data['address']}\nРазмер вашего товара: {user_data['size']}\nЦена товара: {(user_data['price']*13.5+400)}<i> рублей</i>\n\n<b>Внимательно проверяйте введенные вами данные!!</b>"
        await message.answer(user_order, reply_markup=keyboards.ORDER_KEYS)
        await message.bot.send_message(chat_id=750523220, text = user_order)