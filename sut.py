class Dependency:
    def execute(self):
        pass


class Sut:
    def __init__(self, dep: Dependency):
        self.dep = dep

    def execute(self):
        self.dep.execute()
