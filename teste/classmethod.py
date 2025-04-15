class Connection:
    def __init__(self, host='localhost'):
        self.host = "localhost"
        self.user = None
        self.password = None



    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    

#c1 = Connection.create_with_auth('luiz', '1234')
#print(c1.user, c1.password)