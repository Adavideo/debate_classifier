from topics_identifier.models import Cluster
from .example_trees import example_tree
from .validations_clusters import validate_clusters_list


# TREES VALIDATION

def validate_number_of_clusters(test, level, clusters):
    # Obtain the number of clusters for this level
    num_clusters = len(example_tree[level]["clusters"])
    test.assertIs(len(clusters), num_clusters)

def validate_tree_level(test, tree, level):
    clusters_list = Cluster.objects.filter(tree=tree, level=level)
    validate_number_of_clusters(test, level, clusters_list)
    example_clusters = example_tree[level]["clusters"]
    validate_clusters_list(test, clusters_list, example_clusters, with_documents=True)

def validate_tree_document_types(test, tree, document_types):
    if document_types == "both":
        test.assertIs(tree.news, True)
        test.assertIs(tree.comments, True)
    elif document_types == "news":
        test.assertEqual(tree.news, True)
        test.assertEqual(tree.comments, False)
    else:
        test.assertEqual(tree.news, False)
        test.assertEqual(tree.comments, True)

def validate_tree(test, tree, max_level, document_types="both"):
    validate_tree_document_types(test, tree, document_types)
    for level in range(0, max_level):
        validate_tree_level(test, tree, level)