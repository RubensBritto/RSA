def eh_primo(n):
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

    @staticmethod
    def _handle_value(n):
        if not n.isnumeric():
            raise TypeError ('The value must be an integer.')

    def generate_public_key(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        if (n <= 26):
            return False
        while True:
            e = input('Digite o valor de e: ').strip()
            try:
                self._handle_value(e)
                e = int(e)
                if not (mdc(phi, e) == 1) or (e > phi or e < 2):
                    print('e não é primo relativo de phi.')
                    continue
                break
            except:
                print('Valor invalido!')
        with open('public key.txt', 'w') as arq:
            arq.write(str(n) + '\n')
            arq.write(str(e))
        self._pbKey = (n, e)
        return True
    
    def input_public_key(self):
       pass
       # TODO: fazer essa função ai e midificar generate_public_key para
       # receber o e tambem 

    @property
    def pbKey(self):
        return self._pbKey
        
rsa = RSA()
rsa.generate_public_key(17, 41)

print(rsa.pbKey)
