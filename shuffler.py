import random 
from rich.console import Console
c = Console()
passwords = ["rewqAse2w@dwwdSS" , "d90@1!werWS" , "34rxad!@!dwAsdd"]
choice = random.choice(passwords)
listforshuffle = list(choice)
random.shuffle(listforshuffle)
joined = "".join(listforshuffle)
print("The jumbled password is",joined)
print("Hint : The password is one of these three",passwords)
wrongpasswords = []
times = 0
while times<3:
    guess =  c.input("[green]Guessing Time![/green] : [orange1]Guess the password : [/orange1]")
    if not guess==choice : 
        wrongpasswords.append(f"[red]{guess}[/red]")
        c.print("[red]Wrong![/red]")
        times+=1
    else:
        c.print("[green]Correct![/green]")
        break
if times==3:
    c.print(f"You have failed 3 times . Your answers were {wrongpasswords} but the real answer is {choice} . ")