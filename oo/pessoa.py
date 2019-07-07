class Pessoa:  # classe sempre se inicia com  letra maiuscula
    # metodo é uma função que pertence a uma classe e portanto, sempre está conectada a um objeto.
    def cumprimentar(self):
        return f'Olá ! {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())