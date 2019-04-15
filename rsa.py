import math

def is_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def swap(m, n):
    aux = n
    n = m
    m = aux
    return m, n

def gcd(m, n):
    if n > m:
        m, n = swap(m, n)
    mod = m % n
    if mod == 0:
        return n
    else:
        return gcd(n, mod)


class RSA(object):
    def __init__(self):
        self._public_key = None
        self._private_key = None
        self._alfabeto = [chr(c) for c in range(65, 91)]
        self._alfabeto.append(' ')


    def generate_public_key(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        if (n <= 26):
            return False
        while True:
            e = input('Digite o valor de e: ').strip()
            if e.isnumeric():
                e = int(e)
                if not (gcd(phi, e) == 1) or (e > phi or e < 2):
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

    def generate_private_key(self, p, q, e):
        n = p * q
        d = 2;
        phi = (p - 1) * (q - 1)
        if n <= 26:
            return False

        while True:
            value = (d * e) % phi
            value = int(value)
            if value == 1:
                break
            d+=1

        try:
            with open('private_key.txt', 'w') as file:
                file.write(str(n) + '\n')
                file.write(str(d))
        except:
            print('Erro na escrita')


        self._private_key = (n, d)

        return True

    @staticmethod
    def _read_prime():
        while True:
            n = input(': ').strip()
            if n.isnumeric():
                n = int(n)
                if not is_prime(n):
                    print("O valor não é primo.")
                    continue
                break
            else:
                print('Valor invalido!')
        return n

    def encrypt(self, message):
        n, e = self._public_key

        try:
            with open('encrypted_text.txt', 'w') as file:
                for i in range(len(message)):
                    caracter = message[i]
                    value = ( ord(caracter) ** e ) % n
                    value = int(value)
                    file.write(str(value))
                    if i != len(message) - 1:
                        file.write(',')
        except:
            print('Erro ao escrever no arquivo!')
        else:
            print('Encriptado com sucesso.\n')

    def decrypt(self):
        decrypted_text = ""

        try:
            with open('private_key.txt', 'r') as private_key_file:
                private_key_list = private_key_file.read().split('\n')

                n = int(private_key_list[0])
                d = int(private_key_list[1])

        except:
            print('erro na leitura')

        try:
            print('Mensagem:')
            with open('encrypted_text.txt', 'r') as file:
                decrypted_text = ''
                encrypted_text = file.read().split(',')

                for value in encrypted_text:
                    value = int(( int(value) ** d ) % n)
                    decrypted_text += chr(value)
            print(decrypted_text)
            print()
        except:
            print('Erro ao ler o arquivo!')
        else:
            print('Desencriptado com sucesso.\n')

    def input_public_key(self):
        while True:
            print('Digite o valor de p')
            p = self._read_prime()
            print('Digite o valor de q')
            q = self._read_prime()

            if self.generate_public_key(p, q):
                print('Chave publica gerada com sucesso.\n')
                break
            else:
                print('p * q não atinge o valor minimo(27).')

    def input_encrypt(self):
        error = False
        while True:
            message = input('Digite a mensagem: ')
            for c in message:
                if not self._alfabeto:
                    error = True
                    break
            if error:
                error = False
                continue
            break

        while True:
            public_key = input('Digite a chave publica (xxx,xx): ').strip()
            if public_key[0] == '(':
                public_key = public_key[1:len(public_key) - 1]

            if ',' in public_key:
                pub_key = public_key.split(',')
            else:
                print('Chave invalida.')
                continue
            if pub_key[0].isnumeric() and pub_key[1].isnumeric():
                self._public_key = (int(pub_key[0]), int(pub_key[1]))
            else:
                print('chave invalida.')
                continue
            break

        self.encrypt(message)

    def input_decrypt(self):
        self.input_public_key()
        self.decrypt()


if __name__ == '__main__':
    rsa = RSA()
    rsa.input_public_key()
"""
    rsa.generate_private_key(17, 41, 13)
    rsa.decrypt()
    print(rsa.public_key)
"""
