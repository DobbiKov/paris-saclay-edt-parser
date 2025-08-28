class Event:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"{self.content}"
    def __repr__(self) -> str:
        return self.__str__()
