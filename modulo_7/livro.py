# livro.py

class Livro:
    def _init_(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def _str_(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} ({status})"