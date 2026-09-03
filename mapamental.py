

import matplotlib.pyplot as plt
import networkx as nx

# 1. Inicializar o grafo direcionado (mostra o fluxo de informações)
G = nx.DiGraph()

# 2. Definir os Nós (Redes e suas funções principais)
redes_cerebrais = {
    "DMN\n(Modo Padrão)": "Imaginação, divagação, geração de ideias brutas e memórias.",
    "Executiva\nCentral": "Foco, tomada de decisão, filtragem e execução (O Editor).",
    "Rede de\nSaliência": "Filtro de relevância, alterna a atenção entre a DMN e a Executiva."
}

for node, desc in redes_cerebrais.items():
    G.add_node(node, descrição=desc)

# 3. Definir as Arestas (Como as redes funcionam e interagem entre si)
# Origem, Destino, Relação Pedagógica/Neurocientífica
conexoes = [
    ("DMN\n(Modo Padrão)", "Rede de\nSaliência", "Envia insights brutos, pensamentos e conexões improváveis."),
    ("Rede de\nSaliência", "Executiva\nCentral", "Detecta uma ideia relevante e convoca o controle focado."),
    ("Executiva\nCentral", "DMN\n(Modo Padrão)", "Inibe a divagação para finalizar o trabalho ou organizar o caos."),
    ("Rede de\nSaliência", "DMN\n(Modo Padrão)", "Desliga o foco executivo (incubação), permitindo o ócio criativo.")
]

for origem, destino, relacao in conexoes:
    G.add_edge(origem, destino, interacao=relacao)

# 4. Configurações estéticas do Mapa Mental / Grafo
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42, k=1.5)  # Algoritmo de posicionamento espacial

# Desenhar os Nós
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='#a2d2ff', edgecolors='#003049', linewidths=2)

# Desenhar as Arestas (Linhas de comunicação)
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color='#003049', width=2, connectionstyle="arc3,rad=0.1")

# Desenhar os Rótulos dos Nós
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_family='sans-serif')

# Desenhar as explicações das conexões (arestas)
edge_labels = nx.get_edge_attributes(G, 'interacao')
# Formata as strings longas para que fiquem visualmente organizadas no gráfico
edge_labels_quebradas = {k: '\n'.join([v[i:i+30] for i in range(0, len(v), 30)]) for k, v in edge_labels.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels_quebradas, font_size=8, font_color='#555555')

# Finalizar exibição
plt.title("Mapa Mental de Conectividade Funcional das Redes da Criatividade", fontsize=14, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()
plt.show()

