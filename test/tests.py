import os
import platform
import asyncio
import discord
from dotenv import load_dotenv

import test_office_hours
import test_event_creation
import test_qna
import test_calendar
import test_chart
import test_profanity
import test_email_utility
import test_attendance
import test_help
import test_regrade
import test_email_address
import test_spam
import test_ranking

import unittest

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()
TOKEN = os.getenv('TESTING_BOT_TOKEN')
TEST_GUILD_ID = int(os.getenv('TEST_GUILD_ID'))
intents = discord.Intents.all() ## needed to give the testing bot ability to do everything it needs
testing_bot = discord.Client(intents=intents)


async def run_tests():
    exit_status = 0
    await begin_tests()
    try:
        print('testing QNA\n----------')
        await test_qna.test(testing_bot, TEST_GUILD_ID)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')
    
    try:
        print('testing office hours\n----------')
        await test_office_hours.test(testing_bot, TEST_GUILD_ID)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')

    try:
        print('testing calendar\n----------')
        await test_calendar.test(testing_bot, TEST_GUILD_ID)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')
    
    try:
        print('testing profanity\n----------')
        await test_profanity.test(testing_bot, TEST_GUILD_ID)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')

    try:
        print('testing attendance\n----------')
        await test_attendance.test(testing_bot, TEST_GUILD_ID)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')

    try:
        print('testing help\n----------')
        await test_help.test(testing_bot, TEST_GUILD_ID)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')

    try:
        print('testing regrade\n----------')
        await test_regrade.test(testing_bot, TEST_GUILD_ID)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')

    try:
        print('testing email address configuration\n----------')
        await test_email_address.test(testing_bot, TEST_GUILD_ID)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')

    try:
        print('testing chart\n-----------')
        await test_chart.test(testing_bot, TEST_GUILD_ID)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')

    try:
        print('testing spam\n----------')
        await test_spam.test(testing_bot, TEST_GUILD_ID)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')

    try:
        print('testing rank card\n----------')
        await test_ranking.test(testing_bot)
    except AssertionError as ex:
        print('exception: ', type(ex).__name__ + ':', ex)
        print('--')

    finally:
        await end_tests()

    print('exit_status: ', exit_status)
    assert exit_status == 0
    await testing_bot.close()


@testing_bot.event
async def on_ready():
    print('Testing bot running')
    print('------')
    await run_tests()

async def begin_tests():
    await next(ch for ch in testing_bot.get_guild(TEST_GUILD_ID).text_channels
               if ch.name == 'instructor-commands').send('!begin-tests')

async def end_tests():
    await next(ch for ch in testing_bot.get_guild(TEST_GUILD_ID).text_channels
               if ch.name == 'instructor-commands').send('!end-tests')

if __name__ == '__main__':
    testing_bot.run(TOKEN)

###########################
# Function: test_dummy
# Description: Run the bot
###########################
def test_bot():
    testing_bot.run(TOKEN)
