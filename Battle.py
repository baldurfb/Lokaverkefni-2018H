# Baldur Fróði Briem
# 22/11/2018
import Soldier
import random
import time

from Soldier import get_integer_from_user


def create_factions():
    factions = []
    for faction in ['Pessar', 'Hettir', 'Dreyrar']:
        regular_soldiers = get_integer_from_user(
            'Hversu margir venjulegir hermenn eiga að vera í ættbálkinum {}? '.format(faction))
        super_soldiers = get_integer_from_user(
            'Hversu margir super hermenn eiga að vera í ættbálkinum {}? '.format(faction))
        user_control = True if input('Vilt þú stjórna ættbálkinum[Y/N]? ').upper() == 'Y' else False
        factions.append(Soldier.Faction(faction, regular_soldiers, super_soldiers, user_control))
    return factions


def damage(soldier):
    soldier.hp -= 1
    if soldier.hp <= 0:
        soldier.faction.kia(soldier)
        if soldier.faction.defeated:
            factions.remove(soldier.faction)


def fight(battle_factions: list):
    global factions
    soldiers = [faction.pick_soldier() for faction in battle_factions]

    for index, soldier in enumerate(soldiers):
        for enemyIndex, enemy in enumerate(soldiers):
            if index <= enemyIndex:
                continue
            soldier_strike = soldier.calculate_strike()
            enemy_strike = enemy.calculate_strike()

            if soldier_strike < enemy_strike:
                damage(soldier)
                return ('{} með högg {} '
                        'vinnur {} með '
                        'högg {}'.format(enemy.name, round(enemy_strike, 2), soldier.name,
                                         round(soldier_strike, 2)))
            if soldier_strike > enemy_strike:
                damage(enemy)
                return ('{} með högg {} '
                        'vinnur {} með '
                        'högg {}'.format(soldier.name, round(soldier_strike, 2), enemy.name,
                                         round(enemy_strike, 2)))
            else:
                return 'Jafntefli'


def main():
    global factions
    factions = create_factions()

    while True:
        if len(factions) > 1:
            try:
                print(fight(random.sample(factions, 2)))
            except IndexError:
                print([faction.soldiers for faction in factions])
            time.sleep(2)
        else:
            return 'Ættbálkurinn {} vann!'.format(factions[0].name)


if __name__ == '__main__':
    factions = []
    print(main())
