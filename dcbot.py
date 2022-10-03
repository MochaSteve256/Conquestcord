#import necessary libraries
from re import M
import discord
import threading
from time import sleep as sl
#import matplotlib
import functions

bot = discord.Bot(intents=discord.Intents.all(), debug_guilds=[1025370799386939444])
refreshing = False
pts = 0

@bot.event
async def on_ready():
    print(f'Successfully logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game("Territorial.io"))

#all slash commands
@bot.slash_command(description="Check KANHNI Clan Stats")
async def kanhni(ctx):
    d = functions.get_clan_output("KANHNI")
    response = "Clan: " + d[1] + "\nPlace: " + d[0] + "\nPoints: " + d[2] + "\nInformation from " + functions.shaped_list[0].replace("Clan Leaderboard ", "")
    await ctx.respond(response)

@bot.slash_command(description="Check Any Clan's Stats")
async def checkclan(ctx, clan: str):
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
        await ctx.respond("There was an unknown error. INFORM THE DEVELOPERS **IMMEADITELY**")# XD

@bot.slash_command(description="Check Stats Of A Username")
async def checkplayer(ctx, player: str):
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
        await ctx.respond("There was an unknown error. INFORM THE DEVELOPERS **IMMEADITELY**")

@bot.slash_command(description="View Clan Leaderboard")
async def leaderboard(ctx):
    await ctx.respond("Feature not added yet.")

@bot.slash_command(description="Clans Page")
async def clanlist(ctx):
    await ctx.respond("https://territorial.io/clans")

@bot.slash_command(description="Generate Diagram")
async def diagram(ctx):
    await ctx.respond(file=discord.File("save.png"))

bot.run("MTAyNTM4NDA2MjMzODIyMDA4NA.GHdxWo.66hGOYsNRMLnrFAvnq-oNdvKrQlHyKNdvzsACg")
