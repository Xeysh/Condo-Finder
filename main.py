import requests
import discord
from discord import app_commands
import asyncio
from datetime import datetime

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"Bot is Ready {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

main_url = "https://2ps.club/api/games?guid="

game_list = ["2p", "3p", "30p"]

# for item in game_list:
#     print(f"{item}: Loading status..")

response = requests.get(main_url)
data: str = response.json()

# for x in data:
#     if data[x][1] is True:
#         print(f"{x}: Online")
#     else:
#         print(f"{x}: Offline")

r = requests.get(main_url)

@tree.command(name="upload", description="Uploads condo.")
async def upload(interaction: discord.Interaction):

    embed = discord.Embed(title="**GAME UPLOADS**", description=f"**30 Players:**\n{r.json()['30p'][0]}\n**2 Players:**\n{r.json()['2p'][0]}\n**3 Players:**\n{r.json()['3p'][0]}", color=discord.Color.green(), timestamp=datetime.now())

    await interaction.response.send_message(content=interaction.user.mention,embed=embed)
    await asyncio.sleep(0.3)

    while True:
        await asyncio.sleep(25)
        if r.json()["30p"][1]:
            new_embed = discord.Embed(title="**GAME UPLOADS**", description=f"**30 Players:**\n{r.json()['30p'][0]}\n**2 Players:**\n{r.json()['2p'][0]}\n**3 Players:**\n{r.json()['3p'][0]}", color=discord.Color.green(), timestamp=datetime.now())
            await interaction.edit_original_response(content=interaction.user.mention,embed=new_embed)

        elif r.json()["2p"][1]:
            new_embed = discord.Embed(title="**GAME UPLOADS**", description=f"**30 Players:**\n{r.json()['30p'][0]}\n**2 Players:**\n{r.json()['2p'][0]}\n**3 Players:**\n{r.json()['3p'][0]}", color=discord.Color.green(), timestamp=datetime.now())
            await interaction.edit_original_response(content=interaction.user.mention,embed=new_embed)

        elif r.json()["3p"][1]:
            new_embed = discord.Embed(title="**GAME UPLOADS**", description=f"**30 Players:**\n{r.json()['30p'][0]}\n**2 Players:**\n{r.json()['2p'][0]}\n**3 Players:**\n{r.json()['3p'][0]}", color=discord.Color.green(), timestamp=datetime.now())
            await interaction.edit_original_response(content=interaction.user.mention,embed=new_embed)

@tree.command(name="status", description="Shows condo's status.")
async def status(interaction: discord.Interaction):
    embed = discord.Embed(title="**STATUS**", description=f"**Loading status...**", color=discord.Color.green(), timestamp=datetime.utcnow())
    await interaction.response.send_message(content=interaction.user.mention,embed=embed)
    await asyncio.sleep(0.4)

    uploaded_embed = discord.Embed(title="**STATUS**", description="\n".join([f"**{x.replace('p', ' Players')}**:\n<:online:1214568509346943026> Online" if data[x][1] else f"**{x.replace('p', ' Players')}**:\n<:offline:1214568523506917436> Offline" for x in data]), color=discord.Color.green(), timestamp=datetime.now())
    await interaction.edit_original_response(embed=uploaded_embed)



client.run('TOKEN')
