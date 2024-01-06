from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

save_send_builder = ReplyKeyboardBuilder()
save_send_builder.row(KeyboardButton(text="/save"), KeyboardButton(text="/send"))

cancel_builder = ReplyKeyboardBuilder()
cancel_builder.row(KeyboardButton(text="/cancel"))

send_files_builder = ReplyKeyboardBuilder()
send_files_builder.row(KeyboardButton(text="/get_last_files"), KeyboardButton(text="/send_file"))
