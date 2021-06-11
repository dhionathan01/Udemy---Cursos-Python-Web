
class Tipo_de_Avaliacao:
    indice = None

    def tipo_av(self, indice):
        self.indice = str(indice)
        if self.indice == '1':
            return 'AV1'
        elif self.indice == '2':
            return 'AV2'
        elif self.indice == '3':
            return 'AV3'
        elif self.indice == '4':
            return 'AVD'



