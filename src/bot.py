"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""

import platform
import asyncio
import os
import re
from time import time
from platform import python_version
from datetime import datetime, timedelta
import json
from psutil import Process, virtual_memory
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from leaderboard_card import draw_leaderboard

import discord
from discord import Embed
from discord.ext import commands
from discord.utils import get
from discord import __version__ as discord_version

from dotenv import load_dotenv

from quickchart import QuickChart
import pyshorteners
from bardapi import Bard
import db
import profanity_custom 
from profanity_help import check_profanity, censor_profanity, custom_words
import event_creation
import office_hours
import email_address
import cal
import qna
import attendance
import help_command
import regrade
import spam
from rank_card import draw_card
from award import award_update_rank_and_xp
from penalize import penalize_update_rank_and_xp

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
		   "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
BOT_VERSION=os.getenv('VERSION')
print(BOT_VERSION)
Test_bot_application_ID = int(os.getenv('TEST_BOT_APP_ID'))
#bard_api_key = os.getenv('BARD_API_KEY', None)
#bard = None
#if bard_api_key:
#    bard = Bard(token = bard_api_key)


guild_id = int(os.getenv('TEST_GUILD_ID'))  ## needed for spam detection

TESTING_MODE = None

intents=discord.Intents.all()
bot = commands.Bot(command_prefix='!', description='This is TeachersPetBot!', intents=intents)
bot.remove_command("help")

cwd = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(cwd, '../data/charts/chartstorage.json')
###########################
# Function: on_ready
# Description: run on bot start-up
###########################
@bot.event
async def on_ready():
    ''' run on bot start-up '''
    global TESTING_MODE
    TESTING_MODE = False
    #DiscordComponents(bot)
    db.connect()
    db.mutation_query('''
        CREATE TABLE IF NOT EXISTS ta_office_hours (
            guild_id    INT,
            ta          VARCHAR(50),
            day         VARCHAR(4),
            begin_time  DATETIME,
            end_time    DATETIME
        )
    ''')
    db.mutation_query('''
        CREATE TABLE IF NOT EXISTS exams (
            guild_id    INT,
            title       VARCHAR(50),
            desc        VARCHAR(300),
            duration    VARCHAR(15),
            begin_date  DATETIME,
            end_date    DATETIME
        )
    ''')
    db.mutation_query('''
        CREATE TABLE IF NOT EXISTS assignments (
            guild_id    INT,
            title       VARCHAR(50),
            link        VARCHAR(300),
            desc        VARCHAR(300),
            date        DATETIME
        )
    ''')
    db.mutation_query('''
        CREATE TABLE IF NOT EXISTS qna (
            guild_id    INT,
            author       VARCHAR(50),
            answer        VARCHAR(300),
            qnumber      INT
        )
    ''')
    db.mutation_query('''
        CREATE TABLE IF NOT EXISTS regrade (
            guild_id    INT,
            name        VARCHAR(50),
            questions   VARCHAR(50)
        )
    ''')
    db.mutation_query('''
        CREATE TABLE IF NOT EXISTS email_address (
            author_id    INT,
            email_id       VARCHAR(50),
            is_active   BOOLEAN NOT NULL CHECK (is_active IN (0, 1))
        )
    ''')
    db.mutation_query('''
        CREATE TABLE IF NOT EXISTS rank (
            user_id     INT NOT NULL UNIQUE ON CONFLICT IGNORE,
            experience  INT DEFAULT 0,
            level       INT DEFAULT 0,
            violation_num     INT DEFAULT 0                     
        )
    ''')
    db.mutation_query('''
            CREATE TABLE IF NOT EXISTS spam_settings (
                warning_num             INT,
                timeout_num             INT,
                timeout_min             INT,
                timeout_hour            INT,
                timeout_day             INT,
                time_between_clears     INT
            )
        ''')
    db.mutation_query('''
            CREATE TABLE IF NOT EXISTS profanity_settings (
                warning_num             INT,
                timeout_num             INT,
                timeout_min             INT,
                timeout_hour            INT,
                timeout_day             INT,
                kicked_out_violations     INT,
                penalty_value           INT
            )
        ''')
    # db.mutation_query('''
    #         CREATE TABLE IF NOT EXISTS explicit_content_violations (
    #             user_id           INT NOT NULL UNIQUE ON CONFLICT IGNORE,
    #             violation_num     INT DEFAULT 0
    #         )
    #     ''')
    event_creation.init(bot)
    office_hours.init(bot)
    spam.init(bot)  #initialize the spam function of the bot so spam.py has
    profanity_custom.init(bot)
    # Get the user list from general
    guild = bot.guilds[0]
    channel_name = 'general'
    general_channel = discord.utils.get(guild.channels, name=channel_name, type=discord.ChannelType.text)
    general_members = general_channel.members
    # Get the general user_ids, make sure the bot is ignored
    general_ids = [i.id for i in general_members if i.bot == False]

    channel_name = 'instructor-commands'
    instructor_channel = discord.utils.get(guild.channels, name=channel_name, type=discord.ChannelType.text)
    instructor_members = instructor_channel.members
    # Get the instructor user_ids, make sure the bot is ignored
    instructor_ids = [i.id for i in instructor_members if i.bot == False]

    for member in general_members:
        blocked = False
        if member.id not in instructor_ids:
            with open("blocked_user.txt", "a+", encoding='utf-8') as f:
                for line in f:
                    if line.strip("\n").split(" ")[0] == str(member.id):
                        await member.kick()
                        channel = get(member.guild.text_channels, name='general')
                        await channel.send(f"A blocked user {member} tried to join the server but was kicked out!! ")
                        blocked = True
                        break
            if blocked == False:
                update_rank_table_query = f"INSERT into rank (user_id, level, experience, violation_num) VALUES(?, ?, ?, ?)"
                db.mutation_query(update_rank_table_query, (member.id, 0, 0, 0))
    
    # for i in range(len(general_ids)):
    #     if general_ids[i] not in instructor_ids:
    #         update_rank_table_query = f"INSERT into rank (user_id, level, experience, violation_num) VALUES(?, ?, ?, ?)"
    #         db.mutation_query(update_rank_table_query, (general_ids[i], 0, 0, 0))
        # else:
        #     update_rank_table_query = f"INSERT into rank (user_id, level, experience) VALUES(?, ?, ?)"
        #     db.mutation_query(update_rank_table_query, (general_ids[i], 0, 0))
        # update_explicit_table_query = f"INSERT into explicit_content_violations (user_id, violation_num) VALUES(?, ?)"
        # db.mutation_query(update_explicit_table_query, (general_ids[i], 0))
    # access to the bot and clearing starts
    print(general_members)
    print("Ranking system initialized!")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await cal.init(bot) ##this needed to be moved below bc otherwise the stuff above is never called
