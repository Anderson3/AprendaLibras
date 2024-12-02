

define mingau = Character("Mingau")
define willy = Character("Willy")
define luna = Character("Luna")

define usuario = Character("[nome_usuario]")

image quadro = "quadro_branco"
image fundo0 = "praca"
image fundo1 = "parque"
image fundo2 = "ruas"
image fundo3 = "nuvens"
image telajogo = "tela_jogo"
image infor_sobre = "informacao_sobre.png"

image simbolo_libras = "simbolo libras.png"
image comunicacao01 = "comunicacao libras 01.png"
image comunicacao02 = "comunicacao libras 02.png"
image comunicacao03 = "comunicacao libras 03.png"
image simbolo_acerto = "simbolo acerto.png"
image simbolo_erro = "simbolo erro.png"

image gato = "gato.png"
image cachorro = "cachorro.png"
image abacaxi = "abacaxi.png"
image carro = "carro.png"
image escola = "escola.png"
image livro = "livro.png"
image caneta = "caneta.png"
image dado = "dado.png"
image bola = "bola.png"
image barco = "barco.png"

#chuva", "cabelo", "peteca", "piano", "alto", "baixo", "amizade", "lua", "ovo", "apito"
image chuva = "chuva.png"
image cabelo = "cabelo.png"
image peteca = "peteca.png"
image piano = "piano.png"
image alto = "alto.png"
image baixo = "baixo.png"
image amizade = "amizade.png"
image lua = "lua.png"
image ovo = "ovo.png"
image apito = "apito.png"

#"dente", "fada", "noiva", "cama", "pai", "tatu", "paz", "caju", "fita", "feliz"
image dente = "dente.png"
image fada = "fada.png"
image noiva = "noiva.png"
image cama = "cama.png"
image pai = "pai.png"
image tatu = "tatu.png"
image paz = "paz.png"
image caju = "caju.png"
image fita = "fita.png"
image feliz = "feliz.png"


image alfabeto_completo = "libras_alfabeto_completo.png"
image letra_a = "libras_a.png"
image letra_b = "libras_b.png"
image letra_c = "libras_c.png"
image letra_d = "libras_d.png"
image letra_e = "libras_e.png"
image letra_f = "libras_f.png"
image letra_g = "libras_g.png"
image letra_h = "libras_h.png"
image letra_i = "libras_i.png"
image letra_j = "libras_j.png"
image letra_k = "libras_k.png"
image letra_l = "libras_l.png"
image letra_m = "libras_m.png"
image letra_n = "libras_n.png"
image letra_o = "libras_o.png"
image letra_p = "libras_p.png"
image letra_q = "libras_q.png"
image letra_r = "libras_r.png"
image letra_s = "libras_s.png"
image letra_t = "libras_t.png"
image letra_u = "libras_u.png"
image letra_v = "libras_v.png"
image letra_x = "libras_x.png"
image letra_y = "libras_y.png"
image letra_z = "libras_z.png"
image letra_w = "libras_w.png"

transform imagem_quadro:
    #xzoom 2.0
    #yzoom 2.0
    pos (0.65, 0.4) 
    anchor (0.5, 0.5)

transform imagem_quadro_alfabeto:
    xzoom 0.6
    yzoom 0.6
    pos (0.65, 0.4) 
    anchor (0.5, 0.5)

transform simbolo_tela_jogo:
    xzoom 0.8
    yzoom 0.8
    pos (0.65, 0.3) 
    anchor (0.5, 0.5)

transform imagem_tela_jogo:
    xzoom 0.9
    yzoom 0.9
    pos (0.65, 0.45) 
    anchor (0.5, 0.5)



image mingau = "gato1"
image willy = "gato2"
image luna = "gato3"


screen menu_opcoes():

    imagemap:
        ground "menu jogo att"
        hover "menu jogo hover att"

        #Hotspot Informação Libras
        hotspot (375-300, 187, 2.5*158,2*516) clicked Jump ("informacaoLibras") activate_sound "mouse click.mp3"
        #Hotspot Alfabeto em libras
        hotspot (537-50, 714, 3*158,516) clicked Jump ("alfabetoLibras") activate_sound "mouse click.mp3"
        #Hotspot Exercícios
        hotspot (950, 520, 2.5*158,516) clicked Jump ("jogos") activate_sound "mouse click.mp3"
        #Hotspot Sobre
        hotspot (1355, 700, 2.5*158,516) clicked Jump ("sobre") activate_sound "mouse click.mp3"
        #hotspot (eixo x, eixo y, largura, altura) clicked Jump ("informacaoLibras")

