"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""

###########################
# Functionality for creating new events
###########################
import datetime
from datetime import timedelta
from discord.ui import Button, Select, View
from discord import SelectOption, ButtonStyle
from discord.utils import get
from discord.ext import tasks

import validators

from utils import EmailUtility


import office_hours
import cal
import db

BOT = None

###########################
# Function: create_event
# Description: creates an event by the specifications of the instructor creating the event
# Inputs:
#      - ctx: context of this discord message
#      - testing_mode: flag indicating whether this event is being created during a system test
# Outputs: new event created in database
###########################
async def create_event(ctx, testing_mode):
    ''' create event input flow '''

    if ctx.channel.name == 'instructor-commands':
        button1 = Button(style=ButtonStyle.blurple, label='Assignment', custom_id='assignment')
        button2 = Button(style=ButtonStyle.green, label='Exam', custom_id='exam')
        button3 = Button(style=ButtonStyle.grey, label='Project', custom_id='project')
        button4 = Button(style=ButtonStyle.red, label='Office Hour', custom_id='office-hour')
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        await ctx.send(
            'Which type of event would you like to create?', view = view
        )
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        """
        if testing_mode:
            button_clicked = await BOT.wait_for('message', timeout = 5, check = check)
            button_clicked = button_clicked.content
        else:
            button_clicked = (await BOT.wait_for('button_click')).custom_id
        """
        async def button_callback(interaction):
            await interaction.response.send_message('What would you like the assignment to '
                                                    'be called')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            title = msg.content.strip()

            await ctx.send('What is the due date of this assignment?\nEnter in format '
                           '`MM-DD-YYYY`')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            date = msg.content.strip()
            try:
                datetime.datetime.strptime(date, '%m-%d-%Y')
            except ValueError:
                await ctx.send('Invalid date foamt. Aborting.')
                return

            await ctx.send('What time is this assignment due?\nEnter in 24-hour format' +
                ' e.g. an assignment due at 11:59pm can be inputted as 23:59')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            t = msg.content.strip()
            try:
                datetime.datetime.strptime(t, '%H:%M')
            except ValueError:
                await ctx.send('Invalid Time format. Aborting.')
                return
            deadline = datetime.datetime.strptime(date+' '+t, '%m-%d-%Y %H:%M')

            await ctx.send('Link associated with submission? Type N/A if none')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            link = msg.content.strip() if msg.content.strip() != 'N/A' else None
            if link and not validators.url(link):
                await ctx.send('Invalid URL. Aborting.')
                return

            await ctx.send('Extra description for assignment? Type N/A if none')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            description = msg.content.strip() if msg.content.strip() != 'N/A' else None

            db.mutation_query(
                'INSERT INTO assignments VALUES (?, ?, ?, ?, ?)',
                [ctx.guild.id, title, link, description, deadline]
            )

            await ctx.send('Assignment successfully created!')
            await cal.display_events(ctx)

        button1.callback = button_callback #assigns to the assignment button the function above

        async def project_button_callback(interaction):
            await interaction.response.send_message('What is the title of this project?')
            msg = await BOT.wait_for('message', timeout=60.0, check=check)
            project_title = msg.content.strip()

            await ctx.send(
                'Please enter the due date of this project along with the time\n'
                'Enter in 24-hour format for e.g. an project due at 11:59pm can be inputted '
                'as 23:59\nEnter in format `MM-DD-YYYY %H:%M`')
            msg = await BOT.wait_for('message', timeout=60.0, check=check)
            date_str = msg.content.strip()

            try:
                due_date = datetime.datetime.strptime(date_str, '%m-%d-%Y %H:%M')
            except ValueError:
                await ctx.send('Invalid date format. Aborting, Please try again!.')
                return

            await ctx.send('Link associated with submission? Type N/A if none')
            msg = await BOT.wait_for('message', timeout=60.0, check=check)
            link = msg.content.strip() if msg.content.strip() != 'N/A' else None
            if link and not validators.url(link):
                await ctx.send('Invalid URL. Aborting, Please try again!.')
                return

            await ctx.send('Extra description for project? Type N/A if none')
            msg = await BOT.wait_for('message', timeout=60.0, check=check)
            description = msg.content.strip() if msg.content.strip() != 'N/A' else None

            db.mutation_query(
                'INSERT INTO assignments VALUES (?, ?, ?, ?, ?)',
                [ctx.guild.id, project_title, link, description, due_date]
            )
            await ctx.send('Project successfully created!')
            await cal.display_events(ctx) ## needed so the calander updates
        button3.callback = project_button_callback #assigns the project button to the function
        # directly above

        async def exam_button_callback(interaction):
            await interaction.response.send_message('What is the title of this exam?')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            title = msg.content.strip()

            await ctx.send('What is the start date of this exam?\nEnter in format `MM-DD-YYYY`')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            date_start = msg.content.strip()
            try:
                datetime.datetime.strptime(date_start, '%m-%d-%Y')
            except ValueError:
                await ctx.send('Invalid date. Aborting.')
                return

            await ctx.send('What is the start time for the exam?\nEnter in 24-hour format' +
                ' e.g. an exam starting at 1:59pm can be inputted as 13:59')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            t_start = msg.content.strip()
            try:
                datetime.datetime.strptime(t_start, '%H:%M')
            except ValueError:
                await ctx.send('Invalid Time format. Aborting.')
                return

            start = datetime.datetime.strptime(date_start+' '+t_start, '%m-%d-%Y %H:%M')

            await ctx.send('What is the end date of this exam?\nEnter in format `MM-DD-YYYY`')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            date_end = msg.content.strip()
            try:
                datetime.datetime.strptime(date_end, '%m-%d-%Y')
            except ValueError:
                await ctx.send('Invalid date. Aborting.')
                return

            await ctx.send('What is the end time for the exam?\nEnter in 24-hour format' +
                ' e.g. an exam ending at 1:59pm can be inputted as 13:59')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            t_end= msg.content.strip()
            try:
                datetime.datetime.strptime(t_end, '%H:%M')
            except ValueError:
                await ctx.send('Invalid Time format. Aborting.')
                return
            end = datetime.datetime.strptime(date_end+' '+t_end, '%m-%d-%Y %H:%M')

            await ctx.send('What is the duration of the exam?\nEnter in minutes' +
                ' e.g. for 1hr 25 mins input as 85 minutes')
            msg = await BOT.wait_for('message', timeout = 60.0, check = check)
            duration = msg.content.strip()

            await ctx.send('description of the exam(like syllabus, online/inperson)?' +
             'Type N/A if none')
            msg = await BOT.wait_for('message', timeout = 300.0, check = check)
            description = msg.content.strip() if msg.content.strip() != 'N/A' else None

            db.mutation_query(
                'INSERT INTO exams VALUES (?, ?, ?, ?, ?, ?)',
                [ctx.guild.id, title, description, duration, start, end]
            )

            await ctx.send('Exam successfully created!')
            await cal.display_events(ctx) ## updates the calender channel on discord
        button2.callback = exam_button_callback

        async def office_hour_button_callback(interaction):
            instructor = None
            day = None
            leadrole = get(ctx.guild.roles, name='Instructor')
            all_instructors = leadrole.members

            if len(all_instructors) < 1:
                await ctx.send('There are no instructors in the guild. Aborting')
                return

            options = [SelectOption(label=instr.name, value=instr.name)
                for instr in all_instructors]
            instructor_select = Select(
                        placeholder='Select an instructor', #all_instructors[0].name,
                        options=options
                    )
            instructor_view = View()
            instructor_view.add_item(instructor_select)
            await interaction.response.send_message(
                'Which instructor will this office hour be for?',
                view = instructor_view
            )
            """
            if testing_mode:
                instructor = await BOT.wait_for('message', timeout = 5, check = check)
                instructor = instructor.content
            else:
                instructor = (await BOT.wait_for('select_option')).values[0]
            """
            day_select = Select(placeholder='Select a day',
                            options=[
                                SelectOption(label='Monday', value='Mon'),
                                SelectOption(label='Tuesday', value='Tue'),
                                SelectOption(label='Wednesday', value='Wed'),
                                SelectOption(label='Thursday', value='Thu'),
                                SelectOption(label='Friday', value='Fri'),
                                SelectOption(label='Saturday', value='Sat'),
                                SelectOption(label='Sunday', value='Sun')
                            ])
            day_view = View()
            day_view.add_item(day_select)
            #function to respond to instructor selection
            async def instructor_select_callback(interaction):
                instructor = instructor_select.values[0] ## assigns instructor with the selected
                # instructor
                print(instructor)
                await interaction.response.send_message(
                    'Which day would you like the office hour to be on?',
                    view=day_view
                )
            instructor_select.callback = instructor_select_callback
            """
            if testing_mode:
                day = await BOT.wait_for('message', timeout = 5, check = check)
                day = day.content
            else:
                day = (await BOT.wait_for('select_option')).values[0]
            """
            async def day_select_callback(interaction):
                day = day_select.values[0]
                print(day)
                await interaction.response.send_message('What is the start time of the office '
                                                        'hour?\nEnter in 24-hour format' +
                    ' e.g. an starting at 1:59pm can be inputted as 13:59')
                msg = await BOT.wait_for('message', timeout = 60.0, check = check)
                t_start = msg.content.strip()
                try:
                    t_start = datetime.datetime.strptime(t_start, '%H:%M')
                except ValueError:
                    await ctx.send('Invalid Time format. Aborting.')
                    return

                await ctx.send('What is the end time of the office hour?\nEnter in 24-hour format' +
                    ' e.g. an exam ending at 1:59pm can be inputted as 13:59')
                msg = await BOT.wait_for('message', timeout = 60.0, check = check)
                t_end= msg.content.strip()
                try:
                    t_end = datetime.datetime.strptime(t_end, '%H:%M')
                except ValueError:
                    await ctx.send('Invalid Time format. Aborting.')
                    return
                office_hours.add_office_hour(
                    ctx.guild,
                    office_hours.TaOfficeHour(
                        instructor,
                        day,
                        (t_start, t_end)
                    )
                )

                db.mutation_query(
                    'INSERT INTO ta_office_hours VALUES (?, ?, ?, ?, ?)',
                    [ctx.guild.id, instructor, day, t_start, t_end]
                )

                await ctx.send('Office hour successfully created!')
                await cal.display_events(ctx)  ## updates the calender channel on discord with
                # new office hours
            day_select.callback = day_select_callback ## sets the day selection button to call to
            # the correct function
        button4.callback = office_hour_button_callback
    else:
        await ctx.author.send('`!create` can only be used in the `instructor-commands` channel')
        await ctx.message.delete()


@tasks.loop(hours=24)
async def check_reminders_due_today():
    current_time = datetime.datetime.now()
    current_day = datetime.datetime(day=current_time.day, month=current_time.month,
                                    year=current_time.year)
    next_day = current_day + timedelta(days=1)
    cur = db.select_query(
        'SELECT title, link, desc, date FROM assignments WHERE date BETWEEN ? AND ?',
        [current_day, next_day])
    due_today_records = cur.fetchall()
    fetch_query = 'SELECT email_id FROM email_address WHERE is_active=1'
    cur = db.select_query(fetch_query)
    email_address = cur.fetchall()
    email_address = [x[0] for x in email_address]
    for title, link, desc, date in due_today_records:
        subject = " REMINDER FROM TEACHERS PET BOT"
        body = f'This is to remind you about assignment {title} deadline.'
        body += f'Assignment is due on {date}'+'\n'+desc
        EmailUtility().send_email(subject=subject, body=body, recipient=email_address)


###########################
# Function: init
# Description: initializes this module, giving it access to discord bot
# Inputs:
#      - b: discord bot
# Outputs: None
###########################
def init(b):
    '''
        initialize event creation
    '''
    global BOT
    BOT = b
    check_reminders_due_today.start()
