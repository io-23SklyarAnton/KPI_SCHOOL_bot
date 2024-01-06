import os
from aiogram import types
from Core.middlewares.database import fill_data
from Core.keyboard.download_get_kb import save_send_builder
from aiogram.fsm.context import FSMContext
from Core.handlers.states import BasicStates


async def start(message: types.Message, state: FSMContext):
    first_name = message.from_user.first_name
    user_id = message.from_user.id

    fill_data.insert_user(user_id, first_name)
    try:
        os.mkdir(os.path.join(r"D:\KPI_SCHOOL_bot\user_files", f"{user_id}"))
    except FileExistsError:
        pass
    await message.answer(f"Hello, {message.from_user.first_name}",
                         reply_markup=save_send_builder.as_markup(resize_keyboard=True))
    await state.set_state(BasicStates.start_state)


async def cancel(message: types.Message, state: FSMContext):
    await message.answer(f"Back to main menu", reply_markup=save_send_builder.as_markup(resize_keyboard=True))
    await state.set_state(BasicStates.start_state)


async def help(message: types.Message):
    await message.answer("""
This bot can take documents,photos,videos,etc\n
It gives you a commands to take back your files or to send it to the other guy\n
""")