screen botoes_auxiliares():
    #modal True

    imagebutton:
        idle "botao_home.png" 
        hover "botao_home_hover.png" 
        xalign 0.98 yalign 0.95
        focus_mask True 
        activate_sound 'mouse click.mp3'        
        action [Function(renpy.hide_screen, "pontuacao_jogo"), SetVariable("quant_acertos", 0), SetVariable("quant_erros", 0), 
                Function(renpy.hide, "simbolo_acerto"), Function(renpy.hide, "simbolo_erro"),Jump("introducao")]
 
    imagebutton:
        idle "botao_som.png" 
        hover "botao_som_hover.png" 
        xalign 0.92 yalign 0.95
        focus_mask True 
        activate_sound 'mouse click.mp3'
        action Preference("all mute", "toggle")



screen pontuacao_jogo():
    #Acertos
    text "[quant_acertos]" xpos 0.59 ypos 0.685
    #Erros
    text "[quant_erros]" xpos 0.81 ypos 0.685

    



init python:

    def botaoVoltar():
        #if botaoVoltarAtivo == True:
        ui.frame(xalign=0.93,yalign=0.95)
        ui.imagebutton("botao_home.png", "botao_home.png", clicked=Jump("introducao"), focus_mask = True)

    def botaoSair():
        #if botaoSairAtivo == True: 
        ui.frame(xalign=.98,yalign=.95)
        ui.imagebutton("botao_som.png", "botao_som.png", clicked=Jump("sair"), focus_mask = True)

    #Função de testagem dos jogos-------------------------------------------------------------------------
    global quant_acertos
    global quant_erros

    quant_acertos = quant_erros = 0

    def gerarDesafio():
        global palavra_sorteada
        global quant_acertos
        global quant_erros

        palavra_sorteada = ""

        lista_palavras = [
            "gato", "cachorro", "abacaxi", "carro", "escola", "livro", "caneta", "dado", "bola", "barco",
            "chuva", "cabelo", "peteca", "piano", "alto", "baixo", "amizade", "lua", "ovo", "apito",
            "dente", "fada", "noiva", "cama", "pai", "tatu", "paz", "caju", "fita", "feliz"
        ]
        palavra_sorteada = renpy.random.choice(lista_palavras)
        renpy.show(palavra_sorteada, at_list=[imagem_tela_jogo])
        #renpy.notify(palavra_sorteada)


    def verificarResultados(resultado_usuario):
        global palavra_sorteada
        global quant_acertos
        global quant_erros
        
        if resultado_usuario.lower() == palavra_sorteada:
            quant_acertos += 1
            renpy.notify("Acerto")
            renpy.show("simbolo_acerto", at_list=[simbolo_tela_jogo])
            renpy.play("som acerto.mp3")
            renpy.say(luna, "Parabéns! Você acertou!!! {p} A palavra era: %(palavra_sorteada)s.")
            
        else:
            quant_erros += 1
            renpy.notify("Errou")
            renpy.show("simbolo_erro", at_list=[simbolo_tela_jogo])
            renpy.play("som erro.mp3")
            renpy.say(luna, "Infelizmente você errou. {p} A resposta correta era: %(palavra_sorteada)s. Mais sorte na próxima vez.")
            
        renpy.hide(palavra_sorteada)
        renpy.hide("simbolo_acerto")
        renpy.hide("simbolo_erro")
        
        if quant_acertos >= 5:
            quant_acertos = quant_erros = 0
            renpy.hide(palavra_sorteada)
            renpy.hide_screen("pontuacao_jogo")
            renpy.jump("jogos_vitoria")
        elif quant_erros >= 3:
            renpy.hide(palavra_sorteada)
            quant_acertos = quant_erros = 0
            renpy.hide_screen("pontuacao_jogo")
            renpy.jump("jogos_derrota")
        

    #Função mudar backgrounds do jogo --------------------------------------------------
    # Ainda é necessário fazer esses código
        

    #config.overlay_functions.append(botaoVoltar)
    #config.overlay_functions.append(botaoSair)


