import discord
import requests
from discord.ext import commands
import json
import cats
class Cat(commands.Cog):
    """
    Creates the instance of admin including its fields
    @bot - the bot itself
    @last_member - last member to use this
    return - nothing
    """
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    """
    deletes the role that is selected
    @self - self obj
    @context - how we'll send messages
    @arg - arguments following the command
    return - nothing
    """
    @commands.command(pass_context = True)
    async def getCat(self, context, arg = None):
        """
        Checks if we have input
        """
        if(arg is None):
            await context.send(f"{context.author.mention} seems you have provided no breed, try again!")
        else:
            try:
                cat_picture = cats.returnCat(arg.lower())
                cat_name = cats.getName(arg.lower())
                await context.send(f"{context.author.mention}, here is your {cat_name} that you asked for!")
                cat_message = discord.Embed(title=cat_name[0].upper() + cat_name[1:], description="Beep beep, I am a " + cat_name)
                cat_message.add_field(name="Image url", value=cat_picture)
                cat_message.set_image(url=cat_picture)
                await context.send(embed=cat_message)
            except:
                await context.send("The API we use doesn't have that breed, check out https://api.thecatapi.com/v1/breeds for a full list")
        

    # @commands.command()
    # async def allCats(self, context):
    #     cat_name = cats.returnAll()
    #     cat_message = discord.Embed(title="Cat breeds", description="Beep beep, here are all the cat's ids")
    #     for i in response:
    #         final_result = i["id"]
    #         print(final_result)
    #         cat_message.add_field(name = "Id", value = final_result, inline = True)
    #     await context.send(embed=cat_message)
    

"""
setup for the command
"""
def setup(bot):
    bot.add_cog(Cat(bot))
    