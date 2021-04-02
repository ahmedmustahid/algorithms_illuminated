# iterator protocol
class UCIter:
    def __init__(self, text):
        self.text = text.upper()
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            result = self.text[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

uc= UCIter("abcde")

a=next(uc)
print("here")
for x in uc:
    print(x)