label start:

    $botaoSairAtivo = True
    $botaoVoltarAtivo = True

    scene fundo0

    show mingau
    

    mingau "Olá amiguinho! Tudo bem com você? {p}Seja muito bem-vindo ao Aprenda Libras."
    $nome_usuario = renpy.input("Qual é o seu nome? {p} Digite seu nome e tecle ENTER para enviar.")
    if nome_usuario == "":
        "Tudo bem, caso você não queira me falar o seu nome.{p} Então vou chamar você de 'colega'."
        $nome_usuario = "colega"

    mingau "Olá %(nome_usuario)s! Me chamo Mingau, e hoje vamos embarcar em uma aventura com Libras."
    jump introducao


label introducao:

    call limpar_tudo from _call_limpar_tudo

    play music "marimba.ogg"  fadein 1.5

    show screen botoes_auxiliares()
    with dissolve
    call screen menu_opcoes
    

    '''
    mingau "Você está preparado para ingressar nessa jornada?"
    menu:
        "Sim. Mas antes quero saber o que é Libras.":
            jump informacaoLibras
        "Sim, eu quero explorar o alfabeto em Libras":
            jump alfabetoLibras
        "Ainda não estou preparado.":
            mingau "Tudo bem. Então em outro momento aprenderemos o alfabeto e libras."
    '''


return


label informacaoLibras:
    scene fundo1
    hide mingau

    show mingau at center
    with dissolve
    mingau "Olá %(nome_usuario)s! Você sabe o que é Libras?"
    mingau "LIBRAS é a Lingua Brasileira de Sinais, {p}através dela conseguimos nos comunicar com pessoas que possuem deficiência auditiva."
   
    show mingau at left
    with dissolve

    show simbolo_libras
    with dissolve

    mingau "A comunicação em Libras se dá através de gestos, sinais com as mãos e também expressões."

    mingau "... aprender Libras é muito importante, pois ampliamos nossas habilidades de comunicação e conseguimos conversar com outras pessoas."
    
    hide simbolo_libras
    show comunicacao01
    with dissolve
    show comunicacao02
    with dissolve
    show comunicacao03
    with dissolve
    mingau "Libras é uma linguagem bem fácil de aprender e é muito útil para fazer novas amizades.{p}"

    hide comunicacao01
    with dissolve
    hide comunicacao02
    with dissolve
    hide comunicacao03
    with dissolve

    hide mingau
    show mingau
    with dissolve
    mingau "Seja muito bem-vindo ao mundo da Libras e bons estudos."

    jump introducao




