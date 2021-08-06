from aiogram import types

from loader import dp

from checkWord import checkWord

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    word = message.text
    if len(word.split())>2:
        words = word.split()
        for word in words:
            result = checkWord(word)
            if result['available']:
                response = f"✅ {word.capitalize()}"
            else:
                response = f"❌{word.capitalize()}\n"
                for text in result['matches']:
                    response += f"✅ {text.capitalize()}\n"
            await message.answer(response)
    else:
        result = checkWord(word)
        if result['available']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌{word.capitalize()}\n"
            for text in result['matches']:
                response += f"✅ {text.capitalize()}\n"
        await message.answer(response)
