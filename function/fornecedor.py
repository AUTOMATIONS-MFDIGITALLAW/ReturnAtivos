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

class CreditoSelector:
    def __init__(self, credito):
        self.creditos = {
            "RETURN": "CRÉDITO CEDIDO - RETURN CAPITAL",
            "ATIVOS": " "
        }
        self.credito = credito.strip().lower()

    def get_credito(self):
        return self.creditos.get(
            self.credito,
            f"Credito '{self.credito}' não encontrado na lista."
        )