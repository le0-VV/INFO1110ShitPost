import webbrowser

print("""
Human brain have 86 billion brain cells
The suffering known as studying for uni consumes brain cells (not true)
""")

suffer = input("Commence suffering? (y/n) ")

if not(suffer == "y" or suffer == "Y"):
    print("You have no choice")

braincells = int(input("How many brain cells do you have? "))
studying = True
while studying:
    if braincells == 0:
        break
    print("You have {}".format(braincells))
    braincells -= 1
print("""
You have no more brain cells
press enter to proceed with brain aneurysm
    """)
input()
webbrowser.open('https://www.youtube.com/watch?v=3ZeHmdJnny4', new=2)