###########################
# Function: on_guild_join
# Description: run when a the bot joins a guild
# Inputs:
#      - guild: the guild the user joined from
###########################
@bot.event
async def on_guild_join(guild):
    ''' run on member joining guild '''
    channel = get(guild.text_channels, name='general')
    if channel is None:
        await guild.create_text_channel('general')
        channel = get(guild.text_channels, name='general')
    if channel.permissions_for(guild.me).send_messages:
        await channel.send('Hi there, I\'m TeachersPetBot, and I\'m here' +
            'to help you manage your class discord! Let\'s do some quick setup.')
        await guild.create_role(name="Instructor", colour=discord.Colour(0x0062ff),
                                    permissions=discord.Permissions.all())
        leadrole = get(guild.roles, name='Instructor')
         #Assign Instructor role to admin is there is no Instructor
        if len(leadrole.members) == 0:
            leader = guild.owner
            leadrole = get(guild.roles, name='Instructor')
            await channel.send(leader.name + " has been given Instructor role!")
            await leader.add_roles(leadrole, reason=None, atomic=True)
        else:
            for member in leadrole.members:
                await member.add_roles(leadrole, reason=None, atomic=True)
            instructors = ", ".join([str(x).rsplit("#", 1)[0] for x in leadrole.members])
            if len(leadrole.members) == 1:
                await channel.send(instructors + " is the Instructor!")
            else:
                await channel.send(instructors + " are the Instructors!")
        await channel.send("To add Instructors, type \"!setInstructor @<member>\"")
        # Initialize ranking system
        for x in guild.members:
            # if x.bot is False: bots must have rank in order to do testing
            insert_query = f"INSERT INTO rank (user_id) VALUES ({x.id})"
            db.mutation_query(insert_query)
        print("Ranking system initialized!")
        await channel.send("Ranking system initialized!")
        #await channel.send("To remove instructors, type \"!removeInstructor @<member>\"")
        #Create Text channels if they don't exist
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False,
            send_messages=False), leadrole: discord.PermissionOverwrite(read_messages=True,
            send_messages=True)}
        if get(guild.text_channels, name='instructor-commands') is None:
            await guild.create_text_channel('instructor-commands', overwrites=overwrites)
            await channel.send("instructor-commands channel has been added!")
        else:
            await channel.send("instructor-commands channel is already present!")
        if get(guild.text_channels, name='q-and-a') is None:
            await guild.create_text_channel('q-and-a')
            await channel.send("q-and-a channel has been added!")
        else:
            await channel.send("q-and-a channel is already present!")
        if get(guild.text_channels, name='course-calendar') is None:
            await guild.create_text_channel('course-calendar')
            await channel.send("course-calendar channel has been added!")
        else:
            await channel.send("course-calendar channel is already present!")
        if get(guild.text_channels, name='regrade-requests') is None:
            await guild.create_text_channel('regrade-requests')
            await channel.send("regrade-requests channel has been added!")
        else:
            await channel.send("regrade-requests channel is already present!")

###########################
# Function: on_member_join
# Description: run when member joins a guild in which bot is alreay present
# Inputs:
#      - member: the user details
###########################
@bot.event
async def on_member_join(member):
    ''' run on guild join '''
    # channel = get(member.guild.text_channels, name='general')
    with open("blocked_user.txt", "r+", encoding='utf-8') as f:
        for line in f:
            if line.strip("\n").split(" ")[0] == str(member.id):
                await member.kick()
                channel = get(member.guild.text_channels, name='general')
                await channel.send(f"A blocked user {member} tried to join the server but was kicked out!! ")
                return

                
    welcome_message = f"Hello {member}! Welcome to {member.guild.name} important links:.\n"
    # Retrieve important links from the 'important-links' channel
    important_links_channel = get(member.guild.text_channels, name='important-links')
    if important_links_channel:
        async for message in important_links_channel.history(limit=10):
            link_match = re.search(r'^(.*?):\s*(https:\/\/[^\s]+)', message.content)
            if link_match:
                link_name, link_url = link_match.group(1), link_match.group(2)
                welcome_message += f"**[{link_name}]({link_url})**\n"
    await member.send(welcome_message)
    channel = get(member.guild.text_channels, name='general')
    insert_query = f"INSERT INTO rank (user_id) VALUES (?)"
    db.mutation_query(insert_query, (member.id,))
    await channel.send(f"Hello {member}! Your rank details are as follows. Level: 0, Experience: 0")
    await member.send(f'You have joined {member.guild.name}!')

