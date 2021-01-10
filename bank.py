class Member:
    def __init__(self, name):
        self.name = name
        self.balance = 100

members = []

def login():

    login_name = input("Member name: ")

    #if login_name in members.name:
    member = [x for x in members if x.name == login_name]
    print(member)
    if member: 
        member = member[0]
        print(f"Welcome back {member.name}!")
    else:
        member = Member(login_name)
        members.append(member)

    return member

def balance(member):
    print(f"Balance: {member.balance}")

if  __name__ == "__main__":
    print("Welecome to Entropy Bank")

    member = login()
    action = ""
    while action != "quit":

        action = input("What would you like to do?")

        if action == "balance":
            balance(member)
        if action == "logout":
            member = login()



