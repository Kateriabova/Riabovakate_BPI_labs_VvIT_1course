import hashlib

class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        hash = username + password
        hash = hashlib.md5(hash.encode())
        hash = hash.hexdigest()
        self.__password_login_hash = hash

    def check_password(self, password):
        login = self.username
        hash = login + password
        hash = hashlib.md5(hash.encode())
        hash = hash.hexdigest()
        if hash == self.__password_login_hash:
            return True
        else:
            return False

    def set_password(self, new_password):
        login = self.username
        hash = login + new_password
        hash = hashlib.md5(hash.encode())
        hash = hash.hexdigest()
        self.__password = new_password
        self.__password_login_hash = hash

Vasya = UserAccount("Vasya_Petrov", "vasyundra_2006@gamil.com", "123456")
print(Vasya.check_password('123456'))
Vasya.set_password("qwerty")
print(Vasya.check_password('123456'))
print(Vasya.check_password('qwerty'))
print(Vasya.__password)
