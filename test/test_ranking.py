
from time import sleep
import discord
from utils import wait_for_msg

# ###########################
# # Function: test
# # Description: runs each test for ranking
# # Inputs:
# #      - testing_bot: bot that sends commands to test TeachersPetBot
# #      - guild_id: id of the guild that is using the TeachersPetBot
# # Outputs: None
# ###########################
async def test(testing_bot):
     general_channel = discord.utils.get(testing_bot.get_all_channels(), name='general')
    #  await test_rank_for_same_user(testing_bot, general_channel)
     await test_rank_for_other_user(testing_bot, general_channel)
     await test_rank_for_other_user_who_does_not_exist(testing_bot, general_channel)


# ###########################
# # Function: test
# # Description: runs each test for command - !rank
# # Inputs:
# #      - testing_bot: bot that sends commands to test TeachersPetBot
# # Outputs: None
# ###########################
async def test_rank_for_same_user(testing_bot, general_channel):
    print("testing ranking for same user")
    await general_channel.send('!rank')
    response = await testing_bot.wait_for('message',
    check=lambda x: x.guild.id==general_channel.guild.id and bool(x.attachments))
    return response

async def test_rank_for_other_user(testing_bot, general_channel):
    member = None
    for member1 in testing_bot.get_all_members():
        if member1.name == 'testerbotse23': # enter the username of a member
            member = member1
            break
    await general_channel.send(f'!rank {member.mention}')
    response = await testing_bot.wait_for('message',
    check=lambda x: x.guild.id==general_channel.guild.id and bool(x.attachments))
    print(f"Response is {response}")
    return response


async def test_rank_for_other_user_who_does_not_exist(testing_bot, general_channel):
    await general_channel.send('!rank @ayush_ai8')
    #response = await testing_bot.wait_for('message',
    #check=lambda x: x.guild.id==general_channel.guild.id and bool(x.attachments))
    await wait_for_msg(testing_bot, general_channel, 'No @ayush_ai8 in the database')
