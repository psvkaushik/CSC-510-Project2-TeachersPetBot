"""
Copyright (C) 2023 TeachersPetBotv2.0 - All Rights Reserved
You may use, distribute, and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: ncsuse23@gmail.com

"""
def award_update_rank_and_xp(rank, current_xp, awarded_xp):
    quotient, remainder = divmod(awarded_xp, 100)
    rank += quotient
    current_xp += remainder
    if current_xp >= 100:
        quotient, remainder = divmod(current_xp, 100)
        rank += quotient
        current_xp = remainder
    return rank, current_xp
