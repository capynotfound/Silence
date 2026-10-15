import discord
from discord import app_commands
import random
import aiohttp
from discord import app_commands 

def register_slash_commands(bot):
    @bot.tree.command(name="oi", description="O bot te cumprimenta!")
    async def oi_slash(interaction: discord.Interaction):
        await interaction.response.send_message(f"Olá, {interaction.user.mention}!")

    @bot.tree.command(name="tiger", description="Envia a imagem da Tiger")
    async def tiger_slash(interaction: discord.Interaction):
        await interaction.response.send_message("https://www.flamesofwar.com/Portals/0/all_images/Briefings/NorthAfrica/Tunisian-Tigers-01.jpg")

    @bot.tree.command(name="gaymeter", description="Mede a porcentagem de gayzisse")
    async def gaymeter_slash(interaction: discord.Interaction):
        await interaction.response.send_message(f"O {interaction.user.mention} é {random.randint(0, 100)}% gay.")

    @bot.tree.command(name="pergunta", description="Faz uma pergunta de sim ou não")
    async def pergunta_slash(interaction: discord.Interaction):
        await interaction.response.send_message(random.choice(['sim', 'não', 'talvez']))

    @bot.tree.command(name="sync", description="Sincroniza os comandos slash (Apenas Adm)")
    async def sync_slash(interaction: discord.Interaction):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("Sem permissão.", ephemeral=True)
            return
        await bot.tree.sync()
        await interaction.response.send_message("Comandos sincronizados!")

    @bot.tree.command(name="help", description="Mostra os comandos disponíveis")
    async def help_slash(interaction: discord.Interaction):
        await interaction.response.send_message("Use .help para ver a lista completa de comandos de prefixo e / para os slash!")

    @bot.tree.command(name="ban", description="Bane um usuário do servidor (Apenas Adm)")
    @app_commands.describe(member="O usuário a ser banido", motivo="O motivo do banimento")
    async def ban_slash(interaction: discord.Interaction, member: discord.Member, motivo: str = None):
        bot_member = interaction.guild.me
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message("Sem permissão.", ephemeral=True)
            return
        if not bot_member.guild_permissions.ban_members or member == interaction.guild.owner or member.top_role >= bot_member.top_role:
            await interaction.response.send_message("Não tenho permissão ou hierarquia para banir este usuário.", ephemeral=True)
            return
        try:
            await member.ban(reason=motivo)
            await interaction.response.send_message(f"{member} foi banido.")
        except discord.Forbidden:
            await interaction.response.send_message("Erro de permissão do Discord.", ephemeral=True)
    @bot.tree.command(name="kick", description="Expulsa um usuário do servidor (Apenas Adm)")
    @app_commands.describe(member="O usuário a ser expulso", motivo="O motivo da expulsão")
    async def kick_slash(interaction: discord.Interaction, member: discord.Member, motivo: str = None):
        bot_member = interaction.guild.me
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message("Sem permissão.", ephemeral=True)
            return
        if not bot_member.guild_permissions.kick_members or member == interaction.guild.owner or member.top_role >= bot_member.top_role:
            await interaction.response.send_message("Não tenho permissão ou hierarquia para expulsar este usuário.", ephemeral=True)
            return
        try:
            await member.kick(reason=motivo)
            await interaction.response.send_message(f"{member} foi expulso.")
        except discord.Forbidden:
            await interaction.response.send_message("Erro de permissão do Discord.", ephemeral=True)