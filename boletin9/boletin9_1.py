class Libro:
    def __init__(self, titulo, autor, ano, numPaginas, valoracion):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._numPaginas = numPaginas
        self._valoracion = valoracion

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_ano(self):
        return self._ano

    def get_numPaginas(self):
        return self._numPaginas

    def get_valoracion(self):
        return self._valoracion


    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_autor(self, autor):
        self._autor = autor

    def set_ano(self, ano):
        self._ano = ano

    def set_numPaginas(self, numPaginas):
        self._numPaginas = numPaginas

    def set_valoracion(self, valoracion):
        self._valoracion = valoracion


    titulo = property(get_titulo, set_titulo)
    autor = property(get_autor, set_autor)
    ano = property(get_ano, set_ano)
    numPaginas = property(get_numPaginas, set_numPaginas)
    valoracion = property(get_valoracion, set_valoracion)


    def amosarLibro(self):
        return (
            f"Título: {self._titulo}\n"
            f"Autor: {self._autor}\n"
            f"Ano: {self._ano}\n"
            f"Número de páxinas: {self._numPaginas}\n"
            f"Valoración: {self._valoracion}"
        )

class Principal:
    def main(self):
        libro = Libro("La Celestina", "Fernando de Rojas", 1449, 336, 9.5)
        print("Información do libro:")
        print(libro.amosarLibro())

if __name__ == "__main__":
    creacion = Principal()
    creacion.main()
