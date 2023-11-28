"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""
import re
import db


async def add_request(ctx, name: str, questions: str):
    """
        command to add regrade request
        Parameters:
            ctx : context of function activation
            name: name of the student
            questions: question numbers to be regraded
            output: adds the regrade request to the database
    """
    name = name.upper()

    for temp_name in db.select_query(
            '''SELECT name,questions FROM regrade WHERE name=? ''',
            (name,)

    ):
        if temp_name:
            await ctx.send("Duplicate regrade request."\
                    "Use !regrade-update command to make updates to request")
            return

    if not re.match(r"[Qq][0-9]+,[Qq][0-9]+", questions):
        await ctx.send("Invalid Input. Enter valid question numbers")
    else:
        db.mutation_query(
            'INSERT INTO regrade VALUES (?, ?, ?)',
            [ctx.guild.id, name, questions]
        )
        await ctx.send(name + "'s regrade request successfully submitted")


async def display_requests(ctx):
    """
        command to display all the  regrade requests
        Parameters:
            ctx : context of function activation
            output: displays the student name and the question numbers to be regraded
    """
    for name, questions in db.select_query(
            'SELECT name,questions FROM regrade'
    ):
        if name:
            await ctx.send(name + " " + questions)
        else:
            await ctx.send('There are no regrade requests at the moment')
            break


async def update_regrade_request(ctx, name: str, questions: str):
    """
        command to update an existing regrade request
        Parameters:
            ctx : context of function activation
            name: name of the student
            questions: question numbers to be regraded
            output: updates an existing regrade request with any modifications
    """

    name = name.upper()

    if not re.match(r"[Qq][0-9]+,[Qq][0-9]+", questions):
        await ctx.send('Invalid Input. Enter valid question numbers \n '
                       'Use !update-request <StudentName> <question numbers> \n \
        ( Example: !regrade-request "Student 1" q1,q2,q3 )')
    else:
        db.mutation_query(
            'UPDATE  regrade SET name = ? , questions = ?'
            'WHERE guild_id = ? AND name = ? ',
            [name, questions, ctx.guild.id, name]
        )
        await ctx.send(name + "'s regrade request updated successfully")

async def remove_regrade_request(ctx, name: str, questions: str):
    """
        command to remove a regrade request
        Parameters:
            ctx : context of function activation
            name: name of the student
            questions: question numbers to be regraded
            output: removes an existing regrade request from the database
    """

    name = name.upper()

    if not re.match(r"[Qq][0-9]+,[Qq][0-9]+", questions):
        await ctx.send('Invalid Input. Enter valid question numbers \n '
                       'Use !remove-request <StudentName> <question numbers> \n \
        ( Example: !remove-request "Student 1" q1,q2,q3 )')

    else:
        db.mutation_query(
            'DELETE FROM regrade '
            'WHERE guild_id = ? AND name = ? ',
            [ctx.guild.id, name]
        )
        await ctx.send(name + "'s regrade request removed successfully")
