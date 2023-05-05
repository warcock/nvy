import discord
import time
import datetime
from termcolor import colored
from discord import app_commands
from discord.utils import get

intents = discord.Intents.default()
bot = discord.Client(intents=intents,status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name="zems market | warcock#0001"))
tree = app_commands.CommandTree(bot)

# -----------------------------------------------

class desiredRewrite:
    desiredRewriteV1_ServerID = 905732450150391838
    desiredRewriteV1_RoleRequiredID = 908242120073162772
    desiredRewriteV1_BotToken = "MTAxOTI0MzAzODM3NzI2NzI3MQ.GW8VfA.YBqNLpEmMl1v4nS-z3av5YQKwdw0EPpwqbDtdI"
    desiredRewriteV1_Color_Purple = '\033[95m'
    desiredRewriteV1_Color_Cyan = '\033[96m'
    desiredRewriteV1_Color_DarkCyan = '\033[36m'
    desiredRewriteV1_Color_Blue = '\033[94m'
    desiredRewriteV1_Color_Green = '\033[92m'
    desiredRewriteV1_Color_Yellow = '\033[93m'
    desiredRewriteV1_Color_Red = '\033[91m'
    desiredRewriteV1_Text_BoldFont = '\033[1m'
    desiredRewriteV1_Text_UnderlineText = '\033[4m'
    desiredRewriteV1_Text_Color_End = '\033[0m'
    
# -----------------------------------------------

# -----------------------------------------------

@tree.command(name = "help", description = "sends a list of commands", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def help(interaction: discord.Interaction):
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name=f"**help**",value="sends a list of commands", inline=False)
        embed.add_field(name=f"**membercount**",value="shows the member count of the guild", inline=False)
        embed.add_field(name=f"**ping**",value="sends the bot's latency", inline=False)
        embed.add_field(name=f"**pdadd `member` `amount`**",value="adds a person to the pending list", inline=False)
        embed.add_field(name=f"**pdremove `member`**",value="removes a person from the pending list", inline=False)
        embed.add_field(name=f"**dahood `amount`**",value="loads the gamepass list for dahood cash", inline=False)
        embed.add_field(name=f"**fastpass `type`**",value="loads the gamepass list for fastpasses", inline=False)
        embed.add_field(name=f"**drop**",value="pings customer inside dropping status channel to let them know you are dropping", inline=False)
        embed.add_field(name=f"**predrop `amount`**",value="pings customer inside dropping status channel to let them know you've dropped [amount]", inline=False)
        embed.add_field(name=f"**format**", value="sends the format for buying dhc", inline=False)
        embed.add_field(name=f"**transactions**", value="sends the link to check for transactions", inline=False)
        embed.add_field(name=f"**verify**",value="verifies the current ticket", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)

