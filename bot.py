from discord.ext import commands
from scheduler import schedule_all_tasks
from database import load_reminders  

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    reminders = load_reminders() 
    schedule_all_tasks(bot, reminders)  

bot.run("YOUR_BOT_TOKEN")