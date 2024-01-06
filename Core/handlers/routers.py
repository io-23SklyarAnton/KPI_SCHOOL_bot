from aiogram import Router, F
from Core.handlers.send_files import get_last_files, send_file, send, send_last_files
from Core.handlers.save_files import save_audio, save_video, save_photo, save_sticker, save_document, save, file_description
from Core.handlers.basic import start, help, cancel
from Core.handlers.states import BasicStates, GetFileStates, DownloadFileStates

base_router = Router()
saving_router = Router()
sending_router = Router()

base_router.message.register(start, F.text == "/start")
base_router.message.register(help, F.text == "/help")
base_router.message.register(cancel, F.text == "/cancel")

saving_router.message.register(save, F.text == "/save", BasicStates.start_state)
saving_router.message.register(file_description, F.text, DownloadFileStates.description_state)
saving_router.message.register(save_photo, F.photo, DownloadFileStates.download_ready_state)
saving_router.message.register(save_video, F.video, DownloadFileStates.download_ready_state)
saving_router.message.register(save_sticker, F.sticker, DownloadFileStates.download_ready_state)
saving_router.message.register(save_document, F.document, DownloadFileStates.download_ready_state)
saving_router.message.register(save_audio, F.audio, DownloadFileStates.download_ready_state)

sending_router.message.register(send, F.text == "/send", BasicStates.start_state)
sending_router.message.register(get_last_files, F.text == "/get_last_files", GetFileStates.get_ready_state)
sending_router.message.register(send_file, F.text == "/send_file", GetFileStates.get_ready_state)
sending_router.message.register(send_last_files, GetFileStates.get_last_files_state)