###########################
# Function: on_member_remove
# Description: run when member leaves a guild in which bot is alreay present
# Inputs:
#      - guild: the guild the user joined from
###########################
@bot.event
async def on_member_remove(member):
    channel = get(member.guild.text_channels, name='general')
    delete_query = f"DELETE FROM rank where user_id=?"
    db.mutation_query(delete_query, (member.id,))
    await channel.send(f"{member.name} has left")

###########################
# Function: on_message
# Description: run when a message is sent to a discord the bot occupies
# Inputs:
#      - message: the message the user sent to a channel
###########################
@bot.event
async def on_message(message):
    ''' run on message sent to a channel '''
    url_data=[]
    message_links = []
    temp=[]
    ctx = await bot.get_context(message)
    member = message.guild.get_member(message.author.id)
    instructor = False
    for role in member.roles:
        if role.name == 'Instructor':
            instructor = True

    # allow messages from test bot
    # print('message.author.bot: ', message.author.bot)
    # print('message.author.id: ', message.author.id)
    # print('Test_bot_application_ID: ', Test_bot_application_ID)
    if message.author.bot and message.author.id == Test_bot_application_ID:
        ctx = await bot.get_context(message)
        await bot.invoke(ctx)
    #print(f"Meessage author is {message.author.name} and type is {type(message.author)}")
    if message.author == bot.user:
        return

    if not instructor:
        # Only spam detect on non instructors
        is_timeout = await spam.handle_spam(message, ctx, guild_id) # handles spam

    if check_profanity(message.content):
        await message.channel.send(message.author.name + ' says: ' +
            censor_profanity(message.content))
        await message.delete()
        if not instructor:
            await profanity_custom.handle_profanity(message, ctx, guild_id)
    await bot.process_commands(message)

    if message.content == 'hey bot':
        response = 'hey yourself ;)'
        await message.channel.send(response)
    
    instructor_role = discord.utils.get(message.guild.roles, name='Instructor')

    if ctx.channel.name == 'instructor-mentions':
        channel = get(member.guild.text_channels, name='general')
        await channel.send(f'{message.author} :- {message.content}')

    if message.mentions or f'<@&{instructor_role.id}>' in message.content:
        mentioned_users = [user for user in message.mentions]
        instructor_mentions = [user for user in mentioned_users if any(role.name == 'Instructor' for role in user.roles)]
        if instructor_mentions or f'<@&{instructor_role.id}>' in message.content:
            target_guild = bot.get_guild(guild_id)
            if target_guild:
                for channel in target_guild.channels:
                    if channel.name == 'instructor-mentions':
                        await channel.send(f'{message.author} :- {message.content}')
            else:
                print(f"Guild with ID {guild_id} not found.")

    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s" \
            r"()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};" \
            r":'.,<>?«»“”‘’]))"
    url_data = re.findall(regex, message.content)
    for url_count in url_data:
        temp.append(url_count[0])
    if temp:
        message_links.append(message.content)
        with open('images/links/links.txt', mode='a', encoding='utf-8') as text_file:
            text_file.write("Message containing url :-  " + message.content + "\n")
            text_file.close()
    else:
        pass
    # Ranking System
    if message.author.bot is False and not instructor:
        id_query = f"SELECT * FROM rank where user_id=?"
        result = db.select_query(id_query, (message.author.id,))
        result = result.fetchone()
        try:
            if result[1] == 99:
                await message.channel.send(
                    f"{message.author.mention} has advanced to level {result[2]+1}!"
                )
                update_query = f"UPDATE rank SET experience=0, level=?  WHERE user_id=?"
                db.mutation_query(update_query, (result[2]+1, message.author.id))
            else:
                update_query = f"UPDATE rank SET experience=? WHERE user_id=?"
                db.mutation_query(update_query, (result[1]+1, message.author.id))
        except Exception as error:
            print(" the error is : ", error)
            # write_query = f"INSERT into rank (user_id, level, experience) VALUES(?, ?, ?)"
            # if instructor:
            #     db.mutation_query(write_query, (message.author.id, 100, 0))
            # else:
            #     db.mutation_query(write_query, (message.author.id, 0, 0))

###########################
# Function: on_message_edit
# Description: run when a user edits a message
# Inputs:
#      - before: the old message
#      - after: the new message
###########################
@bot.event
async def on_message_edit(before, after):
    ''' run on message edited '''
    ctx = await bot.get_context(after)
    member = after.guild.get_member(after.author.id)
    instructor = False
    for role in member.roles:
        if role.name == 'Instructor':
            instructor = True
    if check_profanity(after.content):
        await after.channel.send(after.author.name + ' says: ' +
            censor_profanity(after.content))
        await after.delete()
        if not instructor:
            await profanity_custom.handle_profanity(after, ctx, guild_id)
    await bot.process_commands(after)

###########################
# Function: test
# Description: Simple test command that shows commands are working.
# Inputs:
#      - ctx: context of the command
# Outputs:
#      - Sends test successful message back to channel that called test
###########################
@bot.command()
async def test(ctx):
    ''' simple sanity check '''
    await ctx.send('test successful')

