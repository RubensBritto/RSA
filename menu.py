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
        assert 0 < int(opcao) <= len(self.submenuNum)

    def select(self):
        while True:
            opcao = input('Digite a opção que deseja:: ')
            try:
                self._handle_opcao(opcao)
                break
            except:
                print('Opção invalida!')
                

        opcao = int(opcao)
        keys = self.submenuNum
        print(self.submenus[keys[opcao - 1]])
    
    def print_menu(self):
        keys = self.submenuNum
        for c in range(len(keys)):
            print(f'{c + 1} {keys[c]}')

    def run(self):
        self.print_menu()
        self.select()

if __name__ == '__main__':
    menu = Menu({
        'OP1': 1,
    })
    menu.run()