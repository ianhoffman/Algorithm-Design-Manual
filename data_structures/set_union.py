class SetUnion:
    """A data structure which allows efficient merging and finding of components."""

    def __init__(self, iterable):
        """Initialize the SetUnion.

        :param iterable: an iterable forming the initial components in the union. (Each element begins in its own
            component, named for itself.)
        :type iterable: Iterable
        """
        self.components = list(iterable)
        self.size = [1 for _ in range(len(iterable))]

    def find(self, x):
        """Find the component for a given element.

        :param x:
        :return:
        """
        component = self.components[x]
        if component == x:
            return x
        else:
            return self.find(component)

    def merge(self, x, y):
        component_x = self.find(x)
        component_y = self.find(y)

        if component_x != component_y:
            if self.size[component_x] >= self.size[component_y]:
                self.size[component_x] += self.size[component_y]
                self.components[component_y] = component_x
            else:
                self.size[component_y] += self.size[component_x]
                self.components[component_x] = component_y

    def same_component(self, x, y):
        return self.find(x) == self.find(y)

