from os import getenv
from dotenv import load_dotenv
from discord.utils import get as get_obj
from discord.ext.commands import Bot
from info_team.commands import InfoCommand

load_dotenv()
GUILD = getenv("DISCORD_GUILD")


class FullBot(Bot):
    """ Custom Bot, subclass discord.ext.commands.Bot """

    def __init__(self):
        """ init discord.ext.commands.Bot and add custom commands """
        super().__init__(command_prefix="!")
        self.add_cog(InfoCommand(self))
        self.guild = ""

    def run(self, token):
        super().run(token)

    # Events
    async def on_ready(self):
        """ print in console when bot is started and connected """
        self.guild = get_obj(self.guilds, name=GUILD)
        print('{} is connected to "{}"'.format(self.user, self.guild.name))