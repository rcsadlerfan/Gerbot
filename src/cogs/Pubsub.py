import discord
from discord.ext import commands
import pubsub
import json
import re
class Pubsub(commands.Cog):
    """
    sets up the basic components of the class
    @bot - the bot iself
    @last_member - the last member who used this command
    return - nothing
    """
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command(aliases = ['pubsub', 'pubSub', 'getPubSub'])
    async def getPubsub(self, context, *, sub_argument = None):
        """
        Fetches a delicious pubsub
        """
        if(sub_argument != None):
            if(sub_argument == "help"):
                try:
                    subs = pubsub.get_all_subs()
                    await context.send(f"{context.author.mention}, here is our list of subs! \n" + subs)
                except:
                    print("API is down...")
                    await context.send(context.author.mention + ", unfortunately the api is down. Try again some other time!\n")
            sub = pubsub.get_pub_sub(sub_argument)
            if(sub.status_code == "OK"):
                original_sub_argument = sub_argument.replace("-", " ")
                sub_argument_changed = sub_argument.replace(" ", "-")
                if(sub.status == "True"):
                    await context.send(f"{context.author.mention}, here is your {original_sub_argument}, it's on sale!")
                    pubsub_message = discord.Embed(title="Latest deal for pubsubs" , description="Beep beep, I bring you the most current pubsub deals!")
                    pubsub_message.add_field(name="Latest news on " + original_sub_argument, value="Current sale last from " + sub.last_sale + " with a price of " + sub.price)
                    pubsub_message.set_image(url=sub.image)
                    await context.send(embed=pubsub_message)
                else:
                    pubsub_message = discord.Embed(title="Latest deal for pubsubs" , description="Beep beep, I bring you the most current pubsub deals!")
                    pubsub_message.add_field(name="Last time " + original_sub_argument + " was on sale", value="Last sale was from " + sub.last_sale)
                    pubsub_message.set_image(url=sub.image)
                    await context.send(embed=pubsub_message)
            elif(sub.status_code == "404"):
                await context.send("The pubsub api does not contain that sub, please try another sub!")

        else:
            sub = pubsub.empty_sub_input()
            sub_argument = sub.sub_argument
            last_sale = sub.last_sale
            status = sub.status
            price = sub.price
            image = sub.image
            sub_argument = sub_argument.replace("-", " ")
            if(status == "True"):
                await context.send(f"{context.author.mention}, here is your {sub_argument}, it's on sale!")
                pubsub_message = discord.Embed(title="Latest deal for pubsubs" , description="Beep beep, I bring you the most current pubsub deals!")
                pubsub_message.add_field(name="Latest news on " + sub_argument, value="Current sale last from " + last_sale + " with a price of " + price)
                pubsub_message.set_image(url=image)
                await context.send(embed=pubsub_message)
            else:
                pubsub_message = discord.Embed(title="Latest deal for pubsubs" , description="Beep beep, I bring you the most current pubsub deals!")
                pubsub_message.add_field(name="Last time " + sub_argument + " was on sale", value="Last sale was from " + sub.last_sale)
                pubsub_message.set_image(url=sub.image)
                await context.send(embed=pubsub_message)
                
def setup(bot):
    bot.add_cog(Pubsub(bot))