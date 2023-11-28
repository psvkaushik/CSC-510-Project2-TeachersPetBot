"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""
from easy_pil import *

async def draw_leaderboard(users):
    # Create a blank canvas with a specific background color
    background = Editor(Canvas((1200, 600), color="#141414"))
    y_offset = 20

    poppins = Font.poppins(size=40)
    poppins_small = Font.poppins(size=20)

    # Display leaderboard title
    background.text((50, y_offset), "Leaderboard", font=poppins, color="#FFFFFF")
    y_offset += 60  # Increase the y-offset for the title

    # Display user information in the leaderboard
    for index, user in enumerate(users, start=1):
        # Adjust the image URL based on your data model
        image_url = user['image_url']
        username = user['name']
        xp = user['xp']
        level = user['level']

        profile_picture = await load_image_async(str(image_url))
        profile = Editor(profile_picture).resize((100, 100)).circle_image()

        # Place user profile picture
        background.paste(profile, (50, y_offset))

        # Display user information text
        background.text((200, y_offset + 20), f"{index}. {username}", font=poppins, color="#FFFFFF")
        background.text((200, y_offset + 70), f"Level: {level} | XP: {xp}", font=poppins_small, color="#FFFFFF")

        y_offset += 140  # Increase the y-offset for the next user

    return background.image_bytes
