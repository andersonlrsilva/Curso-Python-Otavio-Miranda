class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.user = None

######################
#Method
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
            self.password = password




c1 = Connection()
c1.set_user('luiz')
c1.set_password(1234)



print(c1.user, c1.password)