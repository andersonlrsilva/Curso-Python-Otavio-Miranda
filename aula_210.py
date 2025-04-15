

#method - self, método de instância
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None


    def set_user(self,user):
        self.user = user

    def set_password(self, password):
        self.password = password


#classmethod
    @classmethod
    def creat_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection




#staticmethod
    def log(msg):
        print('LOG:', msg)



def connection_log(msg):
    print('LOG:', msg)





#method - self, método de instância
c1 = Connection()
c1.set_user('luiz')
c1.set_password('1234')
print(c1.user)
print(c1.password)

#classmethod
c2 = Connection.creat_with_auth('luiz', '1234')


#staticmethod
print(Connection.log('Essa e minha mensagem de log'))
print(connection_log('Essa e minha mensagem de log'))