##################################
#Function : bard enabled
# Description: Integrating bard api
##################################
@bot.command()
async def Aichat(ctx):
    bard_api_key = os.getenv('BARD_API_KEY', None)
    bard = None
    if bard_api_key:
        bard = Bard(token = bard_api_key)
    await ctx.send("You are now in a AI chat session."
                    "Type 'exit' to end the chat.")
    def check(msg):
        return msg.author == ctx.author
    while True:
        try:
            user_input = await bot.wait_for("message", check=check, timeout=300)
            if user_input.content.lower() == 'exit':
                await ctx.send("Chat session ended.")
                break
            if bard:
                chat_reply = bard.get_answer(str(user_input.content))['content']
                await ctx.send(chat_reply)
            else:
                await ctx.send("Bard API is not available.")
        except asyncio.TimeoutError:
            await ctx.send("Chat session timed out. Type `!chat` to start a new session.")
            break
###########################
# Function: get_rank
# Description: Command used to get level and experience
# Inputs:
#      - ctx: context of the command
#      - member: user to whose rank is to be printed
# Outputs:
#      - Sends information back to channel
###########################
@bot.command(name='rank', help='Get rank of user')
async def get_rank(ctx, member_id=None):
    query = "SELECT * FROM rank where user_id=?"
    rank_query = "SELECT p1.*, (SELECT COUNT(*) FROM rank AS p2 WHERE p2.level < p1.level) AS \
    level_rank FROM rank AS p1 WHERE p1.user_id=?"
    # Get your own rank
    if member_id is None:
        result = db.select_query(query, (ctx.author.id,))
        rank_result = db.select_query(rank_query, (ctx.author.id,))
        result = result.fetchone()
        rank = rank_result.fetchone()
        card = await draw_card(
            xp=result[1],
            level=result[2],
            rank=rank[3],
            name=ctx.author.name,
            image_url=ctx.author.display_avatar,
            next_level_xp=100,
        )
        file = discord.File(card, filename="levelcard.png")
        await ctx.channel.send(file=file)
    # Get some other users rank
    else:
        try:
            member = ctx.guild.get_member(int(member_id[2:-1]))
            result = db.select_query(query, (member.id,))
            rank_result = db.select_query(rank_query, (member.id,))
            result = result.fetchone()
            rank = rank_result.fetchone()
            card = await draw_card(
                xp=result[1],
                level=result[2],
                rank=rank[3],
                name=member.name,
                image_url=member.display_avatar,
                next_level_xp=100,
            )
            file = discord.File(card, filename="levelcard.png")
            await ctx.channel.send(file=file)
        except Exception as e:
            await ctx.channel.send(f"No {member_id} in the database")
####get leaderboard####
@bot.command(name='leaderboard', help='Display leaderboard')
async def display_leaderboard(ctx):
    ##conn = sqlite3.connect('C:\\Users\\vaivi\\CSC-510-Project2-TeachersPetBotv2.0\\db.sqlite')
    ##cursor = conn.cursor()
    #cursor.execute("SELECT * FROM rank ORDER BY level DESC, experience DESC LIMIT 10")
    # rows = cursor.fetchall()
    query = "SELECT * FROM rank ORDER BY level DESC, experience DESC LIMIT 10"
    result = db.select_query(query)
    rows = result.fetchall()
    if not rows:
        await ctx.send("No data found in the 'rank' table.")
    else:
        users = []
        for index, row in enumerate(rows, start=1):
            user_id = row[0]
            user = await bot.fetch_user(user_id)
            username = user.name if user else "Unknown User"
            user_data = {
                'name': username,
                'xp': row[1],
                'level': row[2],
                'image_url': user.avatar.url if user.avatar else user.default_avatar.url,
            }
            users.append(user_data)
        leaderboard_image = await draw_leaderboard(users)
        file = discord.File(leaderboard_image, filename="leaderboard.png")
        await ctx.send(file=file)
###########################
# Function: get_instructor
# Description: Command used to give Instructor role out by instructors
# Inputs:
#      - ctx: context of the command
#      - member: user to give role
# Outputs:
#      - Sends confirmation back to channel
###########################
@bot.command(name='getInstructor', help='Find Instructors')
async def get_instructor(ctx):
    ''' set instructor role command '''
    leadrole = get(ctx.guild.roles, name='Instructor')
    instructors = ", ".join([str(x).rsplit("#", 1)[0] for x in leadrole.members])
    if len(leadrole.members) == 1:
        await ctx.send(instructors + " is the Instructor!")
    else:
        await ctx.send(instructors + " are the Instructors!")
###########################
# Function: set_instructor
# Description: Command used to give Instructor role out by instructors
# Inputs:
#      - ctx: context of the command
#      - member: user to give role
# Outputs:
#      - Sends confirmation back to channel
###########################
@bot.command(name='setInstructor', help='Set member to Instructor.')
@commands.has_role('Instructor')
async def set_instructor(ctx, member:discord.Member):
    ''' set instructor role command '''
    if ctx.channel.name == 'instructor-commands':
        irole = get(ctx.guild.roles, name='Instructor')
        if irole in member.roles:
            await ctx.channel.send(member.name + " is already an Instructor!")
        else:
            await member.add_roles(irole, reason=None, atomic=True)
            await ctx.channel.send(member.name + " has been given Instructor role!")
            channel = get(ctx.guild.text_channels, name='instructor-commands')
            await channel.set_permissions(member, read_messages=True,
            send_messages=True,read_message_history=False)
    else:
        await ctx.channel.send('Not a valid command for this channel')
