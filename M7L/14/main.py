'''Utilizando o grafo a seguir, faça um programa que crie uma árvore geradora para
cada item abaixo:'''
from arvore_bfs import ArvoreBFS
from arvore_dfs import ArvoreDFS

# Construção da árvore geradora a partir do vértice 'i'
arvore_bfs = ArvoreBFS.bfs_tree('i', ArvoreBFS.grafo)

# Exibição do resultado
print("Árvore geradora (BFS, partida em 'i'):")
print(arvore_bfs)

print()

arvore_dfs = ArvoreDFS.dfs_tree('a', ArvoreDFS.grafo)

# Exibição do resultado
print("Árvore geradora (DFS, partida em 'a'):")
print(arvore_dfs)