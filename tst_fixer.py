class C:

    # Some Comment
    @some_decorator
    @another_decorator  # Another comment
    def x(self):
        """Docstring."""
        print(1234)

    @staticmethod
    def p(z):
        print(z)

    def cl(self):
        self.x()
        self.p(4321)

    def xyz(self, p):
        def somefunc(self, p):
            def anotherfunc(self, p):
                print(p)
            print(p)
        print(p)


C().cl()
c().xyz(12345)
