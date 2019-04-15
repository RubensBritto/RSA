import rsa, menu

codificacao = rsa.RSA()
submenus = {
    'Gerar chave publica': codificacao.input_public_key,
}

menu = menu.Menu(submenus)
menu.run()
