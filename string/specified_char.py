# program to get the last part of a string before a specified character


def specified_char(str, character):
    part = str.rsplit(character, 1)
    if len(str) > 1:
        return part[0]
    else:
        return str


print(specified_char("asd-sda,wdq/sdqw-weqw,qwq", ","))
