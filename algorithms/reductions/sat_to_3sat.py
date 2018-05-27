from typing import List


class BooleanVariable:
    def __hash__(self) -> int:
        return hash(self.name)

    def __init__(self, name: str = 'A') -> None:
        self.name = name

    def __invert__(self) -> 'BooleanVariable':
        return NegatedBooleanVariable(self.name)

    def __repr__(self) -> str:
        return self.name


class NegatedBooleanVariable(BooleanVariable):
    def __invert__(self) -> BooleanVariable:
        return BooleanVariable(self.name)

    def __repr__(self) -> str:
        return f'~{self.name}'


Clause = List[BooleanVariable]


SatInstance = List[Clause]


def sat_to_3sat(sat_instance: SatInstance) -> SatInstance:
    clauses = []

    for clause in sat_instance:
        if len(clause) == 1:
            for i in range(2):
                new_clause = []
                if i % 2:
                    new_clause.append(BooleanVariable())
                else:
                    new_clause.append(~BooleanVariable())
                for j in range(2):
                    if i % 2:
                        new_clause.append(BooleanVariable())
                    else:
                        new_clause.append(~BooleanVariable())
                clause.extend(clause)
                clauses.append(new_clause)
        elif len(clause) == 2:
            for i in range(2):
                new_clause = []
                if i % 2:
                    new_clause.append(BooleanVariable())
                else:
                    new_clause.append(~BooleanVariable())
                new_clause.extend(clause)
                clauses.append(new_clause)
        elif len(clause) == 3:
            clauses.append(clause)
        else:
            clauses.append([
                *clause[:2],
                BooleanVariable()
            ])
            for i in range(2, len(clause) - 2):
                clauses.append([
                    ~clauses[-1][-1],
                    clause[i],
                    BooleanVariable()
                ])
            clauses.append([
                ~BooleanVariable(),
                *clause[-2:]
            ])

    return clauses


if __name__ == '__main__':
    sat_instance = [
        [
            BooleanVariable(name='X'),
            BooleanVariable(name='Y'),
            ~BooleanVariable(name='Z'),
            BooleanVariable(name='W'),
            BooleanVariable(name='U'),
            ~BooleanVariable(name='V')
        ],
        [
            ~BooleanVariable(name='X'),
            ~BooleanVariable(name='Y'),
            BooleanVariable(name='Z'),
            ~BooleanVariable(name='W'),
            BooleanVariable(name='U'),
            BooleanVariable(name='V')
        ]
    ]
    print(sat_to_3sat(sat_instance))
