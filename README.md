# mancala-move-calculator
[Works with Mancala Avalanche mode] This is a program the takes the number of stones at each pocket of the mancala board as input, then outputs a list of moves that will earn you the most stones.
Depending on whether you are playing counter-clockwise or clockwise, the indexes of each pocket will be different. This program assesses indexes 6-11 as the player side pockets (these are the pockets that the player can choose from). You must match these pockets to each players' respective sides.

Ex. If playing a counter-clockwise game, the 0th index will be the pocket to the right and closest to you, the player. The 11th pocket will be the pocket to the left and closest to you.
Counter-clockwise game:

[NULL(otherplayer's mancala]

[6th index]  [5th index]

[7th index]  [4th index]

[8th index]  [3th index]

[9th index]  [2th index]

[10th index] [1th index]

[11th index] [0th index]

[12th index(your mancala)]

12th index pocket will always be your mancala or store.
