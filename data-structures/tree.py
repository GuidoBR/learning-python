class Tree:
    def __init__(self, value=None, left=None, right=None):
        self._left = left
        self._right = right
        self._value = value
        self.children = [self._left, self._right]

    def __repr__(self, level=0):
        """
        >>> print(Tree(1))
        1
        >>> print(Tree(1, Tree(2), Tree(2)))
          1
        2   2
        >>> print(Tree(1, Tree(2, Tree(3), Tree(3)), Tree(2), Tree(3), Tree(3)))
            1
          2    2
        3   3 3  3
        """
        if self._value == None:
            return None
        print(self._right, level+1)
        print('  ' * level + str(self._value))
        print(self._left, level+1)


def is_mirror(left_tree=None, right_tree=None):
    '''
    >>> t1 = Tree(1, Tree(2), Tree(2))
    >>> t2 = Tree(1, Tree(2, None, Tree(3)), Tree(2))
    >>> t3 = Tree(1, Tree(2, Tree(4, None, None), Tree(3, None, None)), Tree(2, Tree(3, None, None), Tree(4, None, None)))
    >>> print is_mirror(t1._left, t1._right)
    True
    >>> print is_mirror(t2._left, t2._right)
    False
    >>> print is_mirror(t3._left, t3._right)
    True
    '''
    if left_tree is None or right_tree is None:
        return (not left_tree) and (not right_tree)

    same_values = left_tree._value == right_tree._value
    is_mirror_left = is_mirror(left_tree._left, right_tree._right)
    is_mirror_right = is_mirror(right_tree._left, left_tree._right)
    return same_values and is_mirror_left and is_mirror_right


if __name__ == "__main__":
    import doctest
    doctest.testmod()
