import math
import random
import string
from typing import List


class RSA:
    def _gcd(self, a: int, h: int) -> int:
        temp: int

        while True:
            temp = a % h

            if temp == 0:
                return h

            a = h
            h = temp

    def _egcd(self, a: int, b: int):
        x, y, u, v = 0, 1, 1, 0

        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
            gcd = b

        return gcd, x, y

    def _is_prime(self, num: int):
        if num <= 1:
            return False

        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False

        return True

    def _find_d(self) -> int:
        _, d, _ = self._egcd(self._e, self._phi)
        return d

    def _find_e(self) -> int:
        e = 2

        while e < self._phi:
            if self._gcd(e, self._phi) == 1:
                break
            else:
                e += 1

        return e

    def _find_n(self) -> int:
        return self._p * self._q

    def _find_phi(self) -> int:
        return (self._p - 1) * (self._q - 1)

    def _get_prime_number(self, max: int, but: int = 0) -> int:
        primes: List[int] = list(filter(self._is_prime, range(2, max)))
        prime = random.choice(primes)

        while but == prime:
            prime = random.choice(primes)

        return prime

    def _crypt(self, m: int) -> int:
        return pow(m, self._e, self._n)

    def _decrypt(self, c: int) -> int:
        return pow(c, self._d, self._n)

    def cipher(self, plain_text: str) -> int:
        tabled_list = [self._table.index(char.upper()) for char in plain_text]
        ciphed_list = [self._crypt(value) for value in tabled_list]

        return ciphed_list

    def decipher(self, ciphed_list: List[int]) -> List[int]:
        deciphed_list = [self._decrypt(value) for value in ciphed_list]
        deciphed_text = ''.join([self._table[value] for value in deciphed_list])

        return deciphed_text

    def __init__(self) -> None:
        super().__init__()

        self._p = self._get_prime_number(100)
        self._q = self._get_prime_number(100, self._p)
        self._n = self._find_n()
        self._phi = self._find_phi()
        self._e = self._find_e()
        self._d = self._find_d()
        self._table = [letter for letter in string.ascii_uppercase[:26]]

        print("p", self._p)
        print("q", self._q)
        print("n", self._n)
        print("phi", self._phi)
        print("e", self._e)
        print("d", self._d)
        print()


if __name__ == "__main__":
    rsa = RSA()
    print("VALOR CLARO VICTOR")

    c = rsa.cipher("VICTOR")
    print("VALOR CIFRADO", c)

    m = rsa.decipher(c)
    print("VALOR DECIFRADO", m)
