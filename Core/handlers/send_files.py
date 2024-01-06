from aiogram import types
from aiogram import Bot
from aiogram.filters import CommandObject
from Core.middlewares.database import get_data
from aiogram.fsm.context import FSMContext
from Core.handlers.states import GetFileStates
from Core.keyboard.download_get_kb import cancel_builder, send_files_builder


async def send(message: types.Message, state: FSMContext):
    await message.answer("Choose options to send", reply_markup=send_files_builder.as_markup(resize_keyboard=True))
    await state.set_state(GetFileStates.get_ready_state)


async def get_last_files(message: types.Message, state: FSMContext):
    await message.answer("Write down, how many files you wanna get",
                         reply_markup=cancel_builder.as_markup(resize_keyboard=True))
    await state.set_state(GetFileStates.get_last_files_state)


async def send_last_files(message: types.Message):
    if not message.text.isdigit():
        await message.answer("Write down a digit, please", reply_markup=cancel_builder.as_markup(resize_keyboard=True))
        return
    file_answers = {"photo": message.answer_photo, "video": message.answer_video, "audio": message.answer_audio,
                    "document": message.answer_document, "sticker": message.answer_sticker}
    user_id = message.from_user.id
    files_amount = int(message.text)
    result = get_data.return_last_files(user_id=user_id, amount=files_amount)

    if result is None:
        await message.answer("Incorrect format, check <i>/help</i>")
        return
    for file in result:
        file_type = file[0]
        file_id = file[1]
        file_description = file[2]
        file_send_date = file[3]

        await file_answers[file_type](file_id)
        await message.answer(f"{file_description} - {file_send_date}")


async def send_file(message: types.Message, command: CommandObject, bot: Bot):
    file_answers = {"photo": bot.send_photo, "video": bot.send_video, "audio": bot.send_audio,
                    "document": bot.send_document, "sticker": bot.send_sticker}
    if command.args is None:
        await message.answer("No arguments, check <i>/help</i>")
        return
    args = command.args.split(maxsplit=1)
    description = args[0]
    addressee = message.from_user.id if len(args) == 1 else args[1]
    user_id = message.from_user.id

    result = get_data.return_file(user_id=user_id, description=description)
    if result is None:
        await message.answer("Incorrect format, check <i>/help</i>")
        return
    for file in result:
        file_type = file[0]
        file_id = file[1]

        await file_answers[file_type](addressee, file_id)
