from typing import List


class SimplePath:
    def __init__(self, nodes, starting_point=0):
        self.node_list = list(map(int, nodes))
        self.initial_position = starting_point
        self.best_path = [0]
        self.last_index = len(self.node_list) - 1

    def verify_completion(self, new_index_candidate):
        return self.last_index == new_index_candidate

    def solve(self):
        """
        0 0 0 0 1 0
        """
        circuit_complete = False

        for index, node_value in enumerate(self.node_list):

            if circuit_complete:
                break

            new_index = self.best_path[-1] + 2
            plus_two = self.look_ahead(new_index)

            if plus_two and new_index not in self.best_path:
                self.best_path.append(new_index)
                circuit_complete = self.verify_completion(new_index)
            else:
                new_index = self.best_path[-1] + 1
                plus_one = self.look_ahead(new_index)
                if plus_one and new_index not in self.best_path:
                    self.best_path.append(new_index)
                    circuit_complete = self.verify_completion(new_index)

        return len(self.best_path) - 1

    def look_ahead(self, step):
        is_valid = False
        try:
            if self.node_list[step] == 0:
                is_valid = True
        except IndexError:
            is_valid = False

        return is_valid


def cloud_jumper(cloud_list: List) -> int:
    solver = SimplePath(cloud_list, 0)
    return solver.solve()