###########################
# Function: remove_instructor
# Description: Command used to remove a user from Instructor role by instructors
# Inputs:
#      - ctx: context of the command
#      - member: user to remove role
# Outputs:
#      - Sends confirmation back to channel
###########################
@bot.command(name='removeInstructor', help='Remove member from Instructor.')
@commands.has_role('Instructor')
async def remove_instructor(ctx, member:discord.Member):
    ''' remove instructor role command '''
    if ctx.channel.name == 'instructor-commands':
        irole = get(ctx.guild.roles, name='Instructor')
        if irole not in member.roles:
            await ctx.channel.send(member.name + " is not an Instructor!")
        else:
            await member.remove_roles(irole, reason=None, atomic=True)
            await ctx.channel.send(member.name + " has been removed from Instructor role!")
            channel = get(ctx.guild.text_channels, name='instructor-commands')
            await channel.set_permissions(member, overwrite=None)
    else:
        await ctx.channel.send('Not a valid command for this channel')

###########################
# Function: unblock_user
# Description: Command used to unblock a user from joining the channel by instructors
# Inputs:
#      - ctx: context of the command
#      - member: user to remove role
# Outputs:
#      - Sends confirmation back to channel
###########################
@bot.command(name='unblockUser', help='Unblock user from joining the channel.')
@commands.has_role('Instructor')
async def unblock_user(ctx):
    ''' unblock user by instructor command '''
    if ctx.channel.name == 'instructor-commands':
        await ctx.send('Which user do you want to unblock?')
        userid_to_unblock = str((await bot.wait_for('message', timeout=60.0, check=lambda x:
            x.channel.name ==
                'instructor-commands' and x.author.id != bot.user.id)).content)
        with open("blocked_user.txt", "r", encoding='utf-8') as f:
            lines = f.readlines()
        updated_lines = [line.strip() for line in lines if line.strip().split(' ')[1] != userid_to_unblock]
        with open("blocked_user.txt", "w", encoding='utf-8') as f:
            f.write('\n'.join(updated_lines))
        if len(lines) != len(updated_lines):
            await ctx.send(f'The user {userid_to_unblock} got unblocked!!!')
        else:
            await ctx.send(f'The user {userid_to_unblock} is not blocked in the forst place!!!')
    else:
        await ctx.channel.send('Not a valid command for this channel')


###########################
# Function: create_event
# Description: command to create event and send to event_creation module
# Ensures command author is Instructor
# Inputs:
#      - ctx: context of the command
# Outputs:
#      - Options to create event
###########################
@bot.command(name='create', help='Create a new event.')
# @commands.dm_only()
@commands.has_role('Instructor')
async def create_event(ctx):
    ''' run event creation interface '''
    await event_creation.create_event(ctx, TESTING_MODE)
###########################
# Function: create_event
# Description: command to create event and send to event_creation module
# Ensures command author is Instructor
# Inputs:
#      - ctx: context of the command
# Outputs:
#      - Options to create event
###########################
@bot.command(name='set_spam_settings', help='Allows instructor to set spam settings')
@commands.has_role('Instructor')
async def set_spam_settings(ctx):
    ''' run spam setting prompts '''
    await spam.set(ctx)
###########################
# Function: oh
# Description: command related office hour and send to office_hours module
# Inputs:
#      - ctx: context of the command
#      - command: specific command to run
#      - *args: arguments for command
# Outputs:
#      - Office hour details and options
###########################
@bot.command(name='oh', help='Operations relevant for office hours.')
async def office_hour_command(ctx, command, *args):
    ''' run office hour commands with various args '''
    await office_hours.office_hour_command(ctx, command, *args)
###########################
# Function: ask
# Description: command to ask question and sends to qna module
# Inputs:
#      - ctx: context of the command
#      - question: question text
# Outputs:
#      - User question in new post
###########################
@bot.command(name='ask', help='Ask question. Please put question text in quotes.')
async def ask_question(ctx, question):
    print("Bot asked a question?")
    ''' ask question command '''
    # make sure to check that this is actually being asked in the Q&A channel
    if ctx.channel.name == 'q-and-a':
        await qna.question(ctx, question)
    else:
        await ctx.author.send('Please send questions to the #q-and-a channel.')
        await ctx.message.delete()
###########################
# Function: send_links
# Description: command to fetch all the links posted in the group
# Inputs:
#      - ctx: context of the command
# Outputs:
#      - Bot posts all the links posted in group.
###########################
@bot.command(name='send_links', help='Command will output all the messages which contain url')
async def send_links(ctx):
    """To display all messages which contain url."""
    await ctx.send("The below list of messages contains URLs")
    await ctx.send(file=discord.File('images/links/links.txt'))


###########################
# Function: send_links
# Description: command to fetch all the links posted in the group
# Inputs:
#      - ctx: context of the command
# Outputs:
#      - Bot posts all the links posted in group.
###########################
@bot.command(name='set_profanity_settings', help='Allows instructor to set profanity settings')
@commands.has_role('Instructor')
async def set_profanity_settings(ctx):
    ''' run spam setting prompts '''
    await profanity_custom.set(ctx)
###########################
# Function: answer
# Description: command to answer question and sends to qna module
# Inputs:
#      - ctx: context of the command
#      - q_num: question number to answer
#      - answer: answer text
# Outputs:
#      - User answer in question post
###########################
@bot.command(name='answer', help='Answer specific question. Please put answer text in quotes.')
async def answer_question(ctx, q_num, answer):
    ''' answer question command '''
    # make sure to check that this is actually being answered in the Q&A channel
    if ctx.channel.name == 'q-and-a':
        await qna.answer(ctx, q_num, answer)
    else:
        await ctx.author.send('Please send answers to the #q-and-a channel.')
        await ctx.message.delete()
