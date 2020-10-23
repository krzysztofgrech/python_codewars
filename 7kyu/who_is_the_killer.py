""" https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d/ """


def killer(suspect_info, dead):
    suspects = suspect_info.keys()

    for suspect in suspects:
        person_seen = 0
        check = all(item in suspect_info[suspect] for item in dead)
        if check == True:
            return suspect