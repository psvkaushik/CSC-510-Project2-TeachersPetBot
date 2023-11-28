"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""

from easy_pil import *

async def draw_card(xp, level, rank, name, image_url, next_level_xp):
    # Create a blank canvas with colour #141414
    background = Editor(Canvas((900,300), color="#141414"))
    # Load the profile picture from discoerd and resize it to 200x200.
    profile_picture = await load_image_async(str(image_url))
    profile = Editor(profile_picture).resize((200,200)).circle_image()
    # Create two font sizes for font "poppin"
    poppins = Font.poppins(size=40)
    poppins_small = Font.poppins(size=20)
    # Reshape the card for stylinhg
    card_shape = [(600,0),(750,300),(900,300),(900,0)]
    # Paste the profile picture on the polygon
    background.polygon(card_shape, color="#5865F2")
    background.paste(profile, (30,30))
    # Write text on the card
    background.text((250,40), f"{name}", font=poppins, color="#FFFFFF")
    background.rectangle((250, 100), width=350, height=2, fill="#FFFFFF")
    background.text((250,130), f"Rank - {rank}", font=poppins, color="#FFFFFF")
    background.text((250,180),
                    f"Level - {level} | XP - {xp}/{next_level_xp}", 
                    font=poppins_small,
                    color="#FFFFFF")
    return background.image_bytes
                   
