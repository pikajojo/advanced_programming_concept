class Patient:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def print_patient(self):
        information = 'patient // ' + self.name + '// born // ' + self.dob
        print(information)


if __name__ == '__main__':
    patient1 = Patient("lll","2011-4-16")
    