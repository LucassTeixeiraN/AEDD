'''Dada uma tabela de horários de ônibus que fazem viagens para as diversas cidades
do Estado, escreva um programa que possibilite a localização dos horários de saída e
de chegada quando se forneça o destino.'''    


horarios = {
    'A': {
        'saidas': ['08:00', '10:00', '12:00', '14:00'],
        'chegadas': ['09:00', '11:00', '13:00', '15:00']
    },
    'B': {
        'saidas': ['09:00', '11:30', '13:30', '15:30'],
        'chegadas': ['10:30', '12:00', '14:00', '16:00']
    },
    'C': {
        'saidas': ['07:30', '09:30', '11:30', '13:30'],
        'chegadas': ['08:30', '10:30', '12:30', '14:30']
    }
}

def localizacao(destino):
    if destino in horarios:
        saidas = horarios[destino]['saidas'] 
        chegadas = horarios[destino]['chegadas']       

        print(f"Horarios para {destino}: ")
        print("Saidas:", ', '.join(saidas))
        print("Chegadas:", ', '.join(chegadas))
        
    else:
        print(f"Destino '{destino}' nao encontrado na tabela")

def main():
    destinoINP = input("Informe o destino: ")
    localizacao(destinoINP)
main()