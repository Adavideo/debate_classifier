from .examples import news_content, comments_content


tree_name = "test_comments10"

example_terms = ['13', '2010', '21', '23', '310', '355', '40', '8kbxfauvdxa', 'abrir', 'ahora', 'alarma', 'allá', 'anterior', 'anticuerpos', 'aunque', 'años', 'basta', 'be', 'boe', 'brutal', 'chalao', 'cierto', 'cobra', 'cobran', 'colau', 'consta', 'cuenta', 'currar', 'cuéntame', 'darse', 'deficitarias', 'después', 'dices', 'elegantemente', 'empresas', 'enteras', 'evidente', 'explícale', 'expresidente', 'expresidentes', 'fallout', 'falta', 'forma', 'full', 'gatos', 'guardo', 'gustan', 'hace', 'https', 'improductivas', 'injustamente', 'ir', 'jugar', 'ley', 'llegara', 'lol', 'melón', 'mismo', 'mitad', 'montilla', 'niegan', 'origen', 'pantomima', 'parlamento', 'penalice', 'pensión', 'peor', 'precios', 'privadas', 'problemas', 'prohíba', 'publicaciones', 'pujol', 'regiones', 'retiraron', 'sabes', 'sacado', 'sepas', 'si', 'suban', 'subido', 'sueldo', 'todas', 'torra', 'transpasar', 'youtu']


# PREDICTED CLUSTERS

example_predicted_clusters_level0 = [0, 0, 3, 0, 3, 2, 1, 2, 0, 3]
example_predicted_clusters_level1 = [0, 0, 1, 1]
example_predicted_clusters = [ example_predicted_clusters_level0, example_predicted_clusters_level1 ]


# CLUSTERS DOCUMENTS

documents_cluster0_level0 = [
    '#4 Cuéntame tu,  a mi no me consta.',
    '!Brutal! {lol}',
    '#310 No. Las guardo para cuando tenga que ir a currar.',
    'Pantomima Full - Gatos.\nhttps://youtu.be/8kbXfAuvdxA']

documents_cluster1_level0 = [
    '#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...']

documents_cluster2_level0 = [
    'basta jugar fallout para darse cuenta',
    '#355 Transpasar anticuerpos? Que dices chalao...']

documents_cluster3_level0 = [
    'Pero más allá del estado de alarma y sus publicaciones en el BOE, ¿qué ley han sacado ahora mismo que penalice o prohíba algo de esto?\n\nQue para eso hace falta el parlamento.',
    '#23 Pujol ya era expresidente antes que Torra llegara y le retiraron la pensión (injustamente)  hace unos años. No te enteras de nada. \n\n\nQuien sí la cobra es Montilla que es el origen de todos los problemas aunque no lo sepas porque no sabes nada anterior a 2010 (y de después la mitad). \n\n\nY también cobran los expresidentes de todas esas regiones  deficitarias e improductivas que tanto os gustan.\n\n\nPor cierto  , para sueldo subido el de Colau, ¿era el 40%?',
    '#13 explícale que es la que hace que las empresas privadas no suban precios']

documents_cluster0_level1 = [
    "#310 No. Las guardo para cuando tenga que ir a currar.",
    "#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente..."]

documents_cluster1_level1 = [
    "#355 Transpasar anticuerpos? Que dices chalao...",
    "#13 explícale que es la que hace que las empresas privadas no suban precios"
    ]

clusters_documents_level0 = [ documents_cluster0_level0, documents_cluster1_level0 , documents_cluster2_level0, documents_cluster3_level0 ]
clusters_documents_level1 = [ documents_cluster0_level1, documents_cluster1_level1 ]
clusters_documents = [ clusters_documents_level0, clusters_documents_level1 ]


# LEVEL 0 CLUSTERS

cluster0_level0 = {
    "num_cluster": 0,
    "num_children" : 0,
    "terms" : "['currar', 'ir', 'guardo', '310']",
    "reference_doc": "#310 No. Las guardo para cuando tenga que ir a currar.",
    "documents": documents_cluster0_level0,
    "children": []
}

cluster1_level0 = {
    "num_cluster": 1,
    "num_children" : 0,
    "terms" : "['elegantemente', 'melón', 'abrir', 'forma', 'evidente', 'peor', 'niegan', 'si', '21']",
    "reference_doc": "#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...",
    "documents": documents_cluster1_level0,
    "children": []
}

cluster2_level0 = {
    "num_cluster": 2,
    "num_children" : 0,
    "terms" : "['chalao', 'dices', 'anticuerpos', 'transpasar', '355']",
    "reference_doc": "#355 Transpasar anticuerpos? Que dices chalao...",
    "documents": documents_cluster2_level0,
    "children": []
}

cluster3_level0 = {
    "num_cluster": 3,
    "num_children" : 0,
    "terms" : "['precios', 'suban', 'privadas', 'empresas', 'explícale', '13', 'hace']",
    "reference_doc": "#13 explícale que es la que hace que las empresas privadas no suban precios",
    "documents": documents_cluster3_level0,
    "children": []
}


# LEVEL 1 CLUSTERS

cluster0_level1 = {
    "num_cluster": 0,
    "num_children" : 2,
    "terms" : "['elegantemente', 'melón', 'abrir', 'forma', 'evidente', 'peor', 'niegan', 'si', '21']",
    "reference_doc": "#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...",
    "documents": documents_cluster0_level1,
    "children": [ cluster0_level0, cluster1_level0 ]
}
cluster1_level1 = {
    "num_cluster": 1,
    "num_children" : 2,
    "terms" : "['chalao', 'dices', 'anticuerpos', 'transpasar', '355']",
    "reference_doc": "#355 Transpasar anticuerpos? Que dices chalao...",
    "documents": documents_cluster1_level1,
    "children": [ cluster2_level0, cluster3_level0 ]
}


# TERMS
level0_terms = example_terms
level1_terms = ['13', '21', '310', '355', 'abrir', 'anticuerpos', 'chalao', 'currar', 'dices', 'elegantemente', 'empresas', 'evidente', 'explícale', 'forma', 'guardo', 'hace', 'ir', 'melón', 'niegan', 'peor', 'precios', 'privadas', 'si', 'suban', 'transpasar']

# LEVEL DOCUMENTS
level0_documents = comments_content
level1_documents = [
    "#310 No. Las guardo para cuando tenga que ir a currar.",
    "#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...",
    "#355 Transpasar anticuerpos? Que dices chalao...",
    "#13 explícale que es la que hace que las empresas privadas no suban precios"
    ]

# REFERENCE DOCUMENTS

example_reference_documents = [
    level1_documents,
    [ cluster0_level1["reference_doc"], cluster1_level1["reference_doc"] ]
]


# TREES

tree_level0 = {
    "terms": level0_terms,
    "documents": level0_documents,
    "predicted_clusters": example_predicted_clusters_level0,
    "clusters": [ cluster0_level0, cluster1_level0, cluster2_level0, cluster3_level0 ],
    "reference_documents": example_reference_documents[0]
}

tree_level1 = {
    "terms": level1_terms,
    "documents": level1_documents,
    "clusters": [ cluster0_level1, cluster1_level1 ],
    "predicted_clusters": example_predicted_clusters_level1,
    "reference_documents": example_reference_documents[1]
}

example_tree = [tree_level0, tree_level1]
