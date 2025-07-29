import gspread
import pymongo

# Load Google Sheet
gc = gspread.service_account(filename='credentials.json')
worksheet = gc.open('Your Sheet Name').sheet1
data = worksheet.get_all_records()

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")  # Or use your remote URI
db = client["reminder_bot"]
collection = db["reminders"]

# Insert data into MongoDB
for row in data:
    collection.update_one(
        {"discord_id": row["discord_id"], "task": row["task"]},
        {"$set": row},
        upsert=True
    )

print("Data imported to MongoDB.")