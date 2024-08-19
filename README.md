Rock, Paper, Scissors Game

Welcome to the Rock, Paper, Scissors game! This is a simple console-based game where you play against the computer. The game allows you to choose between "rock," "paper," or "scissors," and the computer will make a random choice. The goal is to reach a score of 2 before the computer does.
How to Play

    Start the Game: Run the script to start the game.

    Make a Choice: Type 'rock', 'paper', or 'scissors' to make your move. You can also type 'exit' to quit the game at any time.

    Game Rounds:
        You will play up to 3 rounds.
        If you win 2 out of the 3 rounds, you win the game.
        If the computer wins 2 out of the 3 rounds, the computer wins the game.
        If there's a tie in a round, no points are awarded.

    Check Scores: After each round, your score and the computer's score will be displayed.

    Play Again: After a game ends, you can choose to play again or quit. If you choose to play again, there is a random chance the computer may decide not to play. If so, the game will end.

Code Explanation

    Imports: The random module is used to make random choices for the computer.
    Game Loop: The game continues in a loop until either the user or computer reaches a score of 2, or the user decides to exit.
    User Choice: The user inputs their choice of move.
    Computer Choice: The computer's move is randomly chosen from "rock," "paper," or "scissors."
    Determine Winner: The winner of each round is determined based on the standard rules of Rock, Paper, Scissors.
    Scores: Scores are tracked for both the user and the computer.
    Play Again: After a game ends, the user is asked if they want to play again. The computer also randomly decides whether to play again.

Example Usage

    Welcome to Rock, Paper, Scissors!
    Type 'rock', 'paper', or 'scissors' to choose your move or 'exit' to quit the game:
    
    rock
    
    User chose: rock
    Computer chose: scissors
    
    User wins
    
    User Score: 1
    Computer Score: 0
    ...
