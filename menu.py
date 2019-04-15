class Menu(object):
    def __init__(self, submenus):
        self.submenus = submenus
        self.submenuNum = []
        self._determinar_opcao_num()

    def _determinar_opcao_num(self):
        self.submenus.keys()
        self.submenuNum = list(self.submenus.keys())

    def _handle_opcao(self, option):
        if not option.isnumeric():
            raise ValueError ('Option must be an integer.')
        assert 0 < int(option) <= len(self.submenuNum) or int(option) == 99

    def select(self):
        while True:
            option = input('Digite a opção que deseja:: ')
            try:
                self._handle_opcao(option)
                break
            except:
                print('Opção invalida!')

        option = int(option)
        if option == 99:
            return 99
        keys = self.submenuNum
        self.submenus[keys[option - 1]]()
        return option

    def print_menu(self):
        print('========== Opções ==========')

        keys = self.submenuNum
        for c in range(len(keys)):
            print(f' - {c + 1:>2} {keys[c]}')
        print(' - 99 Sair\n')

    def run(self):
        running = True
        while running:
            self.print_menu()
            if self.select() == 99:
                running = False


if __name__ == '__main__':
    menu = Menu({
        '': 1,
    })
    menu.run()
