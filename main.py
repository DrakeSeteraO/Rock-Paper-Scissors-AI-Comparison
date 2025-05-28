import random

class RockPaperScissorObject:
    def __init__(self):
        self.wins = 0
        self.games_played = 0

    def play(self, previous, reset = False):
        self.games_played += 1
        if previous == 1:
            self.wins += 1
        if reset:
            self.games_played -= 1
        return 0

    def name(self):
        return self.__class__.__name__

    def get_win_rate(self):
        return f"{self.wins/self.games_played * 100} %"

    def print(self):
        output = self.name() + ' ' * (17 - len(self.name())) + str(self.wins) + ' ' * (10 - len(str(self.wins))) + str(self.get_win_rate())
        print(output)



class Rock(RockPaperScissorObject):
    def play(self, previous, reset = False):
        super().play(previous, reset)
        return 0


class Paper(RockPaperScissorObject):
    def play(self, previous, reset = False):
        super().play(previous, reset)
        return 1


class Scissor(RockPaperScissorObject):
    def play(self, previous, reset = False):
        super().play(previous, reset)
        return 2


class Random(RockPaperScissorObject):
    def play(self, previous, reset = False):
        super().play(previous, reset)
        return random.randint(0,2)


class Beat_Most_Common(RockPaperScissorObject):
    def __init__(self):
        super().__init__()
        self.rock = 0
        self.paper = 0
        self.scissor = 0
        self.previous = 0

    def play(self, previous, reset = False):
        super().play(previous, reset)
        if reset:
            self.rock = 0
            self.paper = 0
            self.scissor = 0
            
        self.determine_previous(previous)
        max_value = self.rock
        choice = 1
        if self.paper > max_value:
            max_value = self.paper
            choice = 2
        if self.scissor > max_value:
            choice = 0
        self.previous = choice
        return choice
    
    def determine_previous(self, previous):
        if previous == 1:
            options =[self.scissor, self.rock, self.paper]
            options[self.previous] += 1
                
            self.scissor = options[0]
            self.rock = options[1]
            self.paper = options[2]
        elif previous == 0:
            options =[self.rock, self.paper, self.scissor]
            options[self.previous] += 1
            
            self.rock = options[0]
            self.paper = options[1]
            self.scissor = options[2]
        else:
            options =[self.paper, self.scissor, self.rock]
            options[self.previous] += 1
            
            self.paper = options[0]
            self.scissor = options[1]
            self.rock = options[2]   


class Tit_for_Tat(RockPaperScissorObject):
    def __init__(self):
        super().__init__()
        self.previous = 0
        
    def play(self, previous, reset = False):
        super().play(previous, reset)
        if previous == 1:
            return self.previous
        elif previous == 0:
            self.previous = (self.previous + 1) % 3
            return self.previous
        else:
            self.previous = (self.previous - 1) % 3
            return self.previous
        
       
class Rotate(RockPaperScissorObject):
    def __init__(self):
        super().__init__()
        self.previous = 0
    
    def play(self, previous, reset=False):
        super().play(previous, reset)
        self.previous = (self.previous + 1) % 3
        return self.previous



def determine_vs(AI: list[RockPaperScissorObject]):
    vs = list()
    for x in range(len(AI)-1):
        for y in range(x+1,len(AI)):
            vs.append((AI[x],AI[y]))
    return vs


def run_competition(AI:list[RockPaperScissorObject], amount: int):
    vs = determine_vs(AI)
    for i in vs:
        play_game(i, amount)


def play_game(AI: list[RockPaperScissorObject], amount: int):
    p1_win = 0
    p2_win = 0
    p1 = AI[0].play(0, True)
    p2 = AI[1].play(0, True)
    for i in range(amount):
        win = (p1-p2) % 3
        if win == 1:
            p1_win = 1
            p2_win = -1
        elif win == 2:
            p1_win = -1
            p2_win = 1
        else:
            p1_win = 0
            p2_win = 0
            
        p1 = AI[0].play(p1_win)
        p2 = AI[1].play(p2_win)

def compare_wins(AI: list[RockPaperScissorObject]):
    wins_dict = dict()
    wins_amount = list()
    for ai in AI:
        if ai.wins in wins_dict:
            wins_dict[ai.wins].append(ai)
        else:
            wins_dict[ai.wins] = [ai]
            wins_amount.append(ai.wins)
    wins_amount.sort(reverse = True)
    return wins_dict, wins_amount

def display_results(wins_dict: dict, wins_amount: list[RockPaperScissorObject]):
    output = 'Name' + ' ' * (17 - len('Name')) + 'Wins' + ' ' * (10 - len('Wins')) + 'Win percentage'
    print(output)
    for x in wins_amount:
        for y in wins_dict[x]:
            y.print()


def main():
    AI = [Rock(),Paper(),Scissor(),Random(),Beat_Most_Common(),Tit_for_Tat(),Rotate()]

    amount = 10000

    run_competition(AI, amount)
    wins_dict, wins_amount = compare_wins(AI)
    display_results(wins_dict, wins_amount)

if __name__ == '__main__':
    main()
