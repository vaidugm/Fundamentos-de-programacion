import time

def printlyrics():
    lines = [
        ("insist", 0.07),
        ("That you are in love, my lover", 0.08),
        ("You passed out", 0.07),
        ("And I didn't even notice", 0.07),
        ("I think in position when I see your eyes", 0.09),
        ("Freud will be very, very, very mad", 0.08),
        ("So, so, so...", 0.05),
        ("Sorry you're gone", 0.07),
        ("So, so, so...", 0.05),
        ("Leave him alone", 0.07),
        ("(Lovely)", 0.06),
        ("Lovely, lovely times, nothing but (lovely)", 0.08),
        ("Lovely, lovely times, nothing while (lovely)", 0.08),
        ("Lovely, lovely times, nothing but (lovely, lovely)", 0.08),
        ("(Just me lovin' myself)", 0.09),
    ]

    for text, delay in lines:
        print(text, flush=True)
        time.sleep(delay)

printlyrics()
