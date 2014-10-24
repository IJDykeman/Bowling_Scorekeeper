An example of the usage and output of this program:

The input from the machine is inputted as a string where an F
represents a downed pin, and a T represents and upright pin.


enter the number of players: 2
enter the name of player 1: Isaac
enter the name of player 2: Crimson
enter pin state for Isaac: fffttttttt
enter pin state for Isaac: fffffttttt
enter pin state for Crimson: fffftttttt
enter pin state for Crimson: fffftttfff
====================================Current=Scores====================================
|    Name    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |   10  |  Total  |
--------------------------------------------------------------------------------------
|Isaac       |[3,2]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , , ]|         |
|            |5    |     |     |     |     |     |     |     |     |       |5        |
--------------------------------------------------------------------------------------
|Crimson     |[4,3]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , , ]|         |
|            |7    |     |     |     |     |     |     |     |     |       |7        |
enter pin state for Isaac: ffffffffff
enter pin state for Crimson: fffffffttt
enter pin state for Crimson: ffffffffff
====================================Current=Scores====================================
|    Name    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |   10  |  Total  |
--------------------------------------------------------------------------------------
|Isaac       |[3,2]|[X,-]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , , ]|         |
|            |5    |15   |     |     |     |     |     |     |     |       |15       |
--------------------------------------------------------------------------------------
|Crimson     |[4,3]|[7,/]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , ]|[ , , ]|         |
|            |7    |17   |     |     |     |     |     |     |     |       |17       |
enter pin state for Isaac: fffttttttt
enter pin state for Isaac: fffttttttt
enter pin state for Crimson: ftftftftft
enter pin state for Crimson: ffffftftft


. . .


====================================Current=Scores====================================
|    Name    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |   10  |  Total  |
--------------------------------------------------------------------------------------
|Isaac       |[3,2]|[X,-]|[3,0]|[6,2]|[5,/]|[7,2]|[4,2]|[6,1]|[5,1]|[ , , ]|         |
|            |5    |18   |21   |29   |46   |55   |61   |68   |74   |       |74       |
--------------------------------------------------------------------------------------
|Crimson     |[4,3]|[7,/]|[5,2]|[X,-]|[3,0]|[3,5]|[0,1]|[X,-]|[8,/]|[ , , ]|         |
|            |7    |22   |29   |42   |45   |53   |54   |74   |84   |       |84       |
enter pin state for Isaac: ffffffffff
enter pin state for Isaac: ttttffffff
enter pin state for Isaac: ffffffffff
enter pin state for Crimson: tfffffffff 
enter pin state for Crimson: ffffffffff
enter pin state for Crimson: ffffffffff
====================================Current=Scores====================================
|    Name    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |   10  |  Total  |
--------------------------------------------------------------------------------------
|Isaac       |[3,2]|[X,-]|[3,0]|[6,2]|[5,/]|[7,2]|[4,2]|[6,1]|[5,1]|[X,6,/]|         |
|            |5    |18   |21   |29   |46   |55   |61   |68   |74   |94     |94       |
--------------------------------------------------------------------------------------
|Crimson     |[4,3]|[7,/]|[5,2]|[X,-]|[3,0]|[3,5]|[0,1]|[X,-]|[8,/]|[9,/,X]|         |
|            |7    |22   |29   |42   |45   |53   |54   |74   |93   |113    |113      |