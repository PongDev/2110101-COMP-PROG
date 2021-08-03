realname = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nickname = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]

n = int(input())
for i in range(n):
    data = input()
    if data in realname:
        print(nickname[realname.index(data)])
    elif data in nickname:
        print(realname[nickname.index(data)])
    else:
        print("Not found")
