from random import *
SUITS = ["Diamond", "Club", "Spade", "Heart"]
FACES = list(range(2, 11))+["Jack", "King", "Ace", "Queen"]

User = 0
Dealer = 0
UserList = []
DealerList = []

def card_rate(face):
    if str(face).isdigit():
        return face
    elif face == "Ace":
        return 11
    else:
        return 10

def get_Random_Card():
    global User
    global Dealer
    if User == 0:
        while len(UserList) < 2:
            a = int(random()*len(SUITS))
            suit = SUITS[a]
            b = int(random()*len(FACES))
            face = FACES[b]
            result = suit + " " + str(face)

            if result not in UserList:
                UserList.append(result)
                face = card_rate(face)
                User += face

            if User > 21:
                print("User is lose")
                break

    if Dealer == 0:
        while len(DealerList) < 2:
            a = int(random()*len(SUITS))
            suit = SUITS[a]
            b = int(random()*len(FACES))
            face = FACES[b]
            result = suit + " " + str(face)

            if result not in DealerList:
                DealerList.append(result)
                face = card_rate(face)
                Dealer += face
            if Dealer > 21:
                print("Dealer is lose")

    else:
        a = int(random()*len(SUITS))
        suit = SUITS[a]
        b = int(random()*len(FACES))
        face = FACES[b]
        result = suit + " " + str(face)

        if result not in UserList:
            UserList.append(result)
            face = card_rate(face)
            User += face

        if User > 21:
            print("당신의 카드는 21을 넘었습니다. 당신은 졌습니다.")

def Dealer_get_Card():
    global Dealer
    a = int(random()*len(SUITS))
    suit = SUITS[a]
    b = int(random()*len(FACES))
    face = FACES[b]
    result = suit + " " + str(face)

    if result not in DealerList:
            DealerList.append(result)
            face = card_rate(face)
            Dealer += face
    if Dealer > 21:
            print("딜러가 졌습니다.")



def show():
    print("새로운 게임을 시작합니다.\n")
    print("보여지는 딜러의 카드 : {}".format(DealerList[0]))
    print("당신의 카드 : {0} , {1}".format(UserList[0], UserList[1]))
    print("당신의 점수 : {}".format(User))

    while True:         
        if Dealer < 13 :
            print("딜러가 새로운 카드를 받습니다.")
            print("보여지는 새로운 딜러의 카드 : {}".format(DealerList[len(DealerList)-1]))
            Dealer_get_Card()
            if Dealer > 21 :
                break

        if User > 21:
            break
        get_Card = input("카드를 더 받으시겠습니까? [y/n]")

        if get_Card == "y":

            get_Random_Card()
            print("현재 당신의 카드점수 : {}".format(User))
            print("보유하고 있는 카드의 종류 : {}".format(UserList))

        if get_Card == "n":
            print()
            print("당신의 점수 : {}   딜러의 점수 : {}".format(User, Dealer))
            if Dealer < User:
                print("당신은 이겼습니다.")
                break
            elif Dealer > User:
                print("당신은 졌습니다.")
                break
            elif Dealer == User :
                print("비겼습니다.")
                break


while True :
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    answer = input("새로운 게임을 시작하시겠습니까?[y/n]")
    
    if answer == "y":
        get_Random_Card()
        show()
    elif answer == "n":
        break
