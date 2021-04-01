letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q",
           "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
wordsy = [['BLUE', 'TENNIS', 'EXIT'], ['EARTH', 'EYES', 'MACHINE'],
          ['ERASER', 'BELLY', 'HUSKY'], ['ZAP', 'COMA', 'PERIOD']]
players = ['player1', 'wordNerd', 'Lexi con', 'Prof Reader']
# dictionary maker


def newdict(things, value):
    if isinstance(value, int) or len(value) == 0:
        newdict = [value for _ in range(len(things))]
        return {n: y for n, y in zip(things, newdict)}
    else:
        return {n: y for n, y in zip(things, value)}


players_score = newdict(players, 0)
letter_to_points = newdict(letters, points)
player_to_words = newdict(players, wordsy)
words_played = newdict(players, [])
letter_to_points.update({" ": 0})


def score_word(word, player):
    words_played[player] = words_played[player] + [word]
    for scrabletter in word:
        players_score[player] += letter_to_points.get(scrabletter.upper())
    return player, word


oddball = [[word for word in words]
           for words in player_to_words.values()]

for player, words in player_to_words.items():
    for word in words:
        score_word(word, player)

print(score_word('tiger', 'wordNerd'))
brownie_points = score_word('BrOwNiE', 'player1')


print('end of game:')
for player in players:

    print('''

                {} played: {}
                for a point total of {}.

    ''' .format(player, words_played[player], players_score[player]))

victor = {}
score = 0
for key, value in players_score.items():
    if value > score:
        score = value
        victor = {key: value}


print('''
and the victor is....

                            {}

long may they reign'''.format(victor))

print('''
and the victor is....

                                    o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                 "$
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$

                            {}

long may they reign'''
      .format(victor))



