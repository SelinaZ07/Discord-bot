import discord
from database import update_status, update_due_date

class ReminderView(discord.ui.View):
    """This class contains all the UI with the chatbot"""
    def __init__(self, task):
        super().__init__(timeout=None)
        self.task = task

    #The first button: task finished
    @discord.ui.button(label="Done", style=discord.ButtonStyle.success)
    async def done(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Task marked as done!")
        update_status(self.task["discord_id"], self.task["task"], "Done")

    #The second button: new due date
    @discord.ui.button(label="New Due Date", style=discord.ButtonStyle.secondary)
    async def reschedule(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Enter the new due date (YYYY-MM-DD HH:MM):")
        
        #Wait for response and update the sheet
        def check(m): return m.author.id == interaction.user.id
        msg = await interaction.client.wait_for("message", check=check)
        update_due_date(self.task["discord_id"], self.task["task"], msg.content)
        await interaction.followup.send("Due date updated.")