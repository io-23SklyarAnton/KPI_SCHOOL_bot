import os
from aiogram import types
from Core.middlewares.database import fill_data


async def start(message: types.Message):
    first_name = message.from_user.first_name
    user_id = message.from_user.id

    fill_data.insert_user(user_id, first_name)
    try:
        os.mkdir(os.path.join(r"D:\KPI_SCHOOL_bot\user_files", f"{user_id}"))
    except FileExistsError:
        pass
    await message.answer(f"Hello, {message.from_user.first_name}")


async def help(message: types.Message):
    await message.answer("""
This bot can take documents,photos,videos,etc\n
It gives you a commands to take back your files or to send it to the other guy\n
You could give a description to your file,just write a caption for it (without spaces)\n
<b>Main Instructions</b>\n

<i>/get_last_files <u>&lt; amount &gt;</u></i> - this command returns recent files,
where &lt; amount &gt; is the number of recent files (default value is 1)\n

<i>/send_file <u>&lt; description &gt; &lt;addressee_id&gt;</u> </i> - this command can send files to others.It has \
required argument <u>&lt; description &gt;</u> to identify the file you want to send and <u>&lt; addressee_id &gt; \
</u>to identify an addressee (default value is your id)
""")
