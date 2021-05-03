class Aviao:
    nome = 'A3FGT'
    compania = 'Latam'
    latitude_atual = 0
    longitude_atual = 0
    destino_do_aviao = []
    localizao_atual = []
    ponto_de_partida = []
    distancia_percorrida = []

    def __init__(self, latitude_atual, longitude_atual):
        self.latitude_atual = latitude_atual
        self.longitude_atual = longitude_atual
        self.localizao_atual.append(latitude_atual)
        self.localizao_atual.append(longitude_atual)
        self.ponto_de_partida.append(latitude_atual)
        self.ponto_de_partida.append(longitude_atual)
        print(f'Posição inicial Definida: \n'
              f' Latitude: {latitude_atual} \n'
              f' Longitude: {longitude_atual} \n')

    def destino(self, latitude, longitude):
        self.destino_do_aviao.append(latitude)
        self.destino_do_aviao.append(longitude)
        print(f'Destino Defininido:\n'
              f' Latitude: {self.destino_do_aviao[0]}\n'
              f' Longitude: {self.destino_do_aviao[1]}\n')


class CoordenadaGeografica(Aviao):

    def update_local(self, latitude, longitude):
        self.localizao_atual.clear()
        self.localizao_atual.append(latitude)
        self.localizao_atual.append(longitude)
        print(f'Localização atual:\n'
              f' Latitude: {self.localizao_atual[0]}\n'
              f' Longitude: {self.localizao_atual[1]}\n')

    def calcular_distancia_percorrida(self):
        distancia_latitude = self.localizao_atual[0] - self.ponto_de_partida[0]
        self.distancia_percorrida.append(distancia_latitude)
        distancia_longitude = self.localizao_atual[1] - self.ponto_de_partida[1]
        self.distancia_percorrida.append(distancia_longitude)
        print(f'Distancia percorrida desde Origem:\n'
              f' Você se Moveu {self.distancia_percorrida[0]} Pontos de Latitude \n'
              f' Você se Moveu {self.distancia_percorrida[1]} Pontos de Longitude \n')

    def calcular_distancia_do_objetivo(self):
        distancia_do_objetivo = [self.destino_do_aviao[0] - self.localizao_atual[0],
                                 self.destino_do_aviao[1] - self.localizao_atual[1]]
        print(f'Distancia do Destino:\n Latitude:{distancia_do_objetivo[0]}\n'
              f' Longitude: {distancia_do_objetivo[1]}')


aviao = Aviao(30, 50)
aviao.destino(87, 166)
coordenada = CoordenadaGeografica(aviao.latitude_atual, aviao.longitude_atual)
coordenada.update_local(56, 89)
coordenada.calcular_distancia_do_objetivo()
