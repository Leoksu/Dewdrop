from pyrogram import filters, Client as ghoul
from ..configs import *
from asyncio import sleep
import requests
import random


def generate_text(prompt):
    data = {'prompt': prompt, 'model': 'text-davinci-002', 'temperature': 0.5}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {API_KEY}'}
    response = requests.post('https://api.openai.com/v1/engines/davinci/completions', json=data, headers=headers)
    return response.json()

@ghoul.on_message(filters.private & ~filters.edited)
async def dewgpt(client, message):
    dewword = {
        1: "I'm sorry, as poor robots, for now I can only understand word. tell @aethersghoul don't be lazy, update me >:(",
        2: "Like i told you before, I only understand word",
        3: "Please use normal word :)",
    }
    if not message.text:
        for key in dewword:
            await message.reply_text(dewword[key])
            if key != len(dewword):
                await message.reply_text(dewword[key+1])
    chat_id = message.chat.id
    prompt = message.text
    await message._client.send_chat_action(chat_id, "typing")
    sleep(3)
    response = generate_text(prompt)
    r_text = response['choice'][0]['text']
    await message.reply(r_text)
    await message._client.send_chat_action(chat_id, "cancel")

@ghoul.on_message(~filters.private & filters.text & ~filters.regex(r'^/'))
async def chat(_, message):
    chat_id = message.chat.id
    dewresponses = [
        "Hello! How can I help you today?",
        "Hello! With Dewdrop here. I'm at your service",
        "Hey! I'm here ready to help you. What can I do for you?",
        "^&;/√%+[\(-$... Ahh Forget it, There's something for me to do? ",
    ]
    random.shuffle(dewresponses)
    dewcall = responses[0]
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}dew[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        match2 = re.search(
            "[.|\n]{0,}dewdrop[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match and not match2:
            return
    await ghoul.send_chat_action(chat_id, "typing")
    await sleep(1)
    await message.reply_text(dewcall)
    await ghoul.send_chat_action(chat_id, "cancel")
