class Task:
    def __init__(self, name: str):
        self.name = name
        self.is_done = False

    def write(self):
        if self.is_done:
            sign = 'Done'
        else:
            sign = 'To do'

        return f'{self.name} \t {sign}'

    def set_as_done(self):
        self.is_done = True
