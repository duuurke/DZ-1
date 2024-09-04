class User:
    first_name = 'first_name'
    last_name = 'last_name'

    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def f_name(self):
        print(self.fname)

    def l_name(self):
        print(self.lname)

    def lf_name(self):
        print(self.fname, self.lname)
