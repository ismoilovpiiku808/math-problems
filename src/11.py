
def get_random_math_problem(difficulty):
    if difficulty == "easy":
        problem = random.choice([
            ("2 + 2", 4),
            ("5 - 3", 2),
            ("10 / 2", 5),
        ])
    elif difficulty == "medium":
        problem = random.choice([
            ("2 + 2 x 3", 8),
            ("5 - 2 x 4", 6),
            ("10 / 2 x 2", 5),
        ])
    else: # difficulty == "hard"
        problem = random.choice([
            ("2 + 2 x 3 x 4", 20),
            ("5 - 2 x 4 x 6", 18),
            ("10 / 2 x 2 x 3", 6),
        ])
    return problem[0], problem[1]