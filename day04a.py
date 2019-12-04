from copy import deepcopy

class Password:
    digits = []
    length = len(digits)

    MAX = 10

    def __init__(self, number: int):
        number = str(number)
        self.digits = [int(character) for character in number]
        self.length = len(self.digits)

    def _increment_next_digit(self, index):
        if index == 0:            
            raise Exception
        self.digits[index] = 0
        self.digits[index - 1] += 1
        if self.digits[index - 1] == self.MAX:
            self._increment_next_digit(index - 1)
    
    def increment(self):
        self.digits[self.length - 1] += 1
        if self.digits[self.length - 1] == self.MAX:
            self._increment_next_digit(self.length - 1)

    def _check_no_decreasing(self):
        for index in range(self.length - 1):
            if self.digits[index] > self.digits[index + 1]:
                return False
        return True

    def _check_pair(self):
        for index in range(self.length - 1):
            if self.digits[index] == self.digits[index + 1]:
                return True
        return False

    def check(self):
        return self._check_no_decreasing() and self._check_pair()

END = 732736
START = 256310
current_password = Password(START)
valid_passwords = 0
for _ in range(END - START):
    if current_password.check():
        valid_passwords += 1
    current_password.increment()
print(valid_passwords)