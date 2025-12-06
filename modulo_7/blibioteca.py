# biblioteca.py

class Biblioteca:
    def _init_(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print("\n--- Livros na Biblioteca ---")
        for livro in self.livros:
            print(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower() and livro.disponivel:
                livro.disponivel = False
                print(f"Você emprestou: {livro.titulo}")
                return
        print("Livro não disponível para empréstimo.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower() and not livro.disponivel:
                livro.disponivel = True
                print(f"Você devolveu: {livro.titulo}")
                return
        print("Esse livro não foi emprestado.")