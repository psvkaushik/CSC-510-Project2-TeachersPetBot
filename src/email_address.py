"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""

"""
This file contains functions and logic related to email address configuration.
"""
import db


async def create_email(ctx, email_address):
    """
        Configures the specified email address against user.

        Parameters:
            ctx: used to access the values passed through the current context
            email_address: email address specified by the author

        Returns:
            returns either an error stating a reason for failure or returns a success message
            indicating that the specified email address has been added.

    """
    author_id = ctx.message.author.id
    fetch_query = 'SELECT author_id FROM email_address WHERE author_id=? and is_active=1'
    cur = db.select_query(fetch_query, (author_id,))
    data = cur.fetchone()
    if data:
        await ctx.send('There is already an email address configured for this user. '
                       'Please update it using update_email command')
        return
    insert_query = 'INSERT INTO email_address VALUES (?, ?, ?)'
    db.mutation_query(insert_query, [author_id, email_address, 1])
    await ctx.send('Email has been configured successfully!')


async def update_email(ctx, email_address):
    """
        Updates the configured email address in json with the specified one.

        Parameters:
            ctx: used to access the values passed through the current context
            email_address: email address specified by the author

        Returns:
            returns either an error stating a reason for failure or returns a success message
            indicating that the specified email address has been added.

    """
    author_id = ctx.message.author.id
    fetch_query = 'SELECT author_id FROM email_address WHERE author_id=? and is_active=1'
    cur = db.select_query(fetch_query, (author_id,))
    data = cur.fetchone()
    if data:
        update_query = 'UPDATE email_address SET email_id=? WHERE author_id=? and is_active=?'
        db.mutation_query(update_query, (email_address, author_id, 1,))
        await ctx.send('Email address has been updated successfully')
        return
    await ctx.send('There is no configured email address')


async def view_email(ctx):
    """
        Displays the configured email address against user.

        Parameters:
            ctx: used to access the values passed through the current context

        Returns:
            returns either an error stating a reason for failure or returns a configured email
            address.

    """
    author_id = ctx.message.author.id
    fetch_query = 'SELECT email_id FROM email_address WHERE author_id=? and is_active=1'
    cur = db.select_query(fetch_query, (author_id,))
    email_address = cur.fetchone()
    if email_address:
        await ctx.send(f'Configured email address : {email_address[0]}')
        return
    await ctx.send('There is no configured email address')


async def delete_email(ctx):
    """
        Deletes the configured email address against user.

        Parameters:
            ctx: used to access the values passed through the current context

        Returns:
            returns either an error stating a reason for failure or returns a success message
            indicating that the specified email address has been deleted.

    """
    author_id = ctx.message.author.id
    fetch_query = 'SELECT author_id FROM email_address WHERE author_id=? and is_active=1'
    cur = db.select_query(fetch_query, (author_id,))
    data = cur.fetchone()
    if data:
        update_query = 'UPDATE email_address SET is_active=? WHERE author_id=?'
        db.mutation_query(update_query, (0, author_id,))
        await ctx.send('Email address has been deleted successfully')
        return
    await ctx.send('There is no configured email address')
