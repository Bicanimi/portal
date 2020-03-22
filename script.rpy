init python:
    rotafinal = False
define v = Character ("Victhor")
define d = Character ("Descrição")
define p = Character ("Jackson")
define i = Character ("Igor")
define c = Character ("Chapeleiro Maluco")
define l = Character ("Lebre")

image quarto do victhor= "images/cenas/QUARTO DO VICTHOR.png"
image victhor nervoso = "images/Victhor/victhor azul/victhor bravo.png"
image victhor conformado = "images/Victhor/victhor azul/victhor conformado.png"
image victhor preocupado = "images/Victhor/victhor azul/victhor procupado.png"
image pai do victhor = "images/pai do vicrhor.png"
image sala do victhor = "images/cenas/sala do victhor.png"
image portao = "images/cenas/portao da casaa.png"
image victhor debochando = "images/Victhor/victhor azul/victhor debochando.png"
image entrada do pais das maravilhas = "images/cenas/entrada do pais das maravilhas.png"
image casa = "images/cenas/frente da casa.png"
image victhor desanimado = "images/Victhor/victhor azul/victhor desanimado.png"
image victhor falando = "images/Victhor/victhor azul/victhor falando.png"
image chapeleiro intrigado = "images/Chapeleiro/chapeleiro intrigado.png"
image chapeleiro zombando = "images/Chapeleiro/chapeleiro zombando com roupa.png"
image chapeleiro triste = "images/Chapeleiro/chapeleiro triste.png"
image chapeleiro preocupado = "images/Chapeleiro/chapeleiro preocupado.png"
image chapeleiro irritado = "images/Chapeleiro/chapeleiro irritado.png"
image victhor assustado = "images/Victhor/victhor azul/victhor assustado.png"
image casa do chapeleiro 1= "images/cenas/casa chapeleiro 1.png"
image casa do chapeleiro 2= "images/cenas/casa chapeleiro 2.png"
image casa do chapeleiro 3= "images/cenas/casa chapeleiro 3.png"
image chapeleiro assustado = "images/Chapeleiro/chapeleiro assustado.png"
image bosque = "images/cenas/bosque.png"
image chapeleiro animado = "images/Chapeleiro/chapeleiro animado.png"
image victhor surpreso = "images/Victhor/victhor azul/victhor surpreso.png"
image victhor envergonhado verde = "images/Victhor/victhor verde/Victhor com vergonha.png"
image victhor assustado verde = "images/Victhor/victhor verde/victhor assustado.png"
image victhor bravo verde = "images/Victhor/victhor verde/victhor bravo.png"
image victhor conformado verde = "images/Victhor/victhor verde/victhor conformado.png"
image victhor debochando verde = "images/Victhor/victhor verde/victhor debochando.png"
image victhor desanimado verde = "images/Victhor/victhor verde/victhor desanimado.png"
image victhor falando verde = "images/Victhor/victhor verde/victhor falando.png"
image victhor preocupado verde = "images/Victhor/victhor verde/victhor preocupado.png"
image victhor surpreso verde = "images/Victhor/victhor verde/victhor surpreso.png"
image sala do chapeleiro = "images/cenas/sala do chapeleiro 2.png"
image victhor irritado = "images/Victhor/victhor azul/victhor irritado.png"
image victhor duvidando = "images/Victhor/victhor azul/victhor duvidando.png"
image victhor irritado verde = "images/Victhor/victhor verde/victhor irritado.png"
image victhor duvidando verde = "images/Victhor/victhor verde/victhor duvidando.png"
image victhor duvidando verde = "images/Victhor/victhor verde/victhor duvidando.png"
image cozinha do chapeleiro = "images/cenas/cozinha do chapeleiro.png"
image quarto da alice = "images/cenas/quarto da alice.png"
image chapeleiro rindo = "images/Chapeleiro/chapeleiro rindo.png"
image victhor envergonhado = "images/Victhor/victhor azul/victhor com vergonha.png"
image victhor molhado = "images/Victhor/victhor azul/victhor molhado.png"
image lebre brava = "images/A Lebre/lebre brava.png"
image lebre zombando = "images/A Lebre/lebre zombando.png"
image lebre triste = "images/A Lebre/lebre triste.png"
image lebre sorrindo = "images/A Lebre/lebre sorrindo.png"
image lebre pensando = "images/A Lebre/lebre pensando.png"
image lebre gritando = "images/A Lebre/lebre gritando.png"
image chapeleiro fazendo birra = "images/Chapeleiro/Chapeleiro fazendo birra.png"
image lebre vermelha = "images/A Lebre/lebre vermelha.png"
image victhor animado verde = "images/Victhor/victhor verde/Victhor animado.png"
image bosque castelo vermelho = "images/cenas/caminho para o cv.png"
image entrada castelo vermelho = "images/cenas/castelo vermelho entrada.png"
image castelo vermelho = "images/cenas/castelo vermelho.png"
image final = "images/cenas/final.png"
image festa = "images/cenas/festa.png"

