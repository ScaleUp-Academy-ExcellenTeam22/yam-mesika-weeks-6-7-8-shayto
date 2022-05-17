class BaseFile:
    def __init__(self, filename, creator=''):
        self.content = open(filename)
        self.weight = self.content.__sizeof__()
        self.creator = creator

    def read(self, user_name: str):
        if self.creator == user_name:
            return self.content
        return None


class TextFile(BaseFile):
    def count(self, string: str):
        data = self.content.read()
        return data.count(string)


class BinaryFile(BaseFile):
    def get_dimensions(self):
        name = self.content.name
        name.split('.')
        size = 0
        if name[-1] == 'png' or name[-1] == 'jpg':
            return size
        return size


class Directory:
    def __init__(self):
        self.file_list = list()


class SystemManager:
    def __init__(self, manager_user: str, manager_password: str):
        self.administrator = False
        self.manager_user = manager_user
        self.manager_password = manager_password
        self.directory = Directory()

    def log_in(self, manager_user: str, manager_password: str):
        if self.manager_user == manager_user and \
                self.manager_password == manager_password:
            self.administrator = True
        return self.directory