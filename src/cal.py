"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""
from datetime import datetime
import discord

from discord.ext import tasks
import db
BOT = None
CALENDAR_EMBED = None
CLOSE_CALL_EMBED = None
CLOSE_CALL_EMBED_NONE = None
MSG = None
MSG_CC = None
MSG_CC_NONE = None
###########################
# Function: display_events
# Description: Sends or updates the embed for the calendar
# Inputs:
#      - ctx: context of function activation
###########################
async def display_events(ctx):
    ''' sends the embed to the channel and edits it to update it as well '''
    global MSG
    # recreate the embed from the database
    update_calendar(ctx)

    # if it was never created, send the first message
    if not MSG:
        MSG = await ctx.send(embed=CALENDAR_EMBED)
    else:
        # otherwise, edit the saved message from earlier
        await MSG.edit(embed=CALENDAR_EMBED)


###########################
# Function: update_calendar
# Description: Builds the calendar embed
###########################
def update_calendar(ctx):
    ''' create the calendar embed, it is a global so also updates it '''
    global CALENDAR_EMBED

    # create an Embed with a title and description of color 'currently BLUE'
    CALENDAR_EMBED = discord.Embed(title="The Course Calendar, sire",
        description="All of the class assignments and exams!", color=0x0000FF)

    # make a list that contains the string representing the
    # event that has the comparison item as the first index
    # which is the date, we are comparing as strings but still works for ordering events by date
    # do this for the events we care about in the calendar 'assignments and exams'
    assignments = []
    for title, link, desc, date in db.select_query(
            'SELECT title, link, desc, date FROM assignments ' +
            'WHERE guild_id = ? ' +
            'ORDER BY date ASC', [ctx.guild.id]):
        assignments.append([ f'{date}',
            f'{date}\n{title}\n{desc}\n{link}\n\n'])

    exams = []
    for title, desc, duration, begin_date, end_date in db.select_query(
            'SELECT title, desc, duration, begin_date, end_date FROM exams ' +
            'WHERE guild_id = ? ' +
            'ORDER BY begin_date ASC', [ctx.guild.id]):
        exams.append([ f'{begin_date}',
            f'{begin_date} - {end_date}\n{title}\n{desc}\n{duration}\n\n'])

    # get current time for comparison and make sure it is of same string format
    current_time = datetime.now().strftime('%m-%d-%Y %H:%M')
    #Time in EST: 2017-01-19 08:06:14

    i = 0
    j = 0

    # 2 lists for fields in the calendar
    past_events = ''
    #current_events = ''
    future_events = ''

    # go through the sorted lists and take the earliest date,
    # moving the index of each until all lists are placed
    # into one of the defined areas
    while (i != len(exams) or j != len(assignments)):
        if (i == len(exams) or (j != len(assignments) and assignments[j][0] < exams[i][0])):
            if assignments[j][0] < current_time:
                past_events += assignments[j][1]
            else:
                future_events += assignments[j][1]
            j += 1
        else:
            if exams[i][0] < current_time:
                past_events += exams[i][1]
            else:
                future_events += exams[i][1]
            i += 1

    # add the built strings to the embed
    if past_events != '':
        CALENDAR_EMBED.add_field(name="Past Events", value=past_events, inline=True)

    #CALENDAR_EMBED.add_field(name="Current Events", value=events, inline=False)

    if future_events != '':
        CALENDAR_EMBED.add_field(name="Coming up", value=future_events, inline=True)

    # mark the time that this was done for both creation and editing
    # NOTE - we put in EST because we are EST
    timeNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' EST'
    CALENDAR_EMBED.set_footer(text=f"{timeNow}")


###########################
# Function: init
# Description: Initializes the calendar, creating channel and embed call
# Inputs:
#      - b: bot
###########################
async def init(b):
    ''' initialize the calendar '''
    global BOT
    BOT = b
    for guild in BOT.guilds:
        for channel in guild.text_channels:
            if channel.name == 'course-calendar':
                await channel.delete()

        channel = await guild.create_text_channel('course-calendar')
        await display_events(channel)
        #close calls on assignments and exams
        await closecalls.start(channel)
        print('I dont get here')



