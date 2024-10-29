from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.filters import Command

from text import GREETINGS, HELP

router = Router()


@router.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(GREETINGS)


@router.message(Command('help'))
async def help_handler(message: Message):
    await message.answer(HELP)
