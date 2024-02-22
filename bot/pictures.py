from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

start_photo = FSInputFile("/Users/absq/Desktop/bobolink/picturesforbot/bobolink.jpg")


calc_photo = MediaGroupBuilder(
    caption=f"В нашем <b>калькуляторе</b> вы можете сделать расчет стоимости заказа<b>(ДОСТАВКА ЗАВИСИТ ОТ ВЕСА ЗАКАЗА, ПОЭТОМУ ОНА ОПЛАЧИВАЕТСЯ ОТДЕЛЬНО)</b>\nЧтобы произвести расчет введите цену<b>(предварительно выбрав свой размер)</b> с одной из трех кнопок.\nЗначение кнопок:\n1<b>(голубая)</b>🌐 - быстрая доставка\n2<b>(черная)</b>⚫️- медленная доставка\n3<b>(серая)</b>🔘 - бу вещь\n<i>❗❗❗внимательно смотрите на знак '≈' перед ценой</i>(<b>НЕЛЬЗЯ ЗАКАЗАТЬ</b>)"
)
calc_photo.add_photo(
    media=FSInputFile("/Users/absq/Desktop/bobolink/picturesforbot/example_price.PNG")
)
calc_photo.add_photo(
    media=FSInputFile("/Users/absq/Desktop/bobolink/picturesforbot/examp.jpg")
)

order_photo = MediaGroupBuilder(
    caption=f"<b>(ДОСТАВКА ЗАВИСИТ ОТ ВЕСА ЗАКАЗА, ПОЭТОМУ ОНА ОПЛАЧИВАЕТСЯ ОТДЕЛЬНО)</b>\n\nЧтобы cделать заказ отправьте скриншот товара(как на 1 фото)<b>(предварительно выбрав свой размер)</b> с одной из трех кнопок.\n\nЗначение кнопок:\n1<b>(голубая)</b>🌐 - быстрая доставка\n2<b>(черная)</b>⚫️- медленная доставка\n3<b>(серая)</b>🔘 - бу вещь\n<i>❗❗❗внимательно смотрите на знак '≈' перед ценой</i>(<b>НЕЛЬЗЯ ЗАКАЗАТЬ</b>)(2 фото)"
)
order_photo.add_photo(
    media=FSInputFile("/Users/absq/Desktop/bobolink/picturesforbot/example_price.PNG")
)
order_photo.add_photo(
    media=FSInputFile("/Users/absq/Desktop/bobolink/picturesforbot/examp.jpg")
)
