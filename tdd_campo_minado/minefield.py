def get_positions(m, n, **kwargs):
    minefield = field_structure(m, n, kwargs['bombs'])
    mapped_field = field_mapper(minefield)
    return mapped_field


def field_structure(m, n, bomb_locations):
    field = []
    for row in range(0, m):
        field.append([])
        for col in range(0, n):
            field[row].append(0)

    field = put_bombs(field, bomb_locations)
    return field


def put_bombs(minefield, bombs):
    for bomb in bombs:
        minefield[bomb[0]][bomb[1]] = '*'
    return minefield


def field_mapper(field):
    for x, row in enumerate(field):
        for y, location in enumerate(row):
            if location == '*':
                nearby_places = [
                    [x - 1, y - 1],
                    [x - 1, y],
                    [x - 1, y + 1],
                    [x, y - 1],
                    [x, y + 1],
                    [x + 1, y - 1],
                    [x + 1, y],
                    [x + 1, y + 1],
                ]
                for pos, place in enumerate(nearby_places):
                    try:
                        if place[0] >= 0 and place[1] >= 0:
                            field[place[0]][place[1]] += 1
                    except IndexError:
                        pass
                    except TypeError:
                        pass

    return field


if __name__ == "__main__":
    camp = get_positions(4, 4, bombs=[[0, 0], [2, 1], [3, 3], [0, 3], [3, 0], [1, 2]])

    for line in camp:
        for column in line:
            print(column, '|', end='')
        print()
