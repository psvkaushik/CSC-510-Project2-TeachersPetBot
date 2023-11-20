import sqlite3
from prettytable import PrettyTable
import discord
from discord.ext import commands

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

# Intents required by the bot (change based on your requirements)
intents = discord.Intents.default()

# Initialize the Discord bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event to fetch author names from their IDs
@bot.event
async def on_ready():
    try:
        # Fetch data from the 'rank' table and sort it by 'level' in descending order
        cursor.execute("SELECT * FROM rank ORDER BY level DESC")
        rows = cursor.fetchall()

        # Check if there's data in the table
        if not rows:
            print("No data found in the 'rank' table.")
        else:
            # Create a PrettyTable instance
            table = PrettyTable(['SN', 'Username', 'XP', 'Rank'])

            # Add rows to the table with a serial number column
            for index, row in enumerate(rows[:10], start=1):
                user_id = row[1]  # Assuming the ID column holds user IDs
                user = await bot.fetch_user(user_id)
                username = user.name if user else "Unknown User"
                table.add_row([index, username, row[2], row[3]])  # Assuming XP and Rank columns are at indices 2 and 3

            # Print the table
            print(table)

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Close the connection
    conn.close()

# Run the bot
bot.run('MTE3MzcxOTYxMTkwOTM2MTc0NQ.GuAYW0.NVh6mGU1PGqiBKifOy5bgwKS-7X16-k1bZHvzQ')