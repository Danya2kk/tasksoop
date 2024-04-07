class SuperStr(str):
    def is_repeatance(self, s):
        if s:
            n = len(self) // len(s)
        else:
            n = len(self) // 1
        return self == n * s

    def is_palindrom(self):
        return self.lower() == self[::-1].lower()


a = SuperStr('abA')
print(a.is_palindrom())
b = SuperStr('   ')
print(b.is_repeatance(' '))
c = SuperStr('123123')
print(c.is_repeatance('123'))
d = SuperStr('abaaba')
print(d.is_repeatance('abaa'))