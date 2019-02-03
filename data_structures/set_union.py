from itertools import zip_longest


class SetUnion:
    """A data structure which allows efficient merging and finding of components."""

    def __init__(self, iterable):
        """Initialize the SetUnion.

        :param iterable: an iterable forming the initial components in the union. (Each element begins in its own
            component, named for itself.)
        :type iterable: Iterable
        """
        self.components = dict(zip(iterable, iterable))
        self.component_sizes = dict(zip_longest(iterable, [], fillvalue=0))

    def find(self, x):
        """Find the component for a given element.

        :param x: the element
        :type x: Any
        :return: the component the element is in
        :rtype: Any
        """
        component = self.components[x]
        if component == x:
            return x
        else:
            return self.find(component)

    def merge(self, x, y):
        """Merge to components such that the smaller component becomes part of the larger one.

        :param x: an element in the first component
        :type x: Any
        :param y: an element in the second component
        :type y: Any
        """
        component_x = self.find(x)
        component_y = self.find(y)

        if component_x != component_y:
            if self.component_sizes[component_x] >= self.component_sizes[component_y]:
                self.component_sizes[component_x] += self.component_sizes[component_y]
                self.components[component_y] = component_x
            else:
                self.component_sizes[component_y] += self.component_sizes[component_x]
                self.components[component_x] = component_y

    def same_component(self, x, y):
        """Whether two elements are in the same component.

        :param x: an element in a component
        :type x: Any
        :param y: an element in a component
        :type y: Any
        :return: Whether the elements are in the same component
        :rtype: bool
        """
        return self.find(x) == self.find(y)
