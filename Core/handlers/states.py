from aiogram.fsm.state import StatesGroup, State


class BasicStates(StatesGroup):
    start_state = State()


class DownloadFileStates(StatesGroup):
    description_state = State()
    download_ready_state = State()


class GetFileStates(StatesGroup):
    get_ready_state = State()
    get_last_files_state = State()
    description_state = State()
    send_files_state = State()
