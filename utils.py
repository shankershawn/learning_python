class Utils:
    def find_max(self, numbers):
        max_num = numbers[0]
        for number in numbers:
            if number > max_num:
                max_num = number
        return max_num
