import string
data = input()

class alphabet_counter():
    def __init__(self, data):
        self.data = data
        
        self.stored_nums = ''
        self.alphabets = []
        self.multiple_dict = {0: 1}
        self.numbers = [str(num) for num in range(10)]
        self.level = 0

        self.char_dict = {}
        for alphabet in string.ascii_lowercase:
            self.char_dict[alphabet] = 0

    def count_alphabets(self):
        for char in self.data:
            if char in self.char_dict:
                self.level += 1

                if self.stored_nums:
                    self.multiple_dict[self.level] = int(self.stored_nums)
                multiple = 1
                for num in self.multiple_dict.values():
                    multiple *= num
                self.alphabets.append((char, multiple))
                if self.level == 0:
                    self.multiple_dict[0] = 1
                self.stored_nums = ''

                self.level -= 1
                self.multiple_dict[self.level + 1] = 1
            elif char == '(':
                self.level += 1
                self.multiple_dict[self.level] = int(self.stored_nums)
                self.stored_nums = ''
            elif char == ')':
                self.level -= 1
                self.multiple_dict[self.level + 1] = 1
            elif char in self.numbers:
                self.calc_multiple(char)

        return self.calc_result()

    def calc_multiple(self, char):
        self.stored_nums += char

    def calc_result(self):
        for char, count in self.alphabets:
            self.char_dict[char] += count
        return self.char_dict
    

ac = alphabet_counter(data)

result = ac.count_alphabets()
for key, value in result.items():
    print(f'{key} {value}')
