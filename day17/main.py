class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user1 = User('001', 'margarita')
user2 = User('002', 'Maria')
user1.follow(user2)
print(user1.following, user2.followers)