label start :

    scene quarto do victhor at truecenter:
         zoom 0.6
    with dissolve

    show victhor preocupado at left:
         zoom 0.185
    with move

    v "Estou atrasado!Muito atrasado!"

    d "Escuta-se uma buzina do lado de fora da casa."

    show victhor preocupado at center:
         zoom 0.185
    with move

    v "Igor já chegou!"

    v "Porque não me arrumei antes?!"

    show victhor preocupado at right:
         zoom 0.185
    with move

    v "Ahhhhhh!"

    hide victhor

    scene quarto do victhor at truecenter:
         zoom 0.6
    with vpunch and hpunch

    d "Victhor corre pelo quarto a procura do paletó, mas não acha..."

    show victhor conformado at left:
       zoom 0.185
    with move

    v "Ah! Esquece vou assim mesmo."

    hide victhor

    show sala do victhor at center:
        zoom 0.6
    with vpunch

    show pai do victhor at left:
        zoom 0.19
    with move

    show victhor envergonhado at right:
        zoom 0.185
    with move

    p "Finalmente alguém está bem vestido!"

    p "Aproveita a festa filho!"

    v "Tá pai, tchau..."

    scene portao at center:
       zoom 0.6
    with hpunch

    show victhor preocupado at left:
       zoom 0.185
    with move

    v "Você chegou rápido!"

    i "E eu achando que a princesa não apareceria nunca!"

    show victhor debochando at center:
        zoom 0.185
    with move

    v "Como se você pudesse falar alguma coisa! Até onde eu sei o senhor dos atrasos é você..."

    i "Hahaha, muito engraçado... Venha logo! Graças a alguém não temos tempo para ficar batendo papo."

    d "Victhor se aproxima do portão e tenta abri-lo, mas não funciona."

    show victhor nervoso at center:
       zoom 0.185
    with move

    i "Anda logo! Desse jeito não vamos chegar nunca!"

    v "A culpa não é minha se essa coisa não abre!!!"

    menu:
        "Chutar o portão":
            $rotafinal = True

        "Tentar mais uma vez":

            $rotafinal = False

    if rotafinal == True:

        jump paisdasmaravilhas

    if rotafinal == False:

        scene casa at center:
            zoom 0.6
        with vpunch

        i "Podia ter feito isso antes"

        show victhor falando at left:
            zoom 0.185
        with move

        v "Ah pare de reclamar e vamos logo."

        hide victhor

        show festa at truecenter:
            zoom 0.6
        with dissolve

        d "Victhor entra no carro e vai para a festa em segurança."

        jump finaldocap

