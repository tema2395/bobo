from aiogram import Router, F
from aiogram.types import Message, URLInputFile
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from fsm import Menu
import keyboards
from pictures import *
from db_function import add_user_to_db, get_user_data
import io

rt1 = Router()


###приветствие###
@rt1.message(F.text, Command("start"))
async def start(message: Message, state: FSMContext) -> None:
    await message.answer_photo(
        start_photo,
        caption="Добро пожаловать в бота группы <b>bobolink</b>",
        reply_markup=keyboards.START_KEYS,
    )
    await state.set_state(Menu.start)


###расчет цены###
@rt1.message(Menu.calc)
async def calc(message: Message, state: FSMContext):
    await message.answer(
        f"💰Стоимость товара - {(str(int(message.text)*13.5 + 400))} руб(<b>без учета доставки</b>).\n\n❗<i>Доставка зависит от веса товара, поэтому она оплачивается отдельно</i>",
        reply_markup=keyboards.CALC_KEYS,
    )
    await state.set_state(Menu.end_calc)


@rt1.message(Menu.photo_id)
async def handle_photo(message: Message, state: FSMContext):
    file_in_io = io.BytesIO()
    await message.photo[-1].download(destination_file=file_in_io)
    id_photo = message.photo[-1].file_id

    await state.update_data(photo_id = id_photo)
    await message.answer(f"Введите ваше ФИО(как в <b>ПАСПОРТЕ</b>)")
    await state.set_state(Menu.fullname)


###ссылка на товар###
@rt1.message(Menu.fullname)
async def link(message: Message, state: FSMContext):
    await message.answer(f"Отправьте ссылку на ваш товар")
    await state.update_data(fullname = message.text)
    await state.set_state(Menu.link)


###адрес заказчика###
@rt1.message(Menu.link)
async def address(message: Message, state: FSMContext):
    await message.answer(
        f"🚚Введите адрес доставки <b>близлежащего</b> СДЕКА🚚\nНапример:\n<i>г.Москва, Можайский переулок 3</i>"
    )
    await state.update_data(link = message.text)
    await state.set_state(Menu.address)


###выбранный размер товара###
@rt1.message(Menu.address)
async def item_size(message: Message, state: FSMContext):
    await message.answer(
        f"Напишите ваш размер выбранного товара\n<i>Если это одежда, то размер указывать в формате: S,M,L,XL...\nЕсли это обувь, то в формате: 42.5,43,44,38....</i>"
    )
    await state.update_data(address = message.text)
    await state.set_state(Menu.size)
    

###цена товара###
@rt1.message(Menu.size)
async def price(message: Message, state: FSMContext):
    await message.answer(f"Напишите цену вашего товара в юанях")
    await state.update_data(size = message.text)
    await state.set_state(Menu.price)
    

###добавление в бд###
@rt1.message(Menu.price)
async def add_process(message: Message, state: FSMContext):
    
    data = await state.get_data()
    photo_id = data.get('photo_id')
    fullname = data.get('fullname')
    link = data.get('link')
    address = data.get('address')
    size = data.get('size')
    
    await add_user_to_db(message.from_user.id, photo_id, fullname, link, address, size, price)
    await state.clear()
    
    user_data = await get_user_data(message.from_user.id)
    if user_data:
        user_order = f"Ваше ФИО: {user_data['fullname']}\nСсылка на ваш товар: {user_data['link']}\nАдрес доставки: {user_data['address']}\nРазмер вашего товара: {user_data['size']}\nЦена товара: {user_data['price']}\nВнимательно проверяйте ваши данные"
        photo_file = await message.get_file(photo_id)
        photo_input_file = InputFile(photo_file.file_path)
    await message.answer_photo(
        photo=photo_input_file,
        caption=user_order
    )
    await message.answer(user_order, reply_markup=keyboards.ORDER_KEYS)



# @rt1.message(Menu.photo)
# async def fullname(message: Message, state: FSMContext):
#     await message.answer(f"Введите ваше ФИО(как в <b>ПАСПОРТЕ</b>)")
#     await state.set_state(Menu.fullname)