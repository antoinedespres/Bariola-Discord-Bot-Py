from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command() # Work in progress
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()


def setup(bot):
    bot.add_cog(Music(bot))
