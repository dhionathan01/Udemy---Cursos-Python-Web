class AcessoAoDisco:
    def __init__(self, nome_arquivo):
        self.__nome_arquivo = nome_arquivo
        
    def abrir(self):
        with open(self.__nome_arquivo) as file_open:
            return file_open.readlines()
            
    def gravar(self, data, completo=False):
        if completo:
            self.__gravarCompleto(data)
        else:
            self.__gravarParcial(data)
    
    def __gravarParcial(self, data):
        with open(self.__nome_arquivo, "a") as file_open:
            file_open.write(f"{data}\n")
    
    def __gravarCompleto(self, data):
        with open(self.__nome_arquivo, "w") as file_open:
            file_open.truncate()
            for value in data:
                file_open.write(f"{value}\n")