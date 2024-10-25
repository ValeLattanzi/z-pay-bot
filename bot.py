import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
API_URL = os.getenv('API_URL')

# Configurar los intents para que el bot pueda gestionar eventos de miembros
intents = discord.Intents.default()
intents.members = True

# Inicializar el bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento cuando el bot esté listo
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Ejemplo de comando que consulta la API
@bot.command(name='status')
async def status(ctx):
    try:
        response = requests.get(f"{API_URL}/status")
        if response.status_code == 200:
            await ctx.send("La API está funcionando correctamente!")
        else:
            await ctx.send("Hubo un problema con la API.")
    except Exception as e:
        await ctx.send(f"Error al conectar con la API: {e}")

# Iniciar el bot
bot.run(TOKEN)