label alfabetoLibras:
    scene fundo1
    hide mingau
    play music "som base alfabeto.mp3" fadein 1.5

    show willy
    with dissolve

    willy "Seja muito bem-vindo, %(nome_usuario)s! {p}A partir de agora iremos aprender o alfabeto em Libras."

    willy "Estou muito feliz por ter você aqui."
    
    show quadro_branco
    with dissolve

    #Apresentação Alfabeto em Libras
    show willy at left
    with dissolve
    show alfabeto_completo at imagem_quadro_alfabeto
    with dissolve
    willy "Assim como o Alfabeto comum que aprendemos para construir palavras, existe um Alfabeto em Libras que serve para nos comunicar com outros amiguinhos."
    willy "O alfabeto em Libras completo pode ser visto ao lado."
    willy "A partir de agora iremos ver como é a representação de cada letra e também como fazemos os respectivos sinais."
    #willy "O Alfabeto pode ser visualizado no quadro ao lado..."
    hide alfabeto_completo
    

    #Letra A
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_a at imagem_quadro
    with dissolve
    willy "A primeira Letra que iremos aprender é a letra A {p} Feche a mão em um punho com o polegar estendido para fora. A palma da mão deve estar voltada para frente."
    show letra_a
    

    #Letra B
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_b at imagem_quadro
    with dissolve
    willy "A segunda Letra que iremos aprender é a letra B {p} Mantenha a mão aberta com os dedos estendidos e unidos, mas com a palma voltada para frente."
    show letra_b
    

    #Letra C
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_c at imagem_quadro
    with dissolve
    willy "Agora Letra que iremos aprender é a letra C {p} Forme um 'C' com a mão aberta, curvando os dedos para baixo. A palma deve estar voltada para frente."
    show letra_c
    

    #Letra D
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_d at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra D {p} Faça um 'D' com a mão mantendo o dedo indicador estendido e os outros dedos fechados, formando um círculo. A palma deve estar voltada para frente."
    show letra_d
    

    #Letra E
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_e at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra E {p} Dobre os dedos da mão, mantendo a palma voltada para frente. A mão deve estar em forma de 'E' com os dedos levemente curvados."
    show letra_e
    

    #Letra F
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_f at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra F {p} Junte as pontas do polegar e do dedo indicador para formar um círculo, com os outros dedos estendidos. A palma deve estar voltada para frente."
    show letra_f
    


    #Letra G
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_g at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra G {p} Estenda o dedo indicador e mantenha os outros dedos fechados. A palma deve estar voltada para o lado, e a ponta do dedo indicador deve estar ligeiramente inclinada para baixo."
    show letra_g
    

    #Letra H
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_h at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra H {p} Estenda o dedo médio e mantenha os outros dedos fechados. A palma deve estar voltada para o lado, e o dedo médio deve estar paralelo ao chão."
    show letra_h
    

    #Letra I
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_i at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra I {p} Levante o dedo mínimo (ou mindinho) enquanto mantém os outros dedos fechados. A palma deve estar voltada para o lado."
    show letra_i
    

    #Letra J
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_j at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra J {p} Levante o dedo mínimo e trace a forma de um 'J' no ar com a ponta do dedo. A palma deve estar voltada para o lado."
    show letra_j


    #Letra K
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_k at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra K {p} Estenda o dedo indicador e o dedo médio, formando um 'V'. O polegar deve estar estendido para cima. A palma deve estar voltada para o lado."
    show letra_k
    

    #Letra L
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_l at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra L {p} Estenda o dedo indicador e o polegar, formando um 'L'. Os outros dedos devem estar fechados. A palma deve estar voltada para o lado."
    show letra_l
    


    #Letra M
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_m at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra M {p} Feche a mão em um punho e coloque o polegar sobre os dedos dobrados, de modo que o polegar toque a base dos dedos. A palma deve estar voltada para frente."
    show letra_m
    

    #Letra N
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_n at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra N {p} Feche a mão em um punho, mas coloque o polegar para baixo, entre o dedo indicador e o dedo médio. A palma deve estar voltada para frente."
    show letra_n
    

    #Letra O
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_o at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra O {p} Junte todos os dedos da mão para formar um círculo, com o polegar tocando a ponta dos outros dedos. A palma deve estar voltada para frente."
    show letra_o
    

    #Letra P
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_p at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra P {p} Forme um 'P' com a mão, estendendo o dedo indicador e o dedo médio e mantendo o polegar estendido para cima. A palma deve estar voltada para o lado."
    show letra_p
    

    #Letra Q
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_q at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra Q {p}  Semelhante ao 'G', mas com a mão em uma posição mais baixa e a ponta do dedo indicador apontando mais para baixo. A palma deve estar voltada para o lado."
    show letra_q
    

    #Letra R
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_r at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra R {p} Estenda o dedo médio e dobre o dedo indicador sobre ele. Mantenha os outros dedos fechados. A palma deve estar voltada para o lado."
    show letra_r
    


    #Letra S
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_s at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra S {p} Feche a mão em um punho com a palma voltada para frente, sem deixar o polegar estendido."
    show letra_s
    

    #Letra T
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_t at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra T {p} Feche a mão em um punho, mas coloque o polegar para fora, entre o dedo indicador e o dedo médio. A palma deve estar voltada para frente."
    show letra_t
    

    #Letra U
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_u at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra U {p} Estenda o dedo indicador e o dedo médio, mantendo os outros dedos fechados. A palma deve estar voltada para frente."
    show letra_u
    

    #Letra V
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_v at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra V {p} Estenda o dedo indicador e o dedo médio em forma de 'V'. Os outros dedos devem estar fechados. A palma deve estar voltada para frente."
    show letra_v
    

    #Letra W
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_w at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra W {p} Estenda o dedo indicador, o dedo médio e o dedo anelar, mantendo os outros dedos fechados. A palma deve estar voltada para frente."
    show letra_w
    

    #Letra X
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_x at imagem_quadro
    with dissolve
    willy "A Letra que iremos aprender é a letra X {p} Dobre o dedo indicador em forma de gancho e mantenha os outros dedos fechados. A palma deve estar voltada para o lado."
    show letra_x

    
    #Letra Y
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_y at imagem_quadro
    with dissolve
    willy "A penúltima Letra que iremos aprender é a letra Y {p} Estenda o polegar e o dedo mínimo (mindinho) e mantenha os outros dedos fechados. A palma deve estar voltada para frente."
    show letra_y
    

    #Letra Z
    show willy at left
    with dissolve
    play sound "pagina.mp3"
    show letra_z at imagem_quadro
    with dissolve
    willy "E a última Letra que iremos aprender é a letra Z {p} Use o dedo indicador para desenhar a forma de um 'Z' no ar. A palma deve estar voltada para baixo ou para o lado, dependendo da posição da mão."
    show letra_z


    hide willy
    hide quadro
    
    show willy
    with dissolve

    willy "Pronto! Agora você aprendeu todas as letras do alfabeto em libras. {p} Agora é a hora de praticar com os 'Exercícios'."
    willy "Lembre-se de sempre rever esses sinais para recordar com mais facilidade."
    willy "Tchau!"

    hide willy
    hide quadro
    jump introducao


