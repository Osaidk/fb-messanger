class Credential:

    user = ''
    password = ''

    def __init__(self):
    # Constructor code
        pass

    def import_credentials(self):
        with open('credentials.txt', 'r') as file:
            lines = file.readlines()
            self.user = lines[0]
            self.password = lines[1]
            # print(user + ', ' + password)

# c = Credential()
# c.import_credentials()
# print(c.user)