def is_valid_walk(walk):
    if len(walk) == 10:
        move = {}

        for i in walk:
            if i in move:
                move[i] += 1
            else:
                move[i] = 1

        vert = False
        horz = False

        try:
            if 'n' and 's' in move:
                if move['n'] == move['s']:
                    vert = True
            else: vert = True
        except KeyError:
            vert = True

        try:
            if 'e' and 'w' in move:
                if move['e'] == move['w']:
                    horz = True
            else: horz = True
        except KeyError:
            horz = True

        print(vert,horz)

        if horz == True and vert == True:
            return True
        else:
            return False

    else:
        return False

print(is_valid_walk(['s', 'e', 's', 'e', 'n', 's', 'n', 's', 'n', 'n']))
