import discord
from discord.ext import commands
class Roadmap(commands.Cog):
    """
    sets up the basic components of the class
    @bot - the bot iself
    @last_member - the last member who used this command
    return - nothing
    """
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    """
    Where the command is executed
    @self = self argument needed for the function
    @context = how we'll send messages
    return - nothing
    """
    @commands.command(aliases = ['certifications', 'certs'])
    async def certRoadmap(self, context, argument = None):
        """
        Returns the CompTIA cert roadmap
        """
        roadmapEmbed = discord.Embed(title="CompTIA's IT Certification Roadmap",
                                     description="https://imgur.com/a/hctdZ07")
        roadmapEmbed.set_image(url='https://cdn.discordapp.com/attachments/750841497733169333/769254094371553350/it-certification-roadmap1024_1.jpg')
        await context.send(embed = roadmapEmbed)
        
def setup(bot):
    bot.add_cog(Roadmap(bot))
