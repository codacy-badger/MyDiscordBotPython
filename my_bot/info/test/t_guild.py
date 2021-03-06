from aiounittest import AsyncTestCase
from unittest.mock import Mock, patch
from discord.ext.commands import Cog
from ..guild import InfoGuildCommands
from ..shaping import GuildEmbed
from ..config import GUILD_TITLES as titles
from .fakers import BOT, CONTEXT
from .results import InfoGuildCommandsTestResult


class InfoGuildCommandsTest(AsyncTestCase):
    """ Async Test case for cog InfoGuildCommands """

    def setUp(self):
        """ Init tests with cog and expected results """
        self.cog = InfoGuildCommands(BOT)
        self.result = InfoGuildCommandsTestResult()
        self.maxDiff = None

    def test_init(self):
        """ assert after init is instance Cog, the number of commands
        and if they have good name and help """
        self.assertIsInstance(self.cog, Cog)
        commands = self.cog.get_commands()
        self.assertEqual(len(commands), 12)
        c_tuples = [(c.name, c.help) for c in commands]
        for i in range(len(commands)):
            self.assertTupleEqual(c_tuples[i], self.result.init_method[i])

    async def assert_send_method(self, method, result):
        """ reset mock called count and args, and assert if
        send method is called once and if the good embed is sended """
        CONTEXT.send.reset_mock()
        await method.callback(self.cog, CONTEXT)
        CONTEXT.send.assert_called_once()
        args, kwargs = CONTEXT.send.call_args
        self.assertDictEqual(kwargs['embed'].to_dict(), result)

    async def test_guild(self):
        """ assert send method after guild command """
        await self.assert_send_method(self.cog.guild, self.result.guild)

    def test_make_objs_embed(self):
        """ assert if make_objs_embed return the good embed """
        embed = self.cog.make_objs_embed(
            'Guild Embed Test', 'https://url.com/icon.png',
            titles.mem, CONTEXT.guild.members)
        self.assertIsInstance(embed, GuildEmbed)
        self.assertDictEqual(embed.to_dict(), self.result.make_objs_embed)

    async def test_owner(self):
        """ assert send method after owner command """
        await self.assert_send_method(self.cog.owner, self.result.owner)

    async def test_members(self):
        """ assert send method after members command """
        await self.assert_send_method(self.cog.members, self.result.members)

    async def test_roles(self):
        """ assert send method after roles command """
        await self.assert_send_method(self.cog.roles, self.result.roles)

    async def test_categories(self):
        """ assert send method after categories command """
        await self.assert_send_method(
            self.cog.categories, self.result.categories)

    async def test_channels(self):
        """ assert send method after channels command """
        await self.assert_send_method(self.cog.channels, self.result.channels)

    async def test_text_channels(self):
        """ assert send method after text_channels command """
        await self.assert_send_method(
            self.cog.text_channels, self.result.text_channels)

    async def test_voice_channels(self):
        """ assert send method after voice_channels command """
        await self.assert_send_method(
            self.cog.voice_channels, self.result.voice_channels)

    async def test_news_channels(self):
        """ assert send method after news_channels command """
        await self.assert_send_method(
            self.cog.news_channels, self.result.news_channels)

    async def test_store_channels(self):
        """ assert send method after store_channels command """
        await self.assert_send_method(
            self.cog.store_channels, self.result.store_channels)

    async def test_emojis(self):
        """ assert send method after emojis command """
        await self.assert_send_method(
            self.cog.emojis, self.result.emojis)

    async def test_shell_info(self):
        """ reset mock called count and args, and assert if
        print function and the context send method is called once
        with the good string """
        CONTEXT.send.reset_mock()
        mock_print = Mock()
        with patch("builtins.print", mock_print):
            await self.cog.shell_info.callback(self.cog, CONTEXT)
            mock_print.assert_called_once_with(self.result.shell_info)
            CONTEXT.send.assert_called_once_with("Infos displayed in shell")
