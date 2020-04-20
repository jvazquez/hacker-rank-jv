class Valley:

    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        if value < -1:
            if self.next is None:
                self.next = Valley(value)
            else:
                self.next.add(value)


class ValleyCount:
    def __init__(self, steps):
        self.total_steps = steps
        self.sea_level_distance = 0
        self.valley_counter = set()

    def step_analyzer(self, step):
        if step == 'U':
            self.sea_level_distance += 1
        elif step == 'D':
            self.sea_level_distance -= 1

        if self.sea_level_distance < -1:
            self.valley_counter.add(self.sea_level_distance)


def counting_valleys(steps, sequence):
    sea_level_index = 0
    valley_count = 0
    map_key = {"U": 1, "D": -1}
    for step in sequence:
        sea_level_index += map_key.get(step)
        if sea_level_index == 0 and step == "U":
            valley_count += 1
    return valley_count
