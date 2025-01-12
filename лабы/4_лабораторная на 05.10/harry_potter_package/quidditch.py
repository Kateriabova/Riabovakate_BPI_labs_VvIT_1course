def seeker(x, y, field):
    if x >= len(field) or y >= len(field[0]):
        return 'дементор'
    if field[x][y] == 1:
        return '150 очков Гриффиндору! Матч закончился'
    else:
        return 'учишься балету, Поттер?'

def broomstick(name_of_broomstick, team):
    team.append(name_of_broomstick)
    if team.count(name_of_broomstick) >= 3 or len(name_of_broomstick) > 20:
        print('в Гриффиндоре никто не покупает себе место')
        return (False, None)
    return (True, team)
