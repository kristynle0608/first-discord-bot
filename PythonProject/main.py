from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#S STEP 0: LOAD OUR TOKEN
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content =  True # NOQA
client: Client = Client(intents=intents)

#STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str, username: str) -> None:
    if not user_message:
        print('(Message was empty')
        return

    if command := user_message[0] == '!':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message, username)
        if 'bear' in username and 'impost' in user_message.lower():
            await message.channel.send("no u")

        elif command:
            await message.channel.send(response)
    except Exception as e:
        print(e)

# STEP 3: BOT STARTUP
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message, username)

# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()