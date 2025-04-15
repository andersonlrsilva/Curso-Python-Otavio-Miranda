class Connection:
    def __init__(self, host='localhost'):
        self.hostt = host
        self.user = None
        self.password = None

    #Configura o parametro user
    def set_user(self, user):
        self.user = user

    #configura o parametro password
    def set_password(self, password):
        self.password = password
        
    @classmethod
    def create_with_aut(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection




    @staticmethod
    def log(msg):
        print('LOG:', msg)


    
def connetion_log(msg):
    print('LOG:',msg)



c1 = Connection.create_with_aut('anderson', '1234')
print(Connection.log('Essa e a mensagem'))
#c1 = Connection()
#c1.set_user('Anderson')
#c1.set_password('1234')
print(c1.user)
print(c1.password)
