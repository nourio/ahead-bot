from random import choice
from time import sleep
import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix=config.prefix, owner_id="252216078359330817")
#bot.remove_command("help")

logs = bot.get_channel('431817121270333442')

red = 0xFF0000
yellow = 0xFF0000
lime = 0x00FF00
blue = 0x0000FF
pink = 0xFF00FF
turq = 0x00FFFF
purple = 0x800080
colours = [red, yellow, lime, blue, pink, turq, purple]

@bot.event
async def on_ready():
    print ("Running!")
    print ("Username is: %s" % bot.user.name)
    print ("ID is: %s" % bot.user.id)
    print ("Prefix is: %s" % config.prefix)
    await bot.change_presence(game=discord.Game(type=0, name = "Ahead's bot | Prefix: " + config.prefix))

@bot.command(pass_context=True, description="Clears an amount of messages", brief="Clear away!")
@commands.has_role("Admin")
async def clear(ctx, value : int=None):
    await bot.purge_from(ctx.message.channel, limit=value)
    deleted = ":white_check_mark: Deleted %s messages" % str(value)
    await bot.say(deleted)

@bot.command(pass_context=True)
async def avatar(ctx, user : discord.User):
    url = user.avatar_url
    await bot.start_private_message(user)
    await bot.say("%s" % (url)) 

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, user : discord.User, *, reason : str = None):
    if reason == None:
        reason = "an unspeciifed reason."
    embed = discord.Embed(
        title = ("Kick by %s" % ctx.message.author.name),
        description = ("Reason:\n```\n%s\n```" % reason),
        colour = choice(colours)
    )
    embed.add_field(name="Kicked by:", value="%s" % ctx.message.author.name, inline=False)
    embed.add_field(name="User kicked:", value="%s" % user.name, inline=False)
    embed.add_field(name="Punishment:", value="Kick", inline=False)
    await bot.send_message(user, content=None, embed=embed)
    await bot.send_message(user, content="\n\n`You have been kicked. You may rejoin with invite:` https://discord.gg/gZznv9j")
    await bot.send_message(destination=discord.Object(id='431817121270333442'), content=None, embed=embed)
    await bot.kick(user)
    #await bot.send_message(ctx.message.channel, "<@%s> has been kicked for %s, by <@%s>" % (user.id, reason, ctx.message.author.id))

bot.run(config.token)
