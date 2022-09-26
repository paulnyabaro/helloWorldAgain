class Week:
    def __init__(self):
        self.days = {1:'Monday', 2: "Tuesday", 3:"Wednesday", 4: "Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
        self._index = 1

    def __iter__(self):
        self._index = 1
        return self

    def __next__(self):
        if self._index < 1 | self._index > 7:
            raise StopIteration
        else:
            ret_value = self.days[self._index]
            self._index += 1
            return ret_value

wk = Week()
for day in wk:
    print(day)