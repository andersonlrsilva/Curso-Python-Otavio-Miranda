import contas
import pessoas


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoas] | None = None,
        contas: list[contas.Conta] | None = None,

    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):  # type: ignore
        if conta.agencia in self.agencias:  # type: ignore
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):  # type: ignore
        if cliente in self.clientes:
            print('checa_clientes', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):  # type: ignore
        if conta in self.contas:
            print('checa_conta', True)
            return True
        print('checa_conta', False)
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):  # type: ignore
        if conta is cliente.consta:  # type: ignore
            print('ccheca_se_conta_e_do_cliente', True)
            return True
        print('checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(self, cliente: pessoas.Pessoas, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'
