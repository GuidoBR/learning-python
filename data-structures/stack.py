class Stack:
    def __init__(self, start=[]):
        """Stack constructor. Receives a list (default empty) to use as the
        stack
        >>> s1 = Stack([1, 2, 3])
        >>> print(s1)
        [Stack: [1, 2, 3]]
        """
        self.stack = []
        for x in start:
            self.push(x)
        self.stack.reverse()

    def push(self, obj):
        """Adds a element in the top of the stack
        >>> s1 = Stack([1, 2, 3])
        >>> s1.push(4)
        >>> s1
        [Stack: [4, 1, 2, 3]]
        """
        self.stack = [obj] + self.stack

    def pop(self):
        """Remove and return the element in the top of the stack
        >>> s1 = Stack([1, 2, 3])
        >>> s1.pop()
        1
        >>> s1
        [Stack: [2, 3]]
        """
        if self.empty():
            raise 'Stack Underflow Error'
        top, self.stack = self.stack[0], self.stack[1:]
        return top

    def top(self):
        """Return the element in the top of the stack
        >>> s1 = Stack([1, 2, 3])
        >>> s1.top()
        1
        """
        if self.empty():
            raise 'Stack Underflow Error'
        return self.stack[0]

    def empty(self):
        """Verifies if a stack is empty
        >>> s1 = Stack()
        >>> s1.empty()
        True
        """
        return not self.stack

    def __repr__(self):
        """
        >>> Stack([1, 2, 3])
        [Stack: [1, 2, 3]]
        """
        return '[Stack: %s]' % self.stack

    def __cmp__(self, other):
        """Returns True if two stacks are equal
        >>> s1 = Stack([1, 2, 3])
        >>> s2 = Stack([4, 5, 6])
        >>> s1 == s2
        False
        >>> s1 != s2
        True
        """
        return cmp(self.stack, other.stack)

    def __len__(self):
        """Returns the lentgh of the stack
        >>> len(Stack())
        0
        >>> len(Stack([1, 2]))
        2
        """
        return len(self.stack)

    def __add__(self, other):
        """Adds two stacks
        >>> s1 = Stack([1, 2, 3])
        >>> s2 = Stack([4, 5, 6])
        >>> s1 + s2
        [Stack: [1, 2, 3, 4, 5, 6]]
        """
        return Stack(self.stack + other.stack)

    def __mul__(self, number):
        """
        >>> Stack([1, 2, 3]) * 2
        [Stack: [1, 2, 3, 1, 2, 3]]
        """
        return Stack(self.stack * number)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
