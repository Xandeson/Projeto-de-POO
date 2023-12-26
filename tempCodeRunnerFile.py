
        if event.type == QUIT:
            pygame.quit()
            exit()
        comando = pygame.key.get_pressed()
        
        if comando[pygame.K_UP]:
             x -= mover
       
    labirinto.desenhar_labirinto()
    tela.blits(play_sprite, [