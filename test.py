from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/DiscordBot/token.env")
token = os.getenv('token')

print(token)