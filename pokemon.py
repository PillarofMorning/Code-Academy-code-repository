import csv

poke_entry = []
with open('C:\\Users\\antoa\\Downloads\\pokelist.csv', newline='') as poke:
    pok = csv.DictReader(poke)
    for row in pok:
        poke_entry.append(row)

poke_moves = []
with open('C:\\Users\\antoa\\Downloads\\pokemoves1.csv', newline='') as poke:
    pok = csv.DictReader(poke)
    for row in pok:
        poke_moves.append(row)


class Poke_type:
    super_effective = {
        'Fire': ['Grass', 'Ice', 'Bug', 'Steel'],
        'Water': ['Fire', 'Ground', 'Rock'],
        'Electric': ['Water', 'Flying'],
        'Grass': ['Water', 'Ground', 'Rock'],
        'Ice': ['Grass', 'Ground', 'Flying', 'Dragons'],
        'Fighting': ['normal', 'Ice', 'Rock', 'Dark', 'Steel'],
        'Poison': ['Grass', 'Fairy'],
        'Ground': ['Fire', 'Electric', 'Poison', 'Rock', 'Ground', 'Steel'],
        'Flying': ['Grass', 'Fighting', 'Bug'],
        'Psychic': ['Fighting', 'Poison'],
        'Bug': ['Grass', 'Psychic', 'Dark'],
        'Rock': ['Fire', 'Ice', 'Flying', 'Bug'],
        'Ghost': ['Psychic', 'Ghost'],
        'Dragon': ['Dragon'],
        'Dark': ['Psychic', 'Ghost'],
        'Steel': ['Ice', 'Rock', 'Fairy'],
        'Fairy': ['Fighting', 'Dark', 'Dragon']
    }
    not_effective = {
        'normal': ['Rock', 'Steel'],
        'Fire': ['Fire', 'Water', 'Rock', 'Dragon'],
        'Water': ['Water', 'Grass', 'Dragon'],
        'Electric': ['Electric', 'Grass', 'Dragon'],
        'Grass': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel'],
        'Ice': ['Fire', 'Water', 'Ice', 'Steel'],
        'Fighting': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy'],
        'Poison': ['Poison', 'Rock', 'Ground', 'Ghost'],
        'Ground': ['Grass', 'Bug'],
        'Flying': ['Electric', 'Rock', 'Steel'],
        'Psychic': ['Psychic', 'Steel'],
        'Bug': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy'],
        'Rock': ['Fighting', 'Ground', 'Steel'],
        'Ghost': ['Dragon'],
        'Dragon': ['Steel'],
        'Dark': ['Fighting', 'Dark', 'Fairy'],
        'Steel': ['Fire', 'Water', 'Electric', 'Steel'],
        'Fairy': ['Fire', 'Poison', 'iron']
    }
    no_effect = {
        'normal': 'Ghost',
        'Electric': 'Ground',
        'Fighting': 'Ghost',
        'Poison': 'Steel',
        'Ground': 'Flying',
        'Psychic': 'Dark',
        'Ghost': 'normal',
        'Dragon': 'Fairy'
    }

    def __init__(self, name, type):
        self.type = type
        self.name = name

    def add_move(self, power_points, base):
        self.pp = power_points
        self.base = base
        return "the move of {} has pp value of {} for {} damage".format(self.name, self.pp, self.base)

    def ogpoke(self, name, pokemon):
        self.ogpoke = pokemon
        return "pokedex entry:{}".format(self.ogpoke)

    def hp(self, trainer, name, hp):
        self.hp = 0
        if isinstance(name, Poke_type) == True:
            name.hp += hp
        return "{} hit points".format(self.hp)

    def moves(self, name, moves):
        self.moves = []
        if isinstance(name, Poke_type) == True:
            for item in moves:
                name.moves.append(item)
        return "trained moves: {}".format(self.moves)

    def attack(self, trainer, pokemon, attack):
        element = pokemon.type
        if element[0] in self.super_effective[attack.type] or element[1] in self.super_effective[attack.type]:
            critical = int(attack.base) * 2
            print('your {} critically hit against {} for {} '.format(
                attack.name, pokemon.name, critical))
            pokemon.hp -= critical
            if pokemon.hp <= 0:
                trainer.available_pokemon.remove(pokemon)
                trainer.ko.append(pokemon)
                print('oh no {} fainted'.format(pokemon))
            return critical
        elif element[0] in self.not_effective[attack.type] or element[1] in self.not_effective[attack.type]:
            bummer = int(round(int(attack.base) / 2))
            print('your {} hit {} for {} '.format(
                attack.name, pokemon.name, bummer))
            pokemon.hp -= bummer
            if pokemon.hp <= 0:
                trainer.available_pokemon.pop(pokemon)
                trainer.ko.append(pokemon)
                print('oh no {} fainted'.format(pokemon))
            return bummer
        elif attack.type in self.no_effect:
            element[0] in self.no_effect[attack.type] or element[1] in self.no_effect[attack.type]
            print('no effect')
            return 0
        else:
            print('attack success')
            return attack.base

    def __repr__(self):
        return "{}".format(self.name)


