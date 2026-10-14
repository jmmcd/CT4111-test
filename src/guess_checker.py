def guess_checker(guess, secret):
    if guess < secret:
        return "Too low"
    elif guess > secret:
        return "Too high"
    return "Correct"
