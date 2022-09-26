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
#
# This style of implementing an
# iterator is commonly found on the internet, but it is not a recommended approach and is
# considered a bad design. The reason is that when we use it in the for loop, we get back
# the main object as an iterator as we implemented __iter__ and __next__ in the
# same class. This can give unpredictable results