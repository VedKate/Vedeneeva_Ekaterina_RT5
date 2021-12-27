class Unique(object):
    def __init__(self, items, **kwargs):
        if kwargs.get('ignore_case'):  # если дан флаг
            for i, val in enumerate(items):  # переводим все str в нижний регистр
                if type(val) == str:
                    items[i] = val.lower()
        self.items = items

    def __next__(self):
        a = self.l[-1]
        while self.n < len(self.items) and self.items[self.n] in self.l:
            self.n += 1
        if self.n > len(self.items):
            raise StopIteration('Достигнут предел итерации')
        elif self.n < len(self.items):
            self.l.append(self.items[self.n])
        self.n += 1
        return a

    def __iter__(self):
        self.l = []
        self.n = 1
        self.l.append(self.items[0])
        return self
