from apscheduler.schedulers.asyncio import AsyncIOScheduler
from button import ReminderView
from datetime import datetime

scheduler = AsyncIOScheduler()

def schedule_all_tasks(bot, tasks):
    for task in tasks:
        try:
            due_time = datetime.strptime(task["due_date"], "%Y-%m-%d %H:%M")
            scheduler.add_job(send_reminder, 'date', run_date=due_time, args=[bot, task])
        except Exception as e:
            print(f"Skipping task due to error: {e}")
    scheduler.start()

async def send_reminder(bot, task):
    user = await bot.fetch_user(int(task["discord_id"]))
    await user.send(
        f"❗ **Reminder**: Your task **{task['task']}** is due!",
        view=ReminderView(task)
    )