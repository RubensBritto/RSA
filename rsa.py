def primo(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def swap(m, n):
    aux = n
    n = m
    m = aux
    return m, n
 

def mdc(m, n):
    if n > m:
        m, n = swap(m, n)
    mod = m % n
    if mod == 0:
        return n
    else:
        return mdc(n, mod)


class RSA(object):
    def __init__(self):
        self._pbKey = None
        self._pvtKey = None

    def generate_public_key(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        if (n <= 26):
            return False
        while True:
            e = input('Digite o valor de e: ').strip()
            if e.isnumeric():
                e = int(e)
                if not (mdc(phi, e) == 1) or (e > phi or e < 2):
                    print('e não é primo relativo de phi.')
                    continue
                else:
                    break
            else:
                print('Valor invalido!')
                continue
        with open('public key.txt', 'w') as arq:
            arq.write(str(n) + '\n')
            arq.write(str(e))
        self._pbKey = (n, e)
        return True

    def _read_primo():
        while True:
            n = input(': ').strip()
            if n.isnumeric():
                n = int(n)
                if not primo(n):
                    print("n não é primo.")
                    continue
                break
            else:
                print('Valor invalido!')
        return n

    def input_public_key(self):
        while True:
            print('Digite o valor de p')
            p = self._read_primo()
            print('Digite o valor de q')
            q = self._read_primo()

            if self.generate_public_key(p, q):
                print('Chave publica gerada com sucesso.')
                break
            else:
                print('p * q não atinge o valor minimo(27).')

    @property
    def pbKey(self):
        return self._pbKey

if __name__ == '__main__':
    rsa = RSA()
    rsa.generate_public_key(17, 41)

    print(rsa.pbKey)
