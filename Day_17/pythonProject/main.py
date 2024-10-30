from urllib.parse import uses_relative


# Creating "user" class. It serves as a blueprint.
class User:
    def __init__(self,id,username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1



user_1 = User("001","virat")
user_2 = User("002","Dhoni")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


"""
class Car:
    def __init__(self,seats):
        self.seats = seats

mycar = Car(5)

print(mycar.seats) """


