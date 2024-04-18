class MovimentacaoUtil:
    @staticmethod
    def realiza_click_tecla(pygame, tecla, pos_atual_x, pos_atual_y):
        """
        Atualiza as coordenadas de posição com base na tecla de movimentação pressionada.

        :param pygame: Referência ao módulo pygame, utilizado para acessar constantes de teclas.
        :param tecla: A tecla pressionada, capturada pelo evento de teclado.
        :param pos_atual_x: Posição atual no eixo X.
        :param pos_atual_y: Posição atual no eixo Y.
        :return: Uma tupla com as novas posições (pos_atual_x, pos_atual_y) após o movimento.

        As teclas de setas são mapeadas para movimentos específicos:
        - Esquerda diminui X em 10.
        - Direita aumenta X em 10.
        - Cima diminui Y em 10.
        - Baixo aumenta Y em 10.
        """
        movimentacao = {
            pygame.K_LEFT: (-10, 0),
            pygame.K_RIGHT: (10, 0),
            pygame.K_UP: (0, -10),
            pygame.K_DOWN: (0, 10)
        }

        if tecla in movimentacao:
            delta_x, delta_y = movimentacao[tecla]
            pos_atual_x += delta_x
            pos_atual_y += delta_y
        return pos_atual_x, pos_atual_y
    
    @staticmethod
    def realiza_segura_botao_direito_arrasta_mouse(pygame, evento, angulo_x, angulo_y):
        """
        Ajusta os ângulos de rotação com base no movimento do mouse com o botão direito pressionado.

        :param pygame: Referência ao módulo pygame, usado para verificar o estado dos botões do mouse.
        :param evento: Evento de movimentação do mouse capturado pelo pygame.
        :param angulo_x: Ângulo atual de rotação em torno do eixo X.
        :param angulo_y: Ângulo atual de rotação em torno do eixo Y.
        :return: Uma tupla com os novos ângulos (angulo_x, angulo_y) após ajuste.

        O movimento vertical do mouse ajusta o angulo_x e o movimento horizontal ajusta o angulo_y.
        Os ângulos são incrementados em 0.01 radianos por unidade de movimento do mouse.
        """
        if pygame.mouse.get_pressed()[2]:
            angulo_x += evento.rel[1] * 0.01
            angulo_y += evento.rel[0] * 0.01
        return angulo_x, angulo_y
