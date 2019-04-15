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
 
    @staticmethod
    def _handle_value(n):
        if not n.isnumeric():
            raise TypeError ('The value must be an integer.')
 
    def generate_public_key(self, p, q, e):
        n = p * q
        phi = (p - 1) * (q - 1)
       
        if (n <= 26):
            return False
       
        try:
            e = int(e)
            if not (gcd(phi, e) == 1) or (e > phi or e < 2):
                print('e não é primo relativo de phi.')
        except:
            print('Valor invalido!')
 
        try:
            with open('public_key.txt', 'w') as file:
                file.write(str(n) + '\n')
                file.write(str(e))
        except:
            print('falha na escrita')
 
 
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
 
    def input_public_key(self):
       pass
       # TODO: fazer essa função ai e midificar generate_public_key para
       # receber o e tambem
 
    def encrypt(self, message):
        n, e = self._public_key
 
        try:
            with open('encrypted_text.txt', 'w') as file:
                for i in range(len(message)):
                    caracter = message[i]
                    value = ( ord(caracter) ** e ) % n
                    value = int(value)
                    file.write(str(value))
                    print('ta entrando')
                    if i != len(message) - 1:
                        file.write(',')
        except:
            print("Erro ao escrever no arquivo!")
     
 
 
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
            with open('encrypted_text.txt', 'r') as file:
                decrypted_text = ''
                encrypted_text = file.read().split(',')
               
                for value in encrypted_text:
                    value = int(( int(value) ** d ) % n)
                    decrypted_text += chr(value)
            print(decrypted_text)
        except:
            print("Erro ao ler o arquivo!")
       
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
        

    @property
    def public_key(self):
        return self._public_key


if __name__ == '__main__':
    rsa = RSA()
    rsa.generate_public_key(17, 41, 13)
    rsa.input_encrypt()
    
    rsa.generate_private_key(17, 41, 13)
    rsa.decrypt()
    print(rsa.public_key)