@bot.command(name='regrade-request', help='add regrade-request')
async def submit_regrade_request(ctx,name:str,questions:str):
    """
        Function: submit_regrade_request
        Description: command to add a regrade request
        Inputs:
            - ctx: context of function activation
            - name: name of the student
            - questions: question numbers to be regraded
        Outputs:
            - adds the regrade request to the database
    """
    if ctx.channel.name == 'regrade-requests':
        await regrade.add_request(ctx,name,questions)
    else:
        await ctx.author.send('Please submit requests in regrade channel.')
        await ctx.message.delete()
@submit_regrade_request.error
async def submit_regrade_request_error(ctx, error):
    """
        this handles errors related to the submit_regrade command
    """
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Invalid command.\n '\
        'Use !regrade-request <StudentName> <question numbers> \n \
        ( Example: !regrade-request "Student 1" q1,q2,q3 )')

@bot.command(name='display-requests', help='displays existing regrade-requests')
async def display_regrade_request(ctx):

    """
        Function: display_regrade_request
        Description: command to display all the regrade requests
        Inputs:
            - ctx: context of function activation
        Outputs:
            - displays regrade requests present in the database
    """
    if ctx.channel.name == 'regrade-requests':
        await regrade.display_requests(ctx)
    else:
        await ctx.author.send('Please submit requests in regrade channel.')
        await ctx.message.delete()
@bot.command(name='update-request', help='update regrade request')
async def update_regrade_request(ctx,name:str,questions:str):
    """
        Function: update_regrade_request
        Description: command to display all the regrade requests
        Inputs:
            - ctx: context of function activation
        Output:
            - updates an existing regrade request with any modifications
    """
    if ctx.channel.name == 'regrade-requests':
        await regrade.update_regrade_request(ctx,name,questions)
    else:
        await ctx.author.send('Please submit requests in regrade channel.')
        await ctx.message.delete()
@update_regrade_request.error
async def update_regrade_request_error(ctx, error):
    """
        this handles errors related to the update_request command
    """
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Invalid command.\n Use !update-request <StudentName> <question numbers> \n \
        ( Example: !update-request "Student 1" q1,q2,q3 )')
@bot.command(name='remove-request', help='remove regrade request')
async def remove_regrade_request(ctx,name:str,questions:str):
    """
        Function: remove_regrade_request
        Description: command to remove a regrade request
        Inputs:
            - ctx: context of function activation
            - name: name of the student
            - questions: question numbers to be regraded
            - output: removes an existing regrade request from the database
    """
    if ctx.channel.name == 'regrade-requests':
        await regrade.remove_regrade_request(ctx,name,questions)
    else:
        await ctx.author.send('Please submit requests in regrade channel.')
        await ctx.message.delete()
@remove_regrade_request.error
async def remove_regrade_request_error(ctx, error):
    """
        this handles errors related to the remove regrade command
    """
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Invalid command.\n Use !remove-request <StudentName> <question numbers> \n \
        ( Example: !remove-request "Student 1" q1,q2,q3 )')
###########################
# Function: ping
# Description: Shows latency for debugging
###########################
@bot.command(name='ping', help='Returns Latency')
async def ping(ctx):
    start=time()
    message=await ctx.send(f"Pong! : {bot.latency*1000:,.0f} ms")
    end=time()
    await message.edit(content="Pong! : "+str(int(bot.latency*1000))+" ms."+
    " Response time : "+str(int((end-start)*1000))+" ms.")
@bot.command(name='chart', help='Creates a custom chart')
@commands.has_role('Instructor')
async def custom_chart(ctx, title: str, chart: str, *args):
    """
        Creates a custom chart with given specs
        Parameters:
            ctx: used to access the values passed through the current context.
            title: the name of the chart
            chart: the type of the chart
            *args: a list of data labels and data numbers for each label
        Returns:
            returns a graph in the chat box
    """
    if len(args) % 2 != 0:
        print("Make sure every data-label singularly matches a datapoint (A B C 1 2 3")
        return
    data_count = int(len(args) / 2)
    with open(file_path, 'r', encoding='utf-8') as file:
        storage = json.load(file)
    labels_list = []
    dataset_list = []
    for data_label in range(data_count):
        labels_list.append(args[data_label])
        print(args[data_label])
    for data_point in range(data_count, len(args)):
        dataset_list.append(args[data_point])
        print(args[data_point])
    quick_chart = QuickChart()
    quick_chart.width = 500
    quick_chart.height = 300
    quick_chart.device_pixel_ratio = 2.0
    quick_chart.config = {
        "type": f"{chart}",
        "data": {
            "labels": labels_list,
            "datasets": [{
                "label": f"{title}",
                "data": dataset_list
            }]
        }
    }
    link = quick_chart.get_url()
    shortener = pyshorteners.Shortener()
    shortened_link = shortener.tinyurl.short(link)
    await update_chart(storage, title, shortened_link)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(storage, file, indent=4)
    await ctx.send("Here is your chart:")
    await ctx.send(f"{shortened_link}")
