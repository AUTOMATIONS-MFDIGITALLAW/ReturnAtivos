class FornecedorSelector:
    def __init__(self, fornecedor):
        self.fornecedores = {
            "tricard": "TRICARD SERVIÇOS DE INTERMEDIAÇÃO DE CARTÕES DE CRÉDITO LTDA - 05.045.717/0001-73",
            "tribanco": "BANCO TRIÂNGULO S/A - 17.351.180/0001-59"
        }
        self.fornecedor = fornecedor.strip().lower()

    def get_fornecedor(self):
        return self.fornecedores.get(
            self.fornecedor,
            f"Fornecedor '{self.fornecedor}' não encontrado na lista."
        )

#..............

class TratativaSelector:
    def __init__(self, tratativa):
        self.tratativas = {
            "tricard": "TRICARD SERVIÇOS DE INTERMEDIAÇÃO DE CARTÕES DE CRÉDITO LTDA - 05.045.717/0001-73",
            "tribanco": "BANCO TRIÂNGULO S/A - 17.351.180/0001-59"
        }
        self.tratativa = tratativa.strip().lower()

    def get_tratativa(self):
        return self.tratativas.get(
            self.tratativa,
            f"Fornecedor '{self.tratativa}' não encontrado na lista."
        )