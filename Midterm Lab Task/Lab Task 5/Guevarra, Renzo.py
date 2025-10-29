#User class
class User:
    def __init__(self, first_name, last_name, followers_count, friends_name):
        self.first_name = first_name
        self.last_name = last_name
        self.followers_count = followers_count
        self.friends_name = friends_name

    def introduce_self(self):
        print(f"Hi I am {self.first_name} {self.last_name}")

    def view_full_profile(self):
        print(f"Profile Name is: {self.first_name} {self.last_name} with {self.followers_count} followers")
        print("Your friends are:", ' '.join(self.friends_name))
        print()


#TestUser class
class TestUser:
    def __init__(self):
        self.user_list = []

    def add_user(self):
        while True:
            insert = input("Insert a Record? [y/n]: ").lower()
            if insert == 'n':
                break

            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            followers = int(input("Followers: "))

            print("Friends:")
            friends = []
            for i in range(3):
                friend = input()
                friends.append(friend)

            # Create a new User object
            user = User(first_name, last_name, followers, friends)
            self.user_list.append(user)

    def show_records(self):
        print("\nHere are the Records....\n")
        for user in self.user_list:
            user.introduce_self()
            user.view_full_profile()

        print(f"There are currently {len(self.user_list)} Members in the Social Media page")


#Main Program
test = TestUser()
test.add_user()
test.show_records()