@bot.command(name='check_chart', help='View a custom chart by giving title name')
async def checkchart(ctx, name: str):
    """
        Lets students check the a custom chart
        Parameters:
            ctx: used to access the values passed through the current context.
            name: the name of the chart they are looking for
        Returns:
            returns the custom chart in the chat box if it exists
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        storage = json.load(file)
        if not storage or storage[name] == '':
            await ctx.send("No chart with that name!")
        else:
            await ctx.send(f"Your requested chart:")
            await ctx.send(f"{storage[name]['URL']}")
async def update_chart(storage, name, link):
    """
        Updates the URL of the chart
        Parameters:
            storage: the json file
            name: the name of the chart
            link: the link to the chart
    """
    if not str(name) in storage:
        storage[str(name)] = {}
    storage[str(name)]['URL'] = link
###########################
# Function: stats
# Description: Shows stats like
###########################
@bot.command(name='stats', help='shows bot stats')
async def show_stats(ctx):
    embed = Embed(title="Bot stats",colour=ctx.author.colour, timestamp=datetime.utcnow())
    proc = Process()
    with proc.oneshot():
        uptime = timedelta(seconds=time()-proc.create_time())
        cpu_time = timedelta(seconds=(cpu := proc.cpu_times()).system + cpu.user)
        mem_total = virtual_memory().total / (1024**2)
        mem_of_total = proc.memory_percent()
        mem_usage = mem_total * (mem_of_total / 100)
    fields = [
        ("Bot version", BOT_VERSION, True),
        ("Python version", python_version(), True),
        ("discord.py version", discord_version, True),
        ("Uptime", uptime, True),
        ("CPU time", cpu_time, True),
        ("Memory usage", f"{mem_usage:,.3f} / {mem_total:,.0f} MiB ({mem_of_total:.0f}%)", True),
        ("Users", f"{ctx.guild.member_count:,}", True)
    ]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    await ctx.send(embed=embed)
###########################
# Function: poll
# Description: Poll functionality for  administrators
# Inputs:
#      - ctx: context of the command
#      - minutes: minutes in integer
#      - question: Enter the topic on which the poll is created
#      - options: options for poll
# Outputs:
#      - Poll in discord channel. results after the specified time.
###########################
polls=[]
scheduler = AsyncIOScheduler()
@bot.command(name='poll', help='Set Poll for a specified time and topic.')
@commands.has_role('Instructor')
async def create_poll(ctx, hours: int, question: str, *options):
    if len(options) > 10:
        await ctx.send("You can only supply a maximum of 10 options.")
    else:
        embed = Embed(title="Poll ‼",description=question,colour=ctx.author.colour,
            timestamp=datetime.utcnow())
        fields = [("Options", "\n".join([f"{numbers[idx]} {option}" for idx,
        option in enumerate(options)]), False),
        ("Instructions", "React to cast a vote!", False),
        ("Duration","The Voting will end in "+str(hours)+" Minutes",False)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        message = await ctx.send(embed=embed)
        for emoji in numbers[:len(options)]:
            await message.add_reaction(emoji)
        polls.append((message.channel.id, message.id))
        scheduler.add_job(complete_poll, "interval",
        minutes=hours,args=(message.channel.id, message.id))
        scheduler.start()
async def complete_poll(channel_id, message_id):
    message = await bot.get_channel(channel_id).fetch_message(message_id)
    most_voted = max(message.reactions, key=lambda r: r.count)
    await message.channel.send("The results are in and option "+most_voted.emoji+
    " was the most popular with "+str(most_voted.count-1)+" votes!")
    polls.remove((message.channel.id, message.id))
    scheduler.shutdown()
@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id in (poll[1] for poll in polls):
        message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
        for reaction in message.reactions:
            if (not payload.member.bot
                and payload.member in await reaction.users().flatten()
                and reaction.emoji != payload.emoji.name):
                await message.remove_reaction(reaction.emoji, payload.member)
###########################
# Function: custom-profanity
# Description: Define a word to be added to the profanity filter
# Inputs:
#      - ctx: context of the command
###########################
@bot.command(name = 'custom', help = 'Add word to profanity filter')
async def custom_profanity(ctx, pword):
    ''' adding custom word to profanity list '''
    custom_words.append(pword)
    await ctx.message.delete()
###########################
# Function: attendance
# Description: Gets the attendance when requested by the instructor for audio channel
# Inputs:
#      - ctx: context of the command
###########################
@bot.command(name='attendance', help='Gets the attendance of voice channel')
@commands.has_role('Instructor')
async def attend(ctx):
    await attendance.compute(bot, ctx)
@bot.command(name='create_email', help='Configures the specified email address against user.')
async def create_email(ctx, email_id):
    await email_address.create_email(ctx, email_id)
@bot.command(name='update_email', help='Updates the configured email address against user.')
async def update_email(ctx, email_id):
    await email_address.update_email(ctx, email_id)
@bot.command(name='view_email', help='displays the configured email address against user.')
async def view_email(ctx):
    await email_address.view_email(ctx)
@bot.command(name='remove_email', help='deletes the configured email address against user.')
async def delete_email(ctx):
    await email_address.delete_email(ctx)
###########################
# Function: help
# Description: Describes the help
# Inputs:
#      - ctx: context of the command
###########################
@bot.group(name='help', invoke_without_command=True)
async def custom_help(ctx):
    await help_command.helper(ctx)
@custom_help.command('answer')
async def custom_answer(ctx):
    await help_command.answer(ctx)
@custom_help.command('ask')
async def custom_ask(ctx):
    await help_command.ask(ctx)
@custom_help.command('attendance')
async def custom_attendance(ctx):
    await help_command.attendance(ctx)
@custom_help.command('begin-tests')
async def custom_begin_tests(ctx):
    await help_command.begin_tests(ctx)
@custom_help.command('create')
async def custom_create(ctx):
    await help_command.create(ctx)
@custom_help.command('end-tests')
async def custom_end_tests(ctx):
    await help_command.end_tests(ctx)
@custom_help.command('oh')
async def custom_oh(ctx):
    await help_command.oh(ctx)
@custom_help.command('ping')
async def custom_ping(ctx):
    await help_command.ping(ctx)
@custom_help.command('poll')
async def custom_poll(ctx):
    await help_command.poll(ctx)
@custom_help.command('setInstructor')
async def custom_setInstructor(ctx):
    await help_command.setInstructor(ctx)
@custom_help.command('stats')
async def custom_stats(ctx):
    await help_command.stats(ctx)
@custom_help.command('test')
async def custom_test(ctx):
    await help_command.test(ctx)
@custom_help.command('regrade-request')
async def custom_regrade_request(ctx):
    await help_command.regrade_request(ctx)
@custom_help.command('update-request')
async def custom_update_request(ctx):
    await help_command.update_request(ctx)
@custom_help.command('display-requests')
async def custom_display_requests(ctx):
    await help_command.display_requests(ctx)
@custom_help.command('remove-request')
async def custom_remove_request(ctx):
    await help_command.remove_request(ctx)
@custom_help.command('create_email')
async def custom_create_email(ctx):
    await help_command.create_email(ctx)
@custom_help.command('update_email')
async def custom_update_email(ctx):
    await help_command.update_email(ctx)
@custom_help.command('remove_email')
async def custom_remove_email(ctx):
    await help_command.remove_email(ctx)
@custom_help.command('view_email')
async def custom_view_email(ctx):
    await help_command.view_email(ctx)
###########################
# Function: begin_tests
# Description: Start the automated testing
# Inputs:
#      - ctx: context of the command
###########################
@bot.command('begin-tests')
async def begin_tests(ctx):
    ''' start test command '''
    global TESTING_MODE
    if ctx.author.id != Test_bot_application_ID:
        return
    TESTING_MODE = True
    test_oh_chan = next((ch for ch in ctx.guild.text_channels
        if 'office-hour-test' in ch.name), None)
    if test_oh_chan:
        await office_hours.close_oh(ctx.guild, 'test')
    await office_hours.open_oh(ctx.guild, 'test')
###########################
# Function: end_tests
# Description: Finalize automated testing
# Inputs:
#      - ctx: context of the command
###########################
@bot.command('end-tests')
async def end_tests(ctx):
    ''' end tests command '''
    if ctx.author.id != Test_bot_application_ID:
        return
    await office_hours.close_oh(ctx.guild, 'test')
    # TODO maybe use ctx.bot.logout()
    await ctx.bot.close()
    # quit(0)

###########################
# Function: award
# Description: Award a worthy member with XP points as an instructor. 
# Inputs:
#      - ctx: context of the command
###########################
@bot.command(name='award', help='Award a bright member.')
@commands.has_role('Instructor')
async def award_member(ctx, member, points):
    ''' award member command '''
    guild = bot.get_guild(guild_id)
    channel_name = 'general'
    general_channel = discord.utils.get(guild.channels, name=channel_name, type=discord.ChannelType.text)
    general_members = general_channel.members
    if ctx.channel.name == 'instructor-commands':
        username_to_award = member
        userid_to_award = None
        for member in general_members:
            if member.name == username_to_award:
                userid_to_award= member.id
                
        if not userid_to_award:
            await ctx.send('Invalid username. Try again...')
            return
                
        id_query = f"SELECT * FROM rank where user_id=?"
        result = db.select_query(id_query, (userid_to_award,))
        result = result.fetchone()
        try:
            points = int(points)
        except:
            await ctx.send('Invalid points argument. Try again...')
            return
        await ctx.channel.send(f'The previous rank for {username_to_award} is {result[2]} and XP is {result[1]}')
        new_rank, new_xp = award_update_rank_and_xp(int(result[2]),int(result[1]), points)
        await ctx.channel.send(f'The new rank for {username_to_award} is {new_rank} and XP is {new_xp}')
        update_query = f"UPDATE rank SET experience=?, level=?  WHERE user_id=?"
        db.mutation_query(update_query, (new_xp, new_rank, userid_to_award))
        
    else:
        await ctx.channel.send('Not a valid command for this channel')  

###########################
# Function: penalize
# Description: Penalize a not-so-worthy member with XP points as an instructor. 
# Inputs:
#      - ctx: context of the command
###########################
@bot.command(name='penalize', help='Penalize a not-so-bright member.')
@commands.has_role('Instructor')
async def penalize_member(ctx, member, points):
    ''' penalize member command '''
    guild = bot.get_guild(guild_id)
    channel_name = 'general'
    general_channel = discord.utils.get(guild.channels, name=channel_name, type=discord.ChannelType.text)
    general_members = general_channel.members
    if ctx.channel.name == 'instructor-commands':
        username_to_penalize = member
        userid_to_penalize = None
        for member in general_members:
            if member.name == username_to_penalize:
                userid_to_penalize= member.id
                
        if not userid_to_penalize:
            await ctx.send('Invalid username. Try again...')
            return
                
        id_query = f"SELECT * FROM rank where user_id=?"
        result = db.select_query(id_query, (userid_to_penalize,))
        result = result.fetchone()
        try:
            points = int(points)
        except:
            await ctx.send('Invalid points argument. Try again...')
            return
        await ctx.channel.send(f'The previous rank for {username_to_penalize} is {result[2]} and XP is {result[1]}')
        new_rank, new_xp = penalize_update_rank_and_xp(int(result[2]),int(result[1]), points)
        await ctx.channel.send(f'The new rank for {username_to_penalize} is {new_rank} and XP is {new_xp}')
        update_query = f"UPDATE rank SET experience=?, level=?  WHERE user_id=?"
        db.mutation_query(update_query, (new_xp, new_rank, userid_to_penalize))
        
    else:
        await ctx.channel.send('Not a valid command for this channel')

if __name__ == '__main__':
    bot.run(TOKEN)
###########################
# Function: test_dummy
# Description: Run the bot
###########################
def test_dummy():
    ''' run bot command '''
    bot.run(TOKEN)

