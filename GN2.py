"""
print wlecom screan
"""


def welcom_scre():
    print("Pomyśl liczbę od 1 do 1000 ja ją zgadne w max 10 próbach")


"""
 guess allogitm
"""


def first_guess(maxv=1000, minv=0):
    shot = int(((maxv - minv) / 2) + minv)
    return shot


"""
get answere fro user
"""


def answer():
    ans = input("jeżeli  liczba jest za małą napisz proszę  To small\n"
                "jeżeli  liczba jest za duża napisz proszę  To big\n"
                "jeżeli odgadłem   You win:\n")
    return ans


"""
chceking answer 
"""


def check_ans():
    x = None
    while x == None:
        ans = answer()
        ans = ans.lower()
        if ans == "you win":
            print("WYGRAŁEM")
            x = 43

        elif ans == "to big":
            x = 1
            return x
        elif ans == "to small":
            x = 2
            return x
        else:
            print("błedan podpowiedź nie rozumiem ")


"""
guesing strategy part 
"""


def game():
    welcom_scre()
    shot = first_guess()
    mv = 1000
    minV= 0
    for i in range(0, 10):
        print(shot)
        temp = check_ans()
        if temp == 1:
            mv = shot
            shot = first_guess(mv, minV)
        elif temp == 2:
            minV = shot
            shot = first_guess(mv, minV )


game()
