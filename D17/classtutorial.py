# Camel Case (camelCase): Same as Pascal case but first word is lowercase.
# Snake Case (snake_case): Every word in lowercase, seperated by underscore.
# Pascal Case (PascalCase): First letter of every word capitalized. Class name should be in this case.

'''
class User:
    pass


user_1 = User()
user_1.id = "001"
user_1.username = "Lokesh"

print(user_1.username)
'''


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Lokesh")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
