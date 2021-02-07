"""
Mancala move calculator
Input: stones in each pocket of the board
Output: list of moves that will provide player with most amount of stones.
"""


def main():
    # get input from user for stones at each pocket
    boxes = []
    for i in range(12):
        print("Number of pebbles in", i, "th box: ", end='')
        boxes.append(int(input()))
    boxes.append(0)

    # output order of moves to make
    moves = rotations(boxes)
    print("To get", moves[0], "pebbles, make moves in this order: ", end='')
    print(moves[1:])


# test every move index 6-11
def rotations(boxes):
    boxes_copied = boxes.copy()
    saved_moves = [0]
    for i in range(6, 12):
        if boxes_copied[i] > 0:
            dict_of_moves = one_rotation(boxes_copied, i)
            if dict_of_moves[0] > saved_moves[0]:
                saved_moves = dict_of_moves
    return saved_moves


# test one rotation of stones from chosen index
def one_rotation(boxes, index):
    boxes_copy = boxes.copy()
    pebbles = boxes_copy[index]
    dict_moves = [index]
    boxes_copy[index] = 0
    while pebbles >= 1:
        # move to next pocket of the board
        if index == 12:
            index = 0
        else:
            index += 1
        new_pebbles = boxes_copy[index]

        # adjust pebble amount in next box of the board
        if pebbles == 1 and index != 12 and new_pebbles > 0:
            # grab stones from this new pocket
            pebbles += new_pebbles
            boxes_copy[index] = 0
        elif pebbles == 1 and index == 12:
            # if ending pebble is placed into mancala store
            pebbles -= 1
            boxes_copy[index] += 1
            # start new set of rotations
            pairing = rotations(boxes_copy)
            boxes_copy[12] = pairing[0]
            pairing.pop(0)
            dict_moves.extend(pairing)
        else:
            pebbles -= 1
            boxes_copy[index] += 1

    # insert the number of gained stones into the first index of the list
    dict_moves.insert(0, boxes_copy[12])

    boxes_copy = []
    # returns a list with gained stones in first index.
    # The following numbers are respective pockets for players to move
    return dict_moves


main()
