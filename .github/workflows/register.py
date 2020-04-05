class Test:
    num_user = 0
    ids = {}

    def __init__(self, num):
        self.num = num


    def register():
        print("===========================")
        print("         Register")
        print("===========================")
        id = input("ID (more than 7 letters) : ")
        while len(id) < 7:
            id = input("Too Short!!, New ID (more than 7 letters) : ")
        else:
            print("Your ID is ", id )
            password = input("PASSWORD (more than 7 letters) : ")
            while len(password) < 7:
                password = input("Too Short!!, New PASSWORD (more than 7 letters) : ")
            else:
                print("Congratulations!!! You are successfully registered!")
    
        Test.ids[id] = password
        Test.num_user += 1
        print("Number of Users : ", Test.num_user)

    def login():
        print("=========================")
        print("        Log In")
        print("=========================")
        id = input("ID : ")
        password = input("PASSWORD : ")
        while id not in Test.ids.keys():
            print("Wrong ID!!!")
            id = input("ID : ")
            password = input("PASSWORD: ")
        else:
            while Test.ids[id] != password:
                print("Wrong Password!!")
                password = input("PASSWORD : ")
            else:
                print("You are successfully Logged in")

        

A = Test.register()
print()
print()
print()
B = Test.register()
print()
print()
print()


Test.login()
