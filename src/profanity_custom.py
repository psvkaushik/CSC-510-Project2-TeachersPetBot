import asyncio
from datetime import timedelta
import discord
import db


BOT = None
###########################
# Function: set
# Description: prompts the instructor to set the profanity settings
# Inputs:
#      - ctx: the context of the channel we are on
###########################
async def set(ctx):
    if ctx.channel.name == 'instructor-commands':
        # only run in the instructor command channel
        await ctx.send('How many messages should a user be able to send before they are muted due '
                       'usage of profanity?')
        try:
            msg = (await BOT.wait_for('message', timeout=60.0, check=lambda x: x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content
            msg = int(msg)
            msg_warn_num = msg
        except:
            await ctx.send('Invalid entry. Try again...')
            return

        await ctx.send('How many messages containing profanity should a user be able to send before they are put in '
                       'timeout?')
        try:
            msg_timeout_num = int((await BOT.wait_for('message', timeout=60.0, check=lambda x:
            x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content)
        except:
            await ctx.send('Invalid entry. Try again...')
            return
        await ctx.send('How much penalty should a person get on the first two messages containing profanity')
        try:
            penalty_value = int((await BOT.wait_for('message', timeout=60.0, check=lambda x:
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
        
        await ctx.send('How many messages containing profanity should a user be able to send before they are'
                       'kicked out?')
        try:
            msg_kicked_num = int((await BOT.wait_for('message', timeout=60.0, check=lambda x:
            x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content)
        except:
            await ctx.send('Invalid entry. Try again...')
            return

        db.mutation_query(
            'UPDATE profanity_settings SET warning_num = ?, timeout_num = ?, timeout_min = ?, '
            'timeout_hour = ?, timeout_day = ?, time_between_clears = ?, penalty_value = ?',
            [msg_warn_num, msg_timeout_num, int(timeout_time[0]), int(timeout_time[1]),
             int(timeout_time[2]), msg_kicked_num, penalty_value]
        )
        await ctx.send('Profanity Settings successfully updated!')
    else:
        await ctx.author.send('`!set_profanity_settings` can only be used in the `instructor-commands` '
                              'channel')
        await ctx.message.delete()
###########################
# Function: clear_spam -> clear_profanity
# Description: run as a constant task that clears the spam.txt file
# Inputs:
#      - None
###########################
# async def clear_spam():
#     while True:
#         rows = db.select_query('SELECT * FROM profanity_settings')
#         rows_tuple = rows.fetchall()[0]
#         time_between_clears = rows_tuple[5]
#         # print("We cleared") ## for testing purposes
#         await asyncio.sleep(time_between_clears) # uses a set seconds betweeen spam clearing
#         with open("spam.txt", "r+", encoding='utf-8') as f:
#            f.truncate(0)  # delete the user_id of the last message sent
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
    #bot.loop.create_task(clear_spam())  # set up a task for the bot to clear out spam from the
    # txt file
    row = db.select_query('SELECT * FROM profanity_settings').fetchall()
    if len(row) == 0:
        # there is nothing in the database then put defaults in it
        warning_num = 1  # number of messages before warning of spam
        timeout_num = 2  # number of messages before timeout
        timeout_min = 1  # number of minutes in timeout
        timeout_hour = 0  # hours in timeout
        timeout_day = 0  # days in timout
        kicked_out_violations = 3
        penalty_value = 10
        db.mutation_query(
            'INSERT INTO profanity_settings VALUES (?, ?, ?, ?, ?, ?, ?)',
            [warning_num, timeout_num, timeout_min, timeout_hour, timeout_day, kicked_out_violations, penalty_value]
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
def profanity_penalize(author_id, table='rank'):
    id_query = f"SELECT * FROM {table} where user_id=?"
    result = db.select_query(id_query, (author_id,))
    result = result.fetchone()

    if result[1] >= 20:
        update_query = f"UPDATE rank SET experience=? WHERE user_id=?"
        db.mutation_query(update_query, (result[1]-10, author_id))
    elif result[1] < 20 and result[2] >0:
        update_query = f"UPDATE rank SET experience=?, level=?  WHERE user_id=?"
        db.mutation_query(update_query, (80+result[1], result[2]-1, author_id))

    if result[1] >= 10:
        update_query = f"UPDATE {table} SET experience=? WHERE user_id=?"
        db.mutation_query(update_query, (result[1]-10, author_id))
    elif result[1] < 10 and result[2] >0:
        update_query = f"UPDATE {table} SET experience=?, level=?  WHERE user_id=?"
        db.mutation_query(update_query, (90+result[1], result[2]-1, author_id))

    else:
        update_query = f"UPDATE {table} SET experience=? WHERE user_id=?"
        db.mutation_query(update_query, (0, author_id))


async def handle_profanity(message, ctx, guild_id):

    #print(message.content)
    #print(message.author.id)
    #print(type(message.author.id))
    print((f"{str(message.author.id)} {str(message.author)}\n"))
    # with open("spam.txt", "a", encoding='utf-8') as f:
    #     f.writelines(f"{str(message.author.id)}\n")

    # with open("spam.txt", "r+", encoding='utf-8') as f:
    #     for line in f:
    #         if line.strip("\n") == str(message.author.id):
    #             count = count + 1
    violations_query = db.select_query(f"SELECT * FROM rank where user_id=?", (message.author.id,))
    print('the violations_query', violations_query)
    violations = violations_query.fetchall()[0][3]
    print('the violations are: ', violations)
    rows = db.select_query('SELECT * FROM profanity_settings')
    rows_tuple = rows.fetchall()[0]
    warning_num = rows_tuple[0]
    timeout_num = rows_tuple[1]
    kicked_out_num  = rows_tuple[-2]
    penalty_value = rows_tuple[-1]
    if violations < warning_num:
        await ctx.send(f"{message.author.name} this is your first violation of using profanity, one more and you'll be in time out.")
        profanity_penalize( message.author.id)
        update_query = f"UPDATE rank SET violation_num=?  WHERE user_id=?"
        db.mutation_query(update_query,(violations+1, message.author.id)) 
    elif violations < timeout_num:
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
        await ctx.send(f"{message.author.name} has been timed out due to exceeding the permitted threshold for use of profanity")  # lets the everyone know who
        # was timed out
        profanity_penalize( message.author.id)
        update_query = f"UPDATE rank SET violation_num=? WHERE user_id=?"
        db.mutation_query(update_query,(violations+1, message.author.id))
    else:
        guild = BOT.get_guild(guild_id)
        member = guild.get_member(message.author.id)
        await member.kick()
        await ctx.send(f"{message.author.name} has been kicked out due to exceeding the permitted threshold for use of profanity")  # lets the everyone know who
        # was kicked out
        with open("blocked_user.txt", "a", encoding='utf-8') as f:
            f.writelines(f"{str(message.author.id)} {str(message.author)}\n")
        update_query = f"DELETE from rank WHERE user_id=?"
        db.mutation_query(update_query,(message.author.id,))
    return False

