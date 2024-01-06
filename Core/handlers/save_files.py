import os
from aiogram import types
from aiogram import Bot
from Core.middlewares.database import fill_data
from aiogram.fsm.context import FSMContext
from Core.handlers.states import DownloadFileStates
from Core.keyboard.download_get_kb import cancel_builder


async def save(message: types.Message, state: FSMContext):
    await message.answer(f"Please, write a description to your file", reply_markup=cancel_builder.as_markup(resize_keyboard=True))
    await state.set_state(DownloadFileStates.download_ready_state)


async def save_photo(message: types.Message, bot: Bot):
    best_photo = message.photo[-1]
    user_id = message.from_user.id
    file_id = best_photo.file_id
    send_date = message.date
    description = message.caption if message.caption else file_id
    dest_path = os.path.join(r"D:\KPI_SCHOOL_bot\user_files", f"{user_id}", f"{description}.jpg")

    result = fill_data.insert_file(user_id=user_id, file_id=file_id, send_date=send_date, description=description,
                                   file_type="photo")
    await bot.download(
        file=file_id,
        destination=dest_path
    )
    await message.reply(result, reply_markup=cancel_builder.as_markup(resize_keyboard=True))


async def save_video(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    file_id = message.video.file_id
    send_date = message.date
    description = message.caption if message.caption else file_id
    dest_path = os.path.join(r"D:\KPI_SCHOOL_bot\user_files", f"{user_id}", f"{description}.mp4")

    result = fill_data.insert_file(user_id=user_id, file_id=file_id, send_date=send_date, description=description,
                                   file_type="video")
    await bot.download(
        file=file_id,
        destination=dest_path
    )
    await message.reply(result, reply_markup=cancel_builder.as_markup(resize_keyboard=True))


async def save_sticker(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    file_id = message.sticker.file_id
    send_date = message.date
    description = file_id
    dest_path = os.path.join(r"D:\KPI_SCHOOL_bot\user_files", f"{user_id}", f"{description}.webp")

    result = fill_data.insert_file(user_id=user_id, file_id=file_id, send_date=send_date, description=description,
                                   file_type="sticker")
    await bot.download(
        file=file_id,
        destination=dest_path
    )
    await message.reply(result, reply_markup=cancel_builder.as_markup(resize_keyboard=True))


async def save_document(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    file_id = message.document.file_id
    send_date = message.date
    description = message.document.file_name
    dest_path = os.path.join(r"D:\KPI_SCHOOL_bot\user_files", f"{user_id}", f"{description}")

    result = fill_data.insert_file(user_id=user_id, file_id=file_id, send_date=send_date, description=description,
                                   file_type="document")
    await bot.download(
        file=file_id,
        destination=dest_path
    )
    await message.reply(result, reply_markup=cancel_builder.as_markup(resize_keyboard=True))


async def save_audio(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    file_id = message.audio.file_id
    send_date = message.date
    description = message.caption if message.caption else message.audio.title
    dest_path = os.path.join(r"D:\KPI_SCHOOL_bot\user_files", f"{user_id}", f"{description}.mp3")

    result = fill_data.insert_file(user_id=user_id, file_id=file_id, send_date=send_date, description=description,
                                   file_type="audio")
    await bot.download(
        file=file_id,
        destination=dest_path
    )
    await message.reply(result, reply_markup=cancel_builder.as_markup(resize_keyboard=True))
