#import necessary libraries
import discord
from discord.ext import commands
import os

import functions
import plotting
import bot_token

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)
refreshing = False
pts = 0

@bot.event
async def on_ready():
    print(f"Successfully logged in as '{bot.user}' (ID: {bot.user.id}), in {len(bot.guilds)} guilds:")
    for guild in bot.guilds:
        print(f"- {guild.id}: {guild.name}")
    await bot.change_presence(activity=discord.Game("Territorial.io"))

#all slash commands
@bot.slash_command(description="Check KANHNI Clan Stats")
async def kanhni(ctx):
    await ctx.trigger_typing()
    d = functions.get_clan_output("KANHNI")
    if (d == "not existing"):
        response = "The KANHNI clan is currently so bad that it has been deleted from the official clan list!!!"
    else:
        response = "Clan: " + d[1] + "\nPlace: " + d[0] + "\nPoints: " + d[2] + "\nInformation from " + functions.shaped_list[0].replace("Clan Leaderboard ", "")
    await ctx.respond(response)

@bot.slash_command(description="Check Any Clan's Stats")
async def checkclan(ctx, clan: str):
    await ctx.trigger_typing()
    clan_infos = functions.get_clan_output(clan)

    if clan_infos != "not existing" and clan_infos != "error" and clan_infos != False:
        response = "Clan: " + clan_infos[1] + "\nPlace: " + clan_infos[0] + "\nPoints: " + clan_infos[2] + "\nInformation from " + functions.shaped_list[0].replace("Clan Leaderboard ", "")
        await ctx.respond(response)
    elif clan_infos == "error":
        await ctx.respond("There was an error downloading the list of clans, please try again later.")
    elif clan_infos == "not existing":
        await ctx.respond("This clan does apparently not exist") 
    elif clan_infos == False:
        await ctx.respond("There has been error. Please try again later")
    else:
        await ctx.respond("There was an unknown error. INFORM THE DEVELOPERS **IMMEDIATELY**")# XD

@bot.slash_command(description="Check Stats Of A Username")
async def checkplayer(ctx, player: str):
    await ctx.trigger_typing()
    player_infos = functions.get_player_output(player)

    if player_infos != "not existing" and player_infos != "error" and player_infos != False:
        response = "Player: " + player_infos[1] + "\nPlace: " + player_infos[0] + "\nPoints: " + player_infos[2] + "\nInformation from " + functions.shaped_list[0].replace("Clan Leaderboard ", "")
        await ctx.respond(response)
    elif player_infos == "error":
        await ctx.respond("There was an error downloading the list of players, please try again later.")
    elif player_infos == "not existing":
        await ctx.respond("This player does apparently not exist") 
    elif player_infos == False:
        await ctx.respond("There has been error. Please try again later")
    else:
        await ctx.respond("There was an unknown error. INFORM THE DEVELOPERS **IMMEDIATELY**")

@bot.slash_command(description="View Clan Leaderboard")
async def leaderboard(ctx, lenght: int = 10):
    await ctx.trigger_typing()
    d = functions.get_leaderboard(int(lenght) + 4)
    if d == "leaderboard":
        await ctx.respond(file=discord.File("leaderboard.txt"))
    else:
        await ctx.respond(d)
    print("Someone checked the clan leaderboard with lenght of " + str(lenght))

@bot.slash_command(description="Clans Page")
async def clanlist(ctx):
    await ctx.respond("https://territorial.io/clans")

@bot.slash_command(description="Generate Diagram")
async def diagram(ctx):
    await ctx.respond(file=discord.File("graph.png"))
    #await ctx.send("_work in progress_")

try:
    plotting.runTask("KANHNI")
    bot.run(bot_token.token)
except Exception as ex:
    if os.path.exists("clans.txt"):
        os.remove("clans.txt")
    else:
        print("The clans file does not exist")
        
    if os.path.exists("players.txt"):
        os.remove("players.txt")
    else:
        print("The players file does not exist")
    print("Some error occurred:")
    print(ex)