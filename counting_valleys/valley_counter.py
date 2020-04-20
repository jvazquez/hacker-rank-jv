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
    valley_counter = ValleyCount(steps)

    for step in sequence:
        valley_counter.step_analyzer(step)

    return len(valley_counter.valley_counter)
