from __future__ import annotations

class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def insert(self, value: int) -> None:
        if value <= self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder(self) -> list[int]:
        result: list[int] = []
        if self.left is not None:
            result.extend(self.left.inorder())
        result.append(self.value)
        if self.right is not None:
            result.extend(self.right.inorder())
        return result


def decision_tree_sort(values: list[int]) -> list[int]:
    """Sort a list using a decision-tree-like binary search tree insertion."""
    if not values:
        return []

    root = TreeNode(values[0])
    for value in values[1:]:
        root.insert(value)
    return root.inorder()


if __name__ == "__main__":
    sample = [7, 3, 9, 1, 5, 8, 2, 4, 6]
    sorted_values = decision_tree_sort(sample)
    print("Original:", sample)
    print("Sorted:", sorted_values)
