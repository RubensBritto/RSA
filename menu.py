class Menu(object):
    def __init__(self, submenus):
        self.submenus = submenus
        self.submenuNum = []
        self._determinar_opcao_num()

    def _determinar_opcao_num(self):
        self.submenus.keys()
        self.submenuNum = list(self.submenus.keys())

    def _handle_opcao(self, opcao):
        if not opcao.isnumeric():
            raise ValueError ('Option must be an integer.')
        assert 0 < int(opcao) <= len(self.submenuNum) or int(opcao) == 99

    def select(self):
        while True:
            opcao = input('Digite a opção que deseja:: ')
            try:
                self._handle_opcao(opcao)
                break
            except:
                print('Opção invalida!')

        opcao = int(opcao)
        if opcao == 99:
            return
        keys = self.submenuNum
        self.submenus[keys[opcao - 1]]()

    def print_menu(self):
        print('========== Opções ==========')

        keys = self.submenuNum
        for c in range(len(keys)):
            print(f' - {c + 1} {keys[c]}')
        print(' - 99 Sair\n')

    def run(self):
        self.print_menu()
        self.select()


if __name__ == '__main__':
    menu = Menu({
        '': 1,
    })
    menu.run()
