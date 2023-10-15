class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.sizes = 0

    def __str__(self):
        return "🍪" * self.sizes

    def deposit(self, n):
        if self.sizes + n > self.capacity:
            raise ValueError("Deposit error")
        self.sizes = self.sizes + n

    def withdraw(self, n):
        if n > self.sizes:
            raise ValueError("Withdraw error")
        self.sizes = self.sizes - n
        print('Hello_Guys')

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("@capacity.setter error")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("@size.setter error")
        self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()