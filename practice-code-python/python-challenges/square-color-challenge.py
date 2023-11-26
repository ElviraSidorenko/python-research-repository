
# get a color of the tile based on the inputs
def get_color(column, row):
    if column.lower() in ('a', 'c', 'e', 'g'):
        if (row % 2) == 0:
            tile = 'white'
        else:
            tile = 'black'
    else:
        if (row % 2) == 0:
            tile = 'black'
        else:
            tile = 'white'
    return f'Your selected tile is {tile}'


# get a tile position
letter = input('Select a letter: ')
number = int(input('Select a number: '))

# display results
print(get_color(letter, number))
