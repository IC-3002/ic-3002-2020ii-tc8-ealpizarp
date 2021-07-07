def contar_rutas_mas_cortas(C):

    fila = len(C)
    columnas = len(C[0])

    if (C[0][0] == 1):
        return 0

    for i in range(fila):
        
        if (C[i][0] == 0):
            C[i][0] = 1

        else:
            C[i][0] = 0
            break
    
    for i in range(1, columnas, 1): 
        if (C[0][i] == 0): 
            C[0][i] = 1
  
        else: 
            C[0][i] = 0
            break
  
    for i in range(1, fila): 

        for j in range(1, columnas): 

            if (C[i][j] == 1):

                C[i][j] = 0

            else:

                if (C[i - 1][j] > 0): 
                    C[i][j] = (C[i][j] + C[i - 1][j]) 
                    
                if (C[i][j - 1] > 0): 

                    C[i][j] = (C[i][j] + C[i][j - 1]) 

    if (C[fila - 1][columnas - 1] > 0): 
    
        return C[fila - 1][columnas - 1]

    else: 
        return 0