label paisdasmaravilhas :

    scene entrada do pais das maravilhas at right:
        zoom 0.6
    with hpunch and vpunch

    show victhor preocupado at center:
        zoom 0.175
    with move

    v "ONDE EU ESTOU?!"

    show victhor desanimado at left:
        zoom 0.165
    with move

    v "Qual era a dificuldade de ir a uma festa como todo mundo?"

    c "Alice, ainda não desistiu de ser normal?"

    show victhor assustado at left:
        zoom 0.155
    with move

    show chapeleiro zombando at center:
        zoom 0.225
    with move

    c "Adorei o cabelo Alice!"

    show victhor duvidando at left:
        zoom 0.155
    with move

    menu:
       "Valeu, quem é você?":

           c"Sou eu!"

           jump conversaalternativacomochapeleiro

       "Obrigado, mas quem é Alice?":

           $rotafinal = True

       "Tenho cara de Alice por um acaso?":

           $rotafinal = False

    if rotafinal == True:

        show chapeleiro preocupado at center:
            zoom 0.225
        with move

        c "AI MEU DEUS O QUE OUVE?!"

        v "Ai meus deus o que foi agora?"

        show victhor debochando at left:
            zoom 0.155
        with dissolve

        c "A Alice enlouqueceu!!!"

        v "Sério? Mas quem é ela?"

        show chapeleiro zombando:
            zoom 0.225
        with move

        c "Você é ela!"

        show chapeleiro preocupado at center:
            zoom 0.225
        with move

        show victhor preocupado at left:
            zoom 0.155
        with move

        c "Você definitivamente não esta bem!"

        c "Tenho que te levar para a minha casa antes que você piore!"

        show victhor preocupado at center:
             zoom 0.155
        with move

        show chapeleiro preocupado at right:
             zoom 0.225
        with move

        show victhor preocupado at right:
             zoom 0.155
        with move

        hide victhor and chapeleiro

        d "O Chapeliro Maluco arrasta Victhor pelo caminho de pedras flutuantes."

        jump finaldocap

    if rotafinal == False:

        show victhor nervoso at left:
            zoom 0.155
        with move

        show chapeleiro irritado:
            zoom 0.225
        with move

        c "Não. Não tem..."

        hide victhor

        d "o Chapeleiro empurra o Victhor e ele cai das pedras mágicas, morrendo com a queda."

        jump fimdojogo

label conversaalternativacomochapeleiro :

    show chapeleiro triste at center:
        zoom 0.225
    with move

    c "Quem mais seria Alice?"

    menu:
       "Se eu soubesse quem você é, não estaria perguntando":

        show victhor nervoso at left:
            zoom 0.155
        with move

        show chapeleiro irritado:
            zoom 0.225
        with move

        hide victhor

        d "Victhor nem conseguiu reagir antes de ser jogado das pedras flutuantes e morrer com o impacto"

        jump fimdojogo

       "Quem é essa Alice que você sempre fala?":

        show chapeleiro preocupado at center:
            zoom 0.225
        with move

        c "AI MEU DEUS O QUE OUVE?!"

        v "Ai meus deus o que foi agora?"

        show victhor debochando at left:
            zoom 0.155
        with dissolve

        c "A Alice enlouqueceu!!!"

        v "Sério? Mas quem é ela?"

        show chapeleiro zombando:
            zoom 0.225
        with move

        c "Você é ela!"

        show chapeleiro preocupado at center:
            zoom 0.225
        with move

        show victhor preocupado at left:
            zoom 0.155
        with move

        c "Você definitivamente não esta bem!"

        c "Tenho que te levar para a minha casa antes que você piore!"

        show victhor preocupado at center:
             zoom 0.155
        with move

        show chapeleiro preocupado at right:
             zoom 0.225
        with move

        show victhor preocupado at right:
             zoom 0.155
        with move

        hide victhor and chapeleiro

        d "O Chapeliro Maluco arrasta Victhor pelo caminho de pedras flutuantes."

        jump finaldocap

label finaldocap:

    d"Parabéns você sobreviveu a mais uma parte, mês que vem tem mais um capítulo..."

    jump final

label fimdojogo :

    scene final at center:
        zoom 0.6
    with dissolve

    d "Infelizmente você matou o Victhor, mas não se preocupe, para você a história
     ainda não acabou..."

label final:
