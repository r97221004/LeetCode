class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):

        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        tmp_root = self.root

        while True:

            if new_node.value == tmp_root.value:
                return False

            elif new_node.value < tmp_root.value:

                if tmp_root.left is None:
                    tmp_root.left = new_node
                    return True
                tmp_root = tmp_root.left
            else:
                if tmp_root.right is None:
                    tmp_root.right = new_node
                    return True
                else:
                    tmp_root = tmp_root.right

    def bfs(self):
        # node_queue 先進先出
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


if __name__ == "__main__":

    bst = BinarySearchTree()

    # for i in [8, 3, 10, 1, 6, 9, 14]:
    #     bst.insert(i)
    for i in [8, 10, 3, 1]:
        bst.insert(i)

    print(bst.bfs())
