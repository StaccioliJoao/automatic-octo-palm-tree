tabuleiro = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0], #Aqui é o tabuleiro do sudoku, mude os zeros para os numeros em suas posiçoes no tabuleiro que deseja resolver
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

def resolver(tab):
                    #Funçao de resolver o sudoku usando backtracking
    achar = achar_vazio(tab) #acha lugar vazio
    if not achar:
        return True
    else:
        fileira, coluna = achar #seta posiçao do vazio
    
    for i in range(1,10): #testa os numeros de 1 a 9
        if valido(tab, i, (fileira, coluna)): #ve se ta é valido o numero a ser posto
            tab[fileira][coluna] = i #se for valido bota o i na casa
            
            if resolver(tab): #recursao da funçao
                return True
            
            tab[fileira][coluna] = 0 #se nao funcionar nenhum numero ele seta pra 0 denovo e volta.
            
    return False
        


def valido(tab, num, pos):
    #verifica se tem o mesmo numero na fileira ja
    for i in range(len(tab[0])):
        if tab[pos[0]][i] == num and pos[1] != i:
            return False
    #verifica se tem o mesmo numero na coluna
    for i in range(len(tab[0])):
        if tab[i][pos[1]] == num and pos[0] != i:
            return False
        
    #ver qual cubo ta
    cubo_x = pos[1] // 3
    cubo_y = pos[0] // 3
    
    for i in range(cubo_y*3, cubo_y*3+3):
        for j in range(cubo_x*3, cubo_x*3+3):
            if tab[i][j] == num and (i,j) != pos:
                return False
    
    return True

def print_tabuleiro(tab): #funçao de imprimir o tabuleiro do sudoku
    
    
    for i in range(len(tab)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
    
        for j in range(len(tab[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end="")
            
def achar_vazio(tab): #acha os vazios para o programa saber onde ele pode operar
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0:
                return(i, j) #fileira, coluna
            
    return None

                            #Mostrar o sudoku resolvido
print_tabuleiro(tabuleiro)
resolver(tabuleiro)
print("-----Resolvido-----")
print_tabuleiro(tabuleiro)