from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")  # Replace with your URI
db = client["reminder_bot"]
reminders = db["reminders"]

# Get all reminder tasks
def load_reminders():
    return list(reminders.find({"status": {"$ne": "Done"}}))  # Only pending ones

# Update status when user clicks "Done"
def update_status(discord_id, task_name, new_status):
    reminders.update_one(
        {"discord_id": discord_id, "task": task_name},
        {"$set": {"status": new_status}}
    )

# Update due date when user selects "Reschedule"
def update_due_date(discord_id, task_name, new_due_date):
    reminders.update_one(
        {"discord_id": discord_id, "task": task_name},
        {"$set": {"due_date": new_due_date}}
    )
