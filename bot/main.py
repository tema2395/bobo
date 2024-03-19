import os, asyncio, logging, sys
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from routers import rt1
from callbacks import rt2


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")  # токен бота
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


bot = Bot(TOKEN, parse_mode=ParseMode.HTML)  # экземпляр бота
dp = Dispatcher()  # экземпляр диспетчера


async def main() -> None:
    dp.include_routers(rt1, rt2)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