###########################
# Function: closecalls
# Description: checks if any deadlines are coming up within a day
# this code runs in the background periodically
# Inputs:
#      - channel : the channel 'course-calendar'
###########################
@tasks.loop(minutes=1440)
async def closecalls(ctx): # pragma: no cover
    global MSG_CC
    global MSG_CC_NONE
    global CLOSE_CALL_EMBED
    global CLOSE_CALL_EMBED_NONE
    assignments = []
    for title, link, desc, date in db.select_query(
            'SELECT title, link, desc, date FROM assignments ' +
            'WHERE guild_id = ? ' +
            'ORDER BY date ASC', [ctx.guild.id]):
        assignments.append([ f'{date}',
            f'{date}\n{title}\n{desc}\n{link}\n\n'])

    exams = []
    for title, desc, duration, begin_date, end_date in db.select_query(
            'SELECT title, desc, duration, begin_date, end_date FROM exams ' +
            'WHERE guild_id = ? ' +
            'ORDER BY begin_date ASC', [ctx.guild.id]):
        exams.append([ f'{begin_date}',
            f'{begin_date} - {end_date}\n{title}\n{desc}\n{duration}\n\n'])

    # get current time for comparison and make sure it is of same string format
    current_time = datetime.now()
    i = j = 0
    close_events = ''
    # go through the sorted lists and take the earliest date,
    # moving the index of each until all lists are placed
    # into one of the defined areas
    while (i != len(exams) or j != len(assignments)):
        if (i == len(exams) or (j != len(assignments) and assignments[j][0] < exams[i][0])):
            if (datetime.strptime(
                assignments[j][0], '%Y-%m-%d %H:%M:%S') - current_time
                ).total_seconds() <= 86400 and (
                    datetime.strptime(
                        assignments[j][0], '%Y-%m-%d %H:%M:%S'
                        ) - current_time).total_seconds() >= 0:
                close_events += assignments[j][1]
            j += 1
        else:
            if (datetime.strptime(
                exams[i][0],'%Y-%m-%d %H:%M:%S') - current_time
                ).total_seconds() <= 86400 and (
                    datetime.strptime(
                        exams[i][0], '%Y-%m-%d %H:%M:%S') - current_time).total_seconds() >= 0:
                close_events += exams[i][1]
            i += 1
    # create an Embed with a title and description of color 'currently BLUE'
    CLOSE_CALL_EMBED = discord.Embed(title="Pay close attention to the close calls",
        description="Due within a day", color=0x0000FF)
    CLOSE_CALL_EMBED_NONE = discord.Embed(title="No close calls as of now",
        description="Nothing due within a day", color=0x0000FF)
    # add the built strings to the embed
    if close_events != '':
        CLOSE_CALL_EMBED.add_field(name="Close Calls", value=close_events, inline=True)

        # mark the time that this was done for both creation and editing
        # NOTE - we put in EST because we are EST
        timeNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' EST'
        CLOSE_CALL_EMBED.set_footer(text=f"{timeNow}")


        # if it was never created, send the first message
        if not MSG_CC:
            MSG_CC = await ctx.send(embed=CLOSE_CALL_EMBED)
        else:
            # otherwise, edit the saved message from earlier
            await MSG_CC.edit(embed=CLOSE_CALL_EMBED)
    else:
        timeNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' EST'
        CLOSE_CALL_EMBED_NONE.set_footer(text=f"{timeNow}")
        if not MSG_CC_NONE:
            MSG_CC_NONE = await ctx.send(embed=CLOSE_CALL_EMBED_NONE)
        else:

            # otherwise, edit the saved message from earlier
            await MSG_CC_NONE.edit(embed=CLOSE_CALL_EMBED_NONE)
@closecalls.before_loop
async def before(): # pragma: no cover
    await BOT.wait_until_ready()
