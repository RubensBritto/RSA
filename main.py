#minimum required version python 3.7.0
import rsa, menu

codificacao = rsa.RSA()
submenus = {
    'Gerar chave publica': codificacao.input_public_key,
    'Encriptar': codificacao.input_encrypt,
    'Desencriptar': codificacao.input_decrypt,
}

menu = menu.Menu(submenus)
menu.run()
