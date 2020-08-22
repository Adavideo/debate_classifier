from .models import Tree
from .ClustersGenerator import ClustersGenerator
from .datasets_manager import get_dataset
from .util import short_document_types
from .models_manager import load_model_and_vectorizer


def tree_already_exist(tree_name):
    tree_search = Tree.objects.filter(name=tree_name)
    if tree_search: return True
    else: return False


class TreeGenerator:

    def __init__(self, tree_name, model_name, documents_options, max_level=1):
        created = self.create_empty_tree(tree_name, documents_options["types"])
        if not created: return None
        self.model_name = model_name
        self.max_level = max_level

    def create_empty_tree(self, tree_name, document_types):
        # Avoids trying to create a tree with a name that is already taken
        if tree_already_exist(tree_name):
            self.tree_already_exist = True
            return None
        else:
            self.tree_already_exist = False
            news, comments = short_document_types(document_types)
            self.tree = Tree(name=tree_name, news=news, comments=comments)
            self.tree.save()
            return self.tree

    def add_documents_to_clusters(self, clusters_generator, documents, level):
        documents_clusters = clusters_generator.predict_documents_clusters(documents)
        self.tree.add_documents_to_clusters(level, documents_clusters)

    def level_iteration(self, level):
        dataset = get_dataset(self.tree, level)
        model, vectorizer = load_model_and_vectorizer(self.model_name, level)
        if model and vectorizer:
            clusters_generator = ClustersGenerator(model, vectorizer, dataset)
            clusters_information = clusters_generator.get_clusters_information()
            self.tree.add_clusters(level, clusters_information)
            self.add_documents_to_clusters(clusters_generator, dataset.data, level)

    def generate_tree(self):
        # Iterate through the tree levels
        for level in range(0, self.max_level+1):
            self.level_iteration(level)
        # Returns the clusters from the top level of the tree
        clusters = self.tree.get_clusters_of_level(self.max_level)
        return clusters
