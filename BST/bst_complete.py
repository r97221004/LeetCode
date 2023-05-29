class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.value)


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._r_insert(self.root, value)

    def _r_insert(self, current_root, value):
        if value < current_root.value:
            if current_root.left == None:
                current_root.left = Node(value)
            else:
                self._r_insert(current_root.left, value)
        elif value > current_root.value:
            if current_root.right == None:
                current_root.right = Node(value)
            else:
                self._r_insert(current_root.right, value)
        else:
            print('This value has existed')

    def r_search(self, value):
        return self._r_search(self.root, value)

    def _r_search(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        if current_node.value > value:
            return self._r_search(current_node.left, value)
        if current_node.value < value:
            return self._r_search(current_node.right, value)

    def bfs(self):
        node_queue = []
        results = []
        current_node = self.root
        node_queue.append(current_node)

        while len(node_queue) > 0:
            current_node = node_queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                node_queue.append(current_node.left)
            if current_node.right is not None:
                node_queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results = []

        def traversal(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traversal(current_node.left)
            if current_node.right is not None:
                traversal(current_node.right)
        traversal(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traversal(current_node.right)
        traversal(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            if current_node.right is not None:
                traversal(current_node.right)
            results.append(current_node.value)
        traversal(self.root)
        return results


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in [8, 3, 10, 1, 6, 9, 14]:
        bst.r_insert(i)

    # print(bst.root)
    # print(bst.root.left)
    # print(bst.root.right)
    # print(bst.root.left.left)
    # print(bst.r_search(8))
    # print(bst.r_search(10))
    # print(bst.r_search(5))
    # print(bst.bfs())
    # print(bst.dfs_pre_order())
    # print(bst.dfs_in_order())
    # print(bst.dfs_post_order())
