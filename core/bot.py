import os
import dotenv

from discord.ext import commands

dotenv.load_dotenv()

class VBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="?"
        )

    def load_cogs(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    self.load_extension(f'cogs.{filename[:-3]}')
                except Exception as e:
                    raise e

    def run(self):
        self.load_cogs()
        
        token = os.getenv("TOKEN")
        super().run(token, reconnect=True)