for itxms in poke_entry:
    namev = itxms['Pokemon']
    type = itxms['Type']
    type2 = itxms['Type2']
    locals()[''+str(namev)+''] = Poke_type(
        name=namev,
        type=[type, type2])

for itvms in poke_moves:
    namev = itvms['Name'].replace(' ', '_')
    type = itvms['Type']
    pp = itvms['PP']
    base = itvms['Power']
    locals()[''+str(namev)+''] = Poke_type(
        name=namev,
        type=type)
    locals()[''+str(namev)+''].add_move(
        power_points=pp,
        base=base.strip('*'))


class Trainer:
    def __init__(self, name):
        badges = []
        self.name = name
        ko = []
        self.ko = ko
        self.badges = badges
        available_pokemon = []
        self.available_pokemon = available_pokemon

    def ko(self):
        return "ko list {}".format(self.ko)

    def available_pokemon(self):
        return "{} has these pokemon available: {}".format(self.name, self.available_pokemon)
    
    def addinventory(self, name, items):
        inventory = []
        self.inventory = inventory
        if hasattr(name, 'inventory') == True:
            if len(wowwow.inventory) < 20 and len(wowwow.inventory) >= 0:
                self.inventory.append(items)
            else:
                print('you have no space')

    def poke_crew(self, name, pokemon):
        if hasattr(name, 'available_pokemon') == True:
            if len(self.available_pokemon) < 6:
                self.available_pokemon.append(pokemon)
        return "your pokemon {} the {}, has been added to your set".format(name, pokemon)

    def badges(self, name, badge):
        if hasattr(name, 'badges') == True:
            pass

    def __repr__(self):
        return "{}".format(self.name)


def pokecreation(trainer, nickname, ogpokes, hp, moves):
    namex = nickname
    type = ogpokes.type
    globals()[''+str(namex)+''] = Poke_type(
        name=namex,
        type=type)
    globals()[''+str(namex)+''].hp(globals()[''+str(trainer)+''],
        globals()[''+str(namex)+''], 85)
    globals()[''+str(trainer)+''].poke_crew(globals()
                                           [''+str(trainer)+''], globals()[''+str(namex)+''])
    globals()[''+str(namex)+''].moves(
        globals()[''+str(namex)+''], ['Absorb', 'Tackle'])
    globals()[''+str(namex)+''].ogpoke(
        globals()[''+str(namex)+''], ogpokes)
    return print('pokemon added')



def pokebattle(blue, red):
    print('battle initated between: {} and {}, there is no running for pokebattles.')
    winner = []
    while len(red.pokecrew) > 0 and len(blue.pokecrew) > 0:
        print('red its your turn to attack')
        red.pokecrew[0].moves[0].attack(blue.pokecrew[0])
        blue.pokecrew[0].moves[0].attack(red.pokecrew[0])
        
    
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
wowwow = Trainer('wowwow')
print('''

inventory''')
wowwow.addinventory(wowwow, 'potion')

print('''

pokecreation''')
pokecreation(trainer = wowwow, nickname='Bulby',
             ogpokes=Bulbasaur, hp=85, moves=[Tackle, Absorb])


print(wowwow.available_pokemon)
print(wowwow.ko)
Charmander.attack(wowwow, Bulby, Ember)
Charmander.attack(wowwow, Bulby, Ember)
print(wowwow.available_pokemon)
print(wowwow.ko)

