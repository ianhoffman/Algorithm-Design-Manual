class SetUnion:
    def __init__(self, iterable):
        self.components = list(iterable)
        self.size = [1 for _ in range(len(iterable))]

    def find(self, x):
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