@tree.command(name = "membercount", description = "shows the total count of members inside the server", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def embed(interaction: discord.Interaction):
    embed = discord.Embed(color=0x2F3136)
    guild = interaction.guild
    embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
    embed.add_field(name=f"**membercount**", value=f"{guild.name} currently has `{guild.member_count}` total members", inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    await interaction.response.send_message(embed=embed)

@tree.command(name = "ping", description = "sends the bot's latency", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def embed(interaction: discord.Interaction):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
    embed.add_field(name="**ping**", value=f"{round(bot.latency * 1000)} ms")
    embed.timestamp = datetime.datetime.utcnow()
    await interaction.response.send_message(embed=embed)

@tree.command(name = "pdadd", description = "adds a member to the pending list", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def pdadd(interaction: discord.Interaction, member: discord.Member, amount: int, price: str, payment: str):
    bot.role = interaction.guild.get_role(desiredRewrite.desiredRewriteV1_RoleRequiredID)
    if bot.role not in interaction.user.roles:
        await interaction.response.send_message("**`failed`** `//` **`you do not have permission to run this command!`**")
    else:
        desiredRewriteGetRole = get(member.guild.roles, id=1091467375011971234)
        await member.add_roles(desiredRewriteGetRole) 
        FormatEmbed = f"""
        username ; `{member}`                                 
        amount ; `{amount}`  
        price ; `{price}`    
        payment method ; `{payment}`
        """
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**pending list add [success]**", value=f"{member} has been added to the pending list! [{amount}m pending]")
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/905732450150391838/a_69bf83a8da7f34ae2ab3b360cbc42536.gif?size=4096')
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
        embed1 = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed1.add_field(name="**pending [add]**", value=f"\n", inline=False)
        embed1.add_field(name=f"\n", value=f"{FormatEmbed}", inline=False)
        embed1.set_thumbnail(url=member.avatar)
        embed1.timestamp = datetime.datetime.utcnow()
        await bot.get_channel(1103243896781291560).send(embed=embed1)

@tree.command(name = "pdremove", description = "removes a member from the pending list", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def pdremove(interaction: discord.Interaction, member: discord.Member):
    bot.role = interaction.guild.get_role(desiredRewrite.desiredRewriteV1_RoleRequiredID)
    if bot.role not in interaction.user.roles:
        await interaction.response.send_message("**`failed`** `//` **`you do not have permission to run this command!`**")
    else:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**pending list remove [success]**", value=f"{member} has been removed the pending list!")
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/905732450150391838/f296c4eaa9b28be26620485f0b0e3de1.png?size=1024')
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
        embed1 = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed1.add_field(name="**pending [remove]**", value=f"{member}'s order has been completed! [pending embed deletion]")
        embed1.set_thumbnail(url='https://cdn.discordapp.com/icons/905732450150391838/f296c4eaa9b28be26620485f0b0e3de1.png?size=1024')
        embed1.timestamp = datetime.datetime.utcnow()
        await bot.get_channel(1103243896781291560).send(embed=embed1)

@tree.command(name = "dahood", description = "sends the amount of da hood cash you want to buy", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
@app_commands.describe(amount="amount of da hood cash to choose from")
@app_commands.choices(amount=[
    discord.app_commands.Choice(name='1M', value=1),
    discord.app_commands.Choice(name='2M', value=2),
    discord.app_commands.Choice(name='3M', value=3),
    discord.app_commands.Choice(name='4M', value=4),
    discord.app_commands.Choice(name='5M', value=5),
    discord.app_commands.Choice(name='6M', value=6),
    discord.app_commands.Choice(name='7M', value=7),
    discord.app_commands.Choice(name='8M', value=8), 
    discord.app_commands.Choice(name='9M', value=9),
    discord.app_commands.Choice(name='10M', value=10),
    discord.app_commands.Choice(name='10M [SHIRT]', value=11),
])
async def dahood(interaction: discord.Interaction, amount: discord.app_commands.Choice[int]):
    if amount.value == 1:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/126639003/desires")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
    elif amount.value == 2:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/126639128/desires")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
    elif amount.value == 3:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/126639248/desires")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
    elif amount.value == 4:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/126639425/4")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
    elif amount.value == 5:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/126639530/5")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
    elif amount.value == 6:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/126639686/6")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
    elif amount.value == 7:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/126639843/unnamed")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
    elif amount.value == 8:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/126640098/unnamed")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
    elif amount.value == 9:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/126640228/unnamed")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)
    elif amount.value == 10:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/126640277/unnamed")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)    
    elif amount.value == 11:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/catalog/12830688443/10M-DHC")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)   

@tree.command(name = "fastpass", description = "sends the type of fastpass you want to buy", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
@app_commands.describe(type="type of fast pass to choose from")
@app_commands.choices(type=[
    discord.app_commands.Choice(name='one time fast pass [1] - unavaiable', value=1),
    discord.app_commands.Choice(name='one time fast pass [2] - unavaiable', value=2),
    discord.app_commands.Choice(name='permanent fast pass', value=3),
])
async def fastpass(interaction: discord.Interaction, type: discord.app_commands.Choice[int]):
    if type.value == 1:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // fast pass**", value=f"nil")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)   
    elif type.value == 2:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // fast pass**", value=f"nil")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)   
    elif type.value == 3:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // fast pass**", value=f"https://www.roblox.com/catalog/12837544851/FAST-PASS-PERMANENT")
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)   

@tree.command(name = "drop", description = "sends a message into the dropping status channel to tell customers that you are dropping", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def drop(interaction: discord.Interaction, size: str):
    bot.role = interaction.guild.get_role(desiredRewrite.desiredRewriteV1_RoleRequiredID)
    if bot.role not in interaction.user.roles:
        await interaction.response.send_message("**`failed`** `//` **`you do not have permission to run this command!`**")
    else:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**dropping!**", value=f"{interaction.user} is currently dropping `{size}` orders, ping them inside your ticket!")
        embed.timestamp = datetime.datetime.utcnow()
        await bot.get_channel(1086104928843477002).send("<@&1102160969095987244>", embed=embed)
        embed1 = discord.Embed(color=0x2F3136)
        embed1.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed1.add_field(name="**success! // drop**", value=f"message successfully sent! [{size}]")
        embed1.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed1)

@tree.command(name = "predrop", description = "sends a message into the current chat for predropped cash", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def predrop(interaction: discord.Interaction, amount: int):
    bot.role = interaction.guild.get_role(desiredRewrite.desiredRewriteV1_RoleRequiredID)
    if bot.role not in interaction.user.roles:
        await interaction.response.send_message("**`failed`** `//` **`you do not have permission to run this command!`**")
    else:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**predropped!**", value=f"{interaction.user} has dropped {amount}m! ping them in your ticket!")
        embed.timestamp = datetime.datetime.utcnow()
        await bot.get_channel(1086104928843477002).send("<@&1102160969095987244>", embed=embed)
        embed1 = discord.Embed(color=0x2F3136)
        embed1.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed1.add_field(name="**success! // predrop**", value=f"message successfully sent! [{amount}]")
        embed1.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed1)
@tree.command(name = "format", description = "sends the format for buying dhc", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def format(interaction: discord.Interaction):
    format1 = """```diff
- please wait until a staff, dropper, or a owner responds to your ticket.
    ```
    """
    format2 = """```diff
+ amount of dhc
+ form of payment [robux, cashapp, etc]
+ timezone

- WE DO NOT ACCEPT REFUNDS AFTER YOU HAVE PURCHASED, THIS IS FINAL!

[[       discord.gg/zdhc       ]]
    ```
    """
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
    embed.add_field(name="**thanks for buying from zems da hood cash store!**", value="please use the following format!", inline=False)
    embed.add_field(name=f"\n", value=format1, inline=False)
    embed.add_field(name=f"\n", value=format2, inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    await interaction.response.send_message(embed=embed)  

@tree.command(name = "transactions", description = "sends the link to check for transactions", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def transactions(interaction: discord.Interaction):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
    embed.add_field(name="**transactions**", value="https://www.roblox.com/transactions", inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    await interaction.response.send_message(embed=embed)  

@tree.command(name = "verify", description = "verifies the current ticket you are sending this message in", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def verify(interaction: discord.Interaction, member: discord.Member):
    bot.role = interaction.guild.get_role(desiredRewrite.desiredRewriteV1_RoleRequiredID)
    customerTrue = discord.utils.get(interaction.guild.roles, id=1091467375011971234)
    if bot.role not in interaction.user.roles:
        await interaction.response.send_message("**`failed`** `//` **`you do not have permission to run this command!`**")
    else:
        customerRole = get(member.guild.roles, id=1091467375011971234)
        await member.add_roles(customerRole) 
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**Thanks for buying from zems market!**", value=f"your ticket has been **checked & verified** by `{interaction.user} / [{interaction.user.id}]`", inline=False)
        embed.add_field(name=f"\n", value="The average wait time for your order is around `1-2` days, if you wish to pay extra to get your order a bit faster, please use the following command", inline=False)
        embed.add_field(name=f"\n", value="Run `/fastpass` in your ticket and send proof of purchase.", inline=False)
        embed.add_field(name=f"\n", value="What should I do after getting my order verified?", inline=False)
        embed.add_field(name=f"\n", value="Please be patient, don't ask multiple times for your cash. It wont speed up the process.", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)  


# -----------------------------------------------

@bot.event 
async def on_ready():
    await tree.sync(guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
    print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + desiredRewrite.desiredRewriteV1_Text_BoldFont + desiredRewrite.desiredRewriteV1_Color_Blue + " INFO     " + desiredRewrite.desiredRewriteV1_Text_Color_End + desiredRewrite.desiredRewriteV1_Color_Purple + "discord.gateway" + desiredRewrite.desiredRewriteV1_Text_Color_End + f" logged in {bot.user} [{bot.user.id}].")

bot.run(desiredRewrite.desiredRewriteV1_BotToken)
