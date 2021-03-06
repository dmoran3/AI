
2048 is played on a 4×4 grid with numbered tiles which can slide up, down, left, or right. This game can be
modeled as a two player game, in which the computer AI generates a 2- or 4-tile placed randomly on the
board, and the player then selects a direction to move the tiles. Note that the tiles move until they either (1)
collide with another tile, or (2) collide with the edge of the grid. If two tiles of the same number collide in a
move, they merge into a single tile valued at the sum of the two originals. The resulting tile cannot merge
with another tile again in the same move.
Usually, each role in a two-player games has a similar set of moves to choose from, and similar objectives
(e.g. chess). In 2048 however, the player roles are inherently asymmetric , as the Computer AI places tiles
and the Player moves them. Adversarial search can still be applied! Using your previous experience with
objects, states, nodes, functions, and implicit or explicit search trees, along with
our skeleton code , focus on optimizing your player algorithm to solve 2048 as efficiently and consistently
as possible. 
