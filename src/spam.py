"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""
import asyncio
from datetime import timedelta
import discord
import db



BOT = None
###########################
# Function: set
# Description: prompts the instructor to set the spam settings
# Inputs:
#      - ctx: the context of the channel we are on
###########################
async def set(ctx):
    if ctx.channel.name == 'instructor-commands':
        # only run in the instructor command channel
        await ctx.send('How many messages should a user be able to send before they are warned '
                       'of spamming?')
        try:
            print("lord...")
            msg = (await BOT.wait_for('message', timeout=60.0, check=lambda x: x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content
            print(f'this is the fucked msg {msg}')
            msg = int(msg)
            print(msg)
            msg_warn_num = msg
        except:
            await ctx.send('Invalid entry. Try again...')
            return

        await ctx.send('How many messages should a user be able to send before they are put in '
                       'timeout?')
        try:
            msg_timeout_num = int((await BOT.wait_for('message', timeout=60.0, check=lambda x:
            x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content)
        except:
            await ctx.send('Invalid entry. Try again...')
            return

        await ctx.send(
            f'How much time should users have to send {msg_warn_num} messages before they will be '
            f'warned '
            f'and then eventually put in timeout?')
        try:
            msg_time_clears = int((await BOT.wait_for('message', timeout=60.0, check=lambda x:
            x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content)
        except:
            await ctx.send('Invalid entry. Try again...')
            return

        await ctx.send('How long should a user be placed in timeout when caught spamming? '
                        'Format: min,hours,days Example: 5,0,0 is 5 minutes')
        try:
            msg_timeout_time = (await BOT.wait_for('message', timeout=60.0, check=lambda x:
            x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content
            timeout_time = msg_timeout_time.split(',')
            minutes = int(timeout_time[0])
            hours = int(timeout_time[1])
            days = int(timeout_time[2])
            timedelta(seconds=0, minutes=minutes, hours=hours, days=days)
        except:
            await ctx.send('Invalid entry. Try again...')
            return
        db.mutation_query(
            'UPDATE spam_settings SET warning_num = ?, timeout_num = ?, timeout_min = ?, '
            'timeout_hour = ?, timeout_day = ?, time_between_clears = ?',
            [msg_warn_num, msg_timeout_num, int(timeout_time[0]), int(timeout_time[1]),
             int(timeout_time[2]), msg_time_clears]
        )
        await ctx.send('Spam settings successfully updated!')
    else:
        await ctx.author.send('`!set_spam_settings` can only be used in the `instructor-commands` '
                              'channel')
        await ctx.message.delete()
###########################
# Function: clear_spam
# Description: run as a constant task that clears the spam.txt file
# Inputs:
#      - None
###########################
async def clear_spam():
    while True:
        rows = db.select_query('SELECT * FROM spam_settings')
        rows_tuple = rows.fetchall()[0]
        time_between_clears = rows_tuple[5]
        # print("We cleared") ## for testing purposes
        await asyncio.sleep(time_between_clears) # uses a set seconds betweeen spam clearing
        with open("spam.txt", "r+", encoding='utf-8') as f:
            f.truncate(0)  # delete the user_id of the last message sent
###########################
# Function: init
# Description: initializes this module, giving it access to discord bot. Also inits the clear
# spam function and
# puts default values in for the spam settings.
# Inputs:
#      - bot: discord bot
# Outputs: None
###########################
def init(bot):
    global BOT
    BOT = bot
    bot.loop.create_task(clear_spam())  # set up a task for the bot to clear out spam from the
    # txt file
    row = db.select_query('SELECT * FROM spam_settings').fetchall()
    if len(row) == 0:
        # there is nothing in the database then put defaults in it
        warning_num = 40  # number of messages before warning of spam
        timeout_num = 50 # number of messages before timeout
        timeout_min = 5  # number of minutes in timeout
        timeout_hour = 0  # hours in timeout
        timeout_day = 0  # days in timout
        time_between_clears = 15
        db.mutation_query(
            'INSERT INTO spam_settings VALUES (?, ?, ?, ?, ?, ?)',
            [warning_num, timeout_num, timeout_min, timeout_hour, timeout_day, time_between_clears]
        )

###########################
# Function: handle_spam
# Description: takes a message and determines whether the author who sent that message is spamming
# or not
# Inputs:
#      - message: the message sent in the channel
#      - ctx: context of the message
#      - guild_id: the id of the guild we are in
# Outputs: None
###########################
async def handle_spam(message, ctx, guild_id):
    print(message.content)
    print(message.author.id)
    count = 0
    with open("spam.txt", "a", encoding='utf-8') as f:
        f.writelines(f"{str(message.author.id)}\n")

    with open("spam.txt", "r+", encoding='utf-8') as f:
        for line in f:
            if line.strip("\n") == str(message.author.id):
                count = count + 1
        rows = db.select_query('SELECT * FROM spam_settings')
        rows_tuple = rows.fetchall()[0]
        warning_num = rows_tuple[0]
        timeout_num = rows_tuple[1]
        if count > timeout_num:
            guild = BOT.get_guild(guild_id)
            member = guild.get_member(message.author.id)
            muted = discord.utils.get(guild.roles, name="Mute")
            # await member.add_roles(muted)
            seconds = 0
            minutes = rows_tuple[2]
            hours = rows_tuple[3]
            days = rows_tuple[4]
            await member.timeout(timedelta(seconds=seconds, minutes=minutes, hours=hours,
                                           days=days))
            await ctx.send(f"{message.author.name} has been muted")  # lets the everyone know who
            # was timed out
            if message.author.bot is False:
                id_query = f"SELECT * FROM rank where user_id=?"
                result = db.select_query(id_query, (message.author.id,))
                result = result.fetchone()
                if result[1] >= 10:
                    update_query = f"UPDATE rank SET experience=? WHERE user_id=?"
                    db.mutation_query(update_query, (result[1]-10, message.author.id))
                elif result[1] < 10 and result[2] >0:
                    update_query = f"UPDATE rank SET experience=?, level=?  WHERE user_id=?"
                    db.mutation_query(update_query, (90+result[1], result[2]-1, message.author.id))
                else:
                    update_query = f"UPDATE rank SET experience=? WHERE user_id=?"
                    db.mutation_query(update_query, (0, message.author.id))

            return True
            
        elif count > warning_num:
            await ctx.send(f"Warning, {message.author.name} will be muted if they continue to spam")
            return False
    return False
