import random


def randInt(min, max):
    """
    Returns random integer between a given range
    """
    return random.randint(min, max)


def randOper():
    """
    Returns a random selection of operators.
    """
    return random.choice(['+', '-', '*'])


def generateProblem(n1, n2, oper):
    """
    Generates a problem and its answer, to be given in the quiz game.
    """
    prob = f"{n1} {oper} {n2}"
    if oper == '+': ans = n1 + n2
    elif oper == '-': ans = n1 - n2
    else: ans = n1 * n2
    return prob, ans

def math_quiz():
    """
    Main function to play the game. Generates random numbers, operators, and question using them.
    """
    
    s = 0
    t_q = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        try:
            n1 = randInt(1, 10); n2 = randInt(1, 6); o = randOper()

            PROBLEM, ANSWER = generateProblem(n1, n2, o)
            print(f"\nQuestion: {PROBLEM}")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                s += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        except Exception as e:
            print("There was an error.\n"+str(e))

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
