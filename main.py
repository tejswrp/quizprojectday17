class User:
    def __init__(self, user_id, username):    #this is a cunsuctor to define the attributes of the object which got created by this class
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User('001','Teja')
print(user_1.username)
print(user_1.followers)

user_2 = User('002','Swaroop')
print(user_2.id)

