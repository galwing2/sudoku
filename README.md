# sudoku

Project theme: The project solves advanced sudoku boards with different difficulty levels, based on user input.

Background: Sudoku contains 81 cells, in a 9 × 9 grid, and has 9 boxes, with each box being the intersection of the first, middle, or last three rows, and the first, middle, or last three columns. Each cell may contain a number from one to nine, and each number can appear only once in each row, column, and box. Sudoku starts with several cells that contain numbers (clues), and the goal is to solve the remaining cells. A proper sudocus has one solution. Players and researchers may use a variety of computer algorithms to solve sudokus, learn their properties, and make new puzzles, including sudokus with interesting symmetries and other features.


Algorithmics: Backtracking is a type of search algorithm that saves over a large number of candidates for solution by using specific features of the problem. The algorithm is designed to find solutions to problems that maintain the feature that can also disqualify partial solutions. A common example of this is a problem where there are several variables, and each variable must have a certain value adjusted so that there are a number of constraints. Many of the crossword puzzles are such problems (e.g. sudoku and kakuro).
In backtracking we have at every stage a partial solution of the problem, and we want to determine whether it can be extended to its complete solution or not.
The trouble is that in general we have several possible ways to expand the solution, and in advance we have no way of knowing which one does lead to the solution! (If any...). Therefore, we are forced to try each of the options one by one, recursively.
A key part of any backtracking algorithm is the stop conditions.
One stopping condition is clear - if the partial solution we received solves the complete problem, then we can stop and return this solution.
Another stopping condition, perhaps more important than that, is the case where we notice that the partial solution we have received is not extensible to a complete solution. In this case we would like to interrupt the recursion, and return a negative answer.
The second type of stop conditions is extremely important, as it helps narrow down our search space, which is huge and plentiful in the first place. In general, the more we learn to identify partial solutions that cannot be continued, and the earlier we identify them, the more efficient and faster backtracking will be.

Realization: The project is an advanced graphical representation of the sudoku problem. The user has the option to choose which board he wants to let the computer solve. Each board has a difficulty level, and the user can switch between them and look at the different solutions.
