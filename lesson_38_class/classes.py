class Client:
    def __init__(self, name, age, service="Cetatenie Romana"):
        self.name = name
        self.age = age
        self.service = service
        print(self.name, self.age, self.service)


if __name__ == '__main__':
    Client("Vasea", 29, "Pasaport")
