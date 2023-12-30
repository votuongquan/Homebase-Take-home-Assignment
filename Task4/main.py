import timeit

class Node:
    def __init__(self, id, children=None):
        self.id = id
        self.children = children if children is not None else []
        self.left = None
        self.right = None

class NestedSet:
    def __init__(self):
        self.root = None
        self.node_lookup = {}
        self.counter = 1

    def convert_to_nested_set(self, root):
        self.root = root
        self._convert_to_nested_set(self.root)

    def _convert_to_nested_set(self, node):
        node.left = self.counter
        self.counter += 1
        self.node_lookup[node.id] = node

        for child in node.children:
            self._convert_to_nested_set(child)

        node.right = self.counter
        self.counter += 1

    def retrieve_parent_child_relationships(self):
        relationships = {}
        self._retrieve_parent_child_relationships(self.root, relationships)
        return relationships

    def _retrieve_parent_child_relationships(self, node, relationships):
        parent_id = node.id

        for child in node.children:
            child_id = child.id
            relationships.setdefault(parent_id, []).append(child_id)
            self._retrieve_parent_child_relationships(child, relationships)

    def display_nested_set(self):
        for node_id, node in self.node_lookup.items():
            print(f"ID: {node_id}, Left: {node.left}, Right: {node.right}")

# Example tree root
root = Node('A', [
    Node('B'),
    Node('C', [
        Node('D'),
        Node('E'),
    ]),
    Node('F', [
        Node('G'),
        Node('H'),
        Node('I', [
            Node('J'), 
            Node('K')]),]),
])

# Create a nested set model
nested_set_model = NestedSet()

# Convert from the tre root to nested set
nested_set_model.convert_to_nested_set(root)

# Display the nested set and its parent-child relationships
nested_set_model.display_nested_set()
print('Relationships: ',nested_set_model.retrieve_parent_child_relationships())
