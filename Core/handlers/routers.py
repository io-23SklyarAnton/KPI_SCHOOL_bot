from aiogram import Router, F
from aiogram.filters import Command
from Core.handlers.send_files import get_last_files, send_file
from Core.handlers.save_files import save_audio, save_video, save_photo, save_sticker, save_document
from Core.handlers.basic import start, help

base_router = Router()
saving_router = Router()
sending_router = Router()

base_router.message.register(start, F.text == "/start")
base_router.message.register(help, F.text == "/help")

saving_router.message.register(save_photo, F.photo)
saving_router.message.register(save_video, F.video)
saving_router.message.register(save_sticker, F.sticker)
saving_router.message.register(save_document, F.document)
saving_router.message.register(save_audio, F.audio)

sending_router.message.register(get_last_files, Command("return_last_files"))
sending_router.message.register(send_file, Command("send_file"))

