import pygame
import sys
import numpy as np

from cores import CoresUtil
from movimentacao import MovimentacaoUtil
from rotacao import RotacaoUtil

pygame.init()
LARGURA_TELA, ALTURA_TELA = 800, 500
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
clock = pygame.time.Clock()
TAMANHO_CUBO = 80

cores = [
    CoresUtil.AMARELO, 
    CoresUtil.AZUL, 
    CoresUtil.LARANJA, 
    CoresUtil.ROXO, 
    CoresUtil.VERDE, 
    CoresUtil.VERMELHO
]

vertices = np.array([
    [1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
    [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]
]) * TAMANHO_CUBO

arestas = [
    (0, 1), (1, 3), (3, 2), (2, 0), 
    (4, 5), (5, 7), (7, 6), (6, 4), 
    (0, 4), (1, 5), (2, 6), (3, 7)
]

def desenhar_cube(vertices, index_cor):
    """
    Desenha um cubo na tela utilizando linhas para conectar os vértices conforme definido pelas arestas.

    :param vertices: Uma matriz numpy contendo as coordenadas dos vértices do cubo projetados na tela 2D.
    :param index_cor: Um índice inicial usado para selecionar a cor inicial da linha a partir da lista global 'cores'.

    O método percorre todas as arestas do cubo, que são pares de índices indicando quais vértices estão conectados. Para cada aresta:
    - Extrai os pontos (vértices) conectados pela aresta.
    - Desenha uma linha entre esses dois pontos na tela.
    - A cor da linha é determinada pelo índice de cor atual, que é atualizado circularmente pela lista de cores disponíveis.
    - Incrementa o índice de cor para a próxima linha a ser desenhada.

    As cores são selecionadas ciclicamente usando o operador módulo para evitar erros de índice fora de alcance.

    Note: As variáveis 'tela' e 'cores' são esperadas como variáveis globais ou externas acessíveis pelo método.
    """
    for umaAresta in arestas:
        pontos = vertices[umaAresta, :]
        pygame.draw.line(tela, cores[index_cor % len(cores)], pontos[0], pontos[1], 5)
        index_cor += 1

def realiza_eventos_interacao(pos_x, pos_y, angle_x, angle_y):
    """
    Processa eventos de interação do usuário, atualizando a posição e os ângulos de um objeto na tela com base nos inputs do teclado e movimentos do mouse.

    :param pos_x: Posição atual no eixo x do objeto.
    :param pos_y: Posição atual no eixo y do objeto.
    :param angle_x: Ângulo atual de rotação em torno do eixo x.
    :param angle_y: Ângulo atual de rotação em torno do eixo y.
    :return: Uma tupla (pos_x, pos_y, angle_x, angle_y) representando as novas posições e ângulos após processar os eventos.

    Processamento dos eventos:
    - QUIT: Fecha o jogo e termina o programa se o evento de saída (fechar a janela) for acionado.
    - KEYDOWN: Atualiza a posição do objeto com base na tecla pressionada, utilizando métodos específicos de movimentação.
    - MOUSEMOTION: Atualiza os ângulos de rotação do objeto se o botão direito do mouse estiver pressionado e o mouse movido.

    O método utiliza funções auxiliares de `MovimentacaoUtil` para tratar os eventos específicos de teclado e movimentos do mouse.
    """
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            pos_x, pos_y = MovimentacaoUtil.realiza_click_tecla(pygame, evento.key, pos_x, pos_y)
        if evento.type == pygame.MOUSEMOTION:
            angle_x, angle_y = MovimentacaoUtil.realiza_segura_botao_direito_arrasta_mouse(pygame, evento, angle_x, angle_y)
    return pos_x, pos_y, angle_x, angle_y

def calcular_vertices_projetados(vertices_transformados, vertices_projetados, perspectiva):
    """
    Calcula a projeção dos vértices 3D para 2D usando uma projeção em perspectiva.

    :param vertices_transformados: np.array com vértices 3D transformados.
    :param perspectiva: Distância da câmera que afeta a projeção em perspectiva.
    :return: np.array com vértices 2D projetados.
    """
    for i, (x, y, z) in enumerate(vertices_transformados):
        factor = z / perspectiva + 1  # Calcula o fator de ajuste com base na profundidade z e perspectiva
        vertices_projetados[i] = [x / factor, y / factor]
    return vertices_projetados

def main():
    angulo_x, angulo_y, angulo_z = 0, 0, 0
    pos_x, pos_y = LARGURA_TELA // 2, ALTURA_TELA // 2

    while True:
        pos_x, pos_y, angulo_x, angulo_y = realiza_eventos_interacao(pos_x, pos_y, angulo_x, angulo_y)
        tela.fill((0, 0, 0))

        vertices_transformados = RotacaoUtil.aplicar_rotacao(vertices, angulo_x, angulo_y, angulo_z)
        vertices_transformados += np.array([pos_x, pos_y, 0])
        vertices_projetados = np.zeros((8, 2))

        calcular_vertices_projetados(vertices_transformados, vertices_projetados, 800)
        desenhar_cube(vertices_projetados, 0)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()