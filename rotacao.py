
import numpy as np

class RotacaoUtil:
    @staticmethod
    def rodar_eixo_x(angulo):
        """
        Cria uma matriz de rotação para rotacionar um ponto ou objeto em torno do eixo X.

        :param angulo: Ângulo de rotação em radianos.
        :return: Uma matriz numpy 3x3 que representa a rotação em torno do eixo X.

        A matriz de rotação no eixo X é construída usando o cosseno e o seno do ângulo fornecido,
        afetando as coordenadas Y e Z enquanto X permanece inalterado.
        """
        cos, sen = np.cos(angulo), np.sin(angulo)
        return np.array([
            [1, 0, 0],
            [0, cos, -sen],
            [0, sen, cos]
        ])
    
    @staticmethod
    def rodar_eixo_y(angulo):
        """
        Cria uma matriz de rotação para rotacionar um ponto ou objeto em torno do eixo Y.

        :param angulo: Ângulo de rotação em radianos.
        :return: Uma matriz numpy 3x3 que representa a rotação em torno do eixo Y.

        A matriz de rotação no eixo Y altera as coordenadas X e Z com base no cosseno e seno do ângulo,
        enquanto a coordenada Y permanece constante.
        """
        cos, sen = np.cos(angulo), np.sin(angulo)
        return np.array([
            [cos, 0, sen],
            [0, 1, 0],
            [-sen, 0, cos]
        ])
    
    @staticmethod
    def rodar_eixo_z(angulo):
        """
        Cria uma matriz de rotação para rotacionar um ponto ou objeto em torno do eixo Z.

        :param angulo: Ângulo de rotação em radianos.
        :return: Uma matriz numpy 3x3 que representa a rotação em torno do eixo Z.

        Esta matriz de rotação afeta as coordenadas X e Y, utilizando o cosseno e seno do ângulo fornecido,
        enquanto a coordenada Z permanece inalterada.
        """
        cos, sen = np.cos(angulo), np.sin(angulo)
        return np.array([
            [cos, -sen, 0],
            [sen, cos, 0],
            [0, 0, 1]
        ])
    
    @staticmethod
    def aplicar_rotacao(vertices, angulo_x, angulo_y, angulo_z):
        """
        Aplica uma rotação sequencial aos vértices em torno dos eixos x, y e z.

        :param vertices: Uma matriz numpy de vértices a serem rotacionados.
        :param angulo_x: Ângulo de rotação em torno do eixo x (em radianos).
        :param angulo_y: Ângulo de rotação em torno do eixo y (em radianos).
        :param angulo_z: Ângulo de rotação em torno do eixo z (em radianos).
        :return: Uma nova matriz de vértices rotacionados.

        O método realiza a rotação dos vértices aplicando sucessivamente as matrizes de rotação dos eixos x, y e z.
        Cada matriz de rotação é calculada com base nos ângulos fornecidos e aplicada através de multiplicação de matrizes.
        """
        vertices_rotacionados = vertices.dot(RotacaoUtil.rodar_eixo_x(angulo_x))
        vertices_rotacionados = vertices_rotacionados.dot(RotacaoUtil.rodar_eixo_y(angulo_y))
        vertices_rotacionados = vertices_rotacionados.dot(RotacaoUtil.rodar_eixo_z(angulo_z))
        return vertices_rotacionados