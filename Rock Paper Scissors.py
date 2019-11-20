
import random
from itertools import cycle
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.my_move = None
        self.their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return beats(my_move, their_move)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player1_total = 0
        self.player2_total = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You Played: {move1}. \nOponent Played: {move2}.")

        a = self.p1.learn(move1, move2)
        b = self.p2.learn(move2, move1)
        if a == True and b == False:
            print("**PLAYER ONE WINS **")
            self.player1_total += 1
        elif a == b:
            print("** Tie **")
        elif a == False and b == True:
            print("** PLAYER TWO WINS **")
            self.player2_total += 1
        print(f"Score: Player one {self.player1_total}")
        print(f"Playe two {self.player2_total}\n\n")

    def total_result(self):
        if self.player1_total > self.player2_total:
            print("PLAYER ONE IS THE WINNER")
        elif self.player2_total > self.player1_total:
            print("PLAYER TWO IS THE WINNER")
        else:
            print("TIE")
        print(f"Fnal Score: player one {self.player1_total}")
        print(f"player two, {self.player2_total}")

    def play_game(self):
        while True:
            print("Game start!")
            for round in range(3):
                print(f"Round {round} --")
                self.play_round()
            self.total_result()
            print("Game over!\n-----------------------------")

            again = input("click Enter to play again, or (n,N,no) to Finish ")
            if again == 'n' or again == 'N' or again == "no":
                break

            self.player1_total = 0
            self.player2_total = 0


class Randomplayer(Player):
    def move(self):
        choice = random.choice(moves)
        return choice


class Humanplayer(Player):
    def move(self):
        while True:
            user_choice = input("Rock, Paper, scissors ? > \n")
            user_choice = user_choice.lower()
            if user_choice in moves:
                break
        return user_choice


class Cycleplayer(Player):
    def __init__(self):
        self.x = cycle(moves)

    def move(self):
        choice = next(self.x)
        return choice


class ReflectPlayer(Player):
    def move(self):
        if not self.their_move:
            return random.choice(moves)
        else:
            return self.their_move


if __name__ == '__main__':

    a = Cycleplayer()
    c = Randomplayer()
    p = Humanplayer()
    r = ReflectPlayer()

    g1 = Game(p, a)
    g2 = Game(p, c)
    g3 = Game(p, r)
    g4 = Game(p, p)

    print("\n------------Human Vs CyclePlayer-----------\n")
    g1.play_game()
    print("\n\n------------Human Vs Randomplayer------------\n")
    g2.play_game()
    print("\n\n-------------Human Vs ReflectPlayer----------\n")
    g3.play_game()
    print("\n\n----------------Human Vs Humanplayer----------------\n")
    g4.play_game()
    
    
    