return



label jogos:
    scene fundo1
    call limpar_tudo from _call_limpar_tudo_1
    play music "som base jogos.mp3" fadein 1.5

    show luna
    with dissolve

    luna "Olá %(nome_usuario)s! {p} Você está pronto para testar seus conhecimentos?"

    show luna at left
    with dissolve

    luna "Agora é o momento de por em prática o que aprendemos ...{p} Digite as respostas e tecle ENTER para enviá-las."

    show telajogo
    with moveinright

    #show screen botoes_jogo()
    with dissolve

    #show questao_tela_jogo()
    show screen pontuacao_jogo()

    #luna "Teste"
    while True:
        $gerarDesafio()
        $resposta_usuario = renpy.input("Qual palavra está escrita na imagem?")
        $verificarResultados(resposta_usuario)

    hide luna
    #hide screen botoes_jogo
    jump introducao


label jogos_vitoria:
    scene fundo1
    call limpar_tudo from _call_limpar_tudo_2
    show luna
    with dissolve

    play sound ("som jogo vencido.wav")

    luna "Parabéns %(nome_usuario)s! {p} Você conseguiu reconhecer vários sinais de Libras e identificou várias palavras corretamente, obtendo bons resultados."
    luna "Fico feliz que tenha aprendido o alfabeto em Libras com facilidade.{p} Muito sucesso nos próximos estudos."
    luna "Até mais, amiguinho!"
    jump introducao

label jogos_derrota:
    scene fundo1
    call limpar_tudo from _call_limpar_tudo_3
    show luna
    with dissolve

    play sound ("som jogo perdido.mp3")

    luna "Infelizmente você errou muitas palavras."
    luna "Estude mais o alfabeto em Libras e tente novamente."
    jump introducao









label sair:
    $botaoSairAtivo = False
    show mingau
    mingau "Até mais!"
    return

label sobre:
    show infor_sobre
    with zoominout
    pause
    #"Este software foi desenvolvido como Trabalho de Conclusão de Curso da Pós-Graduação em Educação Especial do IFMG - Ipatininga."
    jump introducao


#Labels de Controle
label limpar_tudo:
    hide quadro_branco
    hide alfabeto_completo
    hide telajogo
    hide simbolo_libras
    hide comunicacao01
    hide comunicacao02
    hide comunicacao03
    hide infor_sobre
    hide mingau
    hide willy
    hide luna
    hide letra_a 
    hide letra_b
    hide letra_c 
    hide letra_d
    hide letra_e 
    hide letra_f
    hide letra_g 
    hide letra_h
    hide letra_i 
    hide letra_j
    hide letra_k 
    hide letra_l
    hide letra_m 
    hide letra_n
    hide letra_o 
    hide letra_p
    hide letra_q 
    hide letra_r
    hide letra_s 
    hide letra_t
    hide letra_u
    hide letra_v 
    hide letra_w
    hide letra_x 
    hide letra_y
    hide letra_z

    #renpy.hide("pontuacao_jogo")
    jump limpar_tela_game

label limpar_tela_game:
    hide gato 
    hide cachorro 
    hide abacaxi 
    hide carro 
    hide escola 
    hide livro 
    hide caneta 
    hide dado 
    hide bola 
    hide barco

    hide chuva
    hide cabelo
    hide peteca
    hide piano
    hide alto
    hide baixo
    hide amizade
    hide lua
    hide ovo
    hide apito

    hide dente
    hide fada
    hide noiva
    hide cama
    hide pai
    hide tatu
    hide paz
    hide caju
    hide fita
    hide feliz
