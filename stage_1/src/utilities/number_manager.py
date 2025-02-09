import requests


class NumManager:
    def __init__(self, num):
        self.num = num

    def _odd_or_even(self):
        if self.num % 2 == 0:
            return "even"
        else:
            return "odd"
    
    def _is_armstrong(self):
        num_str = str(self.num)
        num_len = len(num_str)
        final = sum([int(i) ** num_len for i in num_str])
        return final == self.num
    
    @property
    def is_prime(self) -> bool:
        if self.num < 2:
            return False
        for i in range(2, int(self.num/2) + 1):
            if self.num % i == 0:
                return False
        return True

    @property
    def is_perfect(self) -> bool:
        divisors = [i for i in range(1, self.num) if self.num % i == 0]
        return sum(divisors) == self.num

    @property
    def properties(self) -> list:
        properties = []
        if self._is_armstrong():
            properties.append("armstrong")
        properties.append(self._odd_or_even())
        return properties
    
    @property
    def digit_sum(self) -> int:
        return sum([int(i) for i in str(self.num)])
    
    @property
    def fun_fact(self) -> str:
        url = f"http://numbersapi.com/{self.num}/math"
        r = requests.get(url)
        return r.text if r.status_code == 200 else "Such a boring number"