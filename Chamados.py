class Chamado:

    def __init__(
        self,
        id,
        solicitante,
        titulo,
        descricao,
        status,
        criado_em=None
    ):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def atualizar_status(self, novo_status):
        self.status = novo_status

    def __str__(self):
        return f"Chamado {self.id}: {self.titulo} - {self.status}"