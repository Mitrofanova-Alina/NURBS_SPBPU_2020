import numpy as np


class Node:
    def __init__(self, x, y, weight=1):
        self.x = x
        self.y = y
        self.weight = weight

    def dist(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class NURBSpline:
    def __init__(self, power=3):
        self.p = power
        self.t = []
        self.points = []
        self.t_start = 0
        self.t_end = 1

    def print_points(self):
        i = 0
        for point in self.points:
            print(format(i, "") + ")", point.x, point.y, point.weight)
            i += 1
        print("t:", self.t)

    def get_key_point_x(self):
        return [self.points[i].x for i in range(len(self.points))]

    def get_key_point_y(self):
        return [self.points[i].y for i in range(len(self.points))]

    def set_points(self, x_, y_, weight_, t_=None, is_clamped_start=False, is_clamped_end=False):
        # make a copy of the source data
        x = x_.copy()
        y = y_.copy()
        weight = weight_.copy()
        t = t_.copy()

        # check dimensions
        if not (len(x) == len(y) == len(weight)):
            print("Warning, invalid dimension, reduced everything to the minimum dimension")
            n = min([len(x), len(y), len(weight)])
        else:
            n = len(x)

        # check dimensions t
        if t is not None:
            if len(t) != n + self.p + 1:
                print("Warning, the length of the array t does not not equal n + p + 1, nodes are set uniformly")
                # we set the nodes ourselves
                t = None
        # check for non-decrease t
        if t is not None:
            for i in range(len(t) - 1):
                if t[i] > t[i + 1]:
                    print("Warning, the array t must be non-decreasing, nodes are set uniformly")
                    # we set the nodes ourselves
                    t = None
                    break

        # check the positivity of weights
        for w in weight:
            if w < 0:
                print("Warning, weights must be positive, all weights are now equal to 1")
                weight = np.ones(n)
                break

        # checking that x, y is too short
        if n < self.p + 1:
            print("Warning, the number of control points less then p + 1, the curve has been replaced with a model one")
            n = self.p + 1
            # set some model curve
            x = [i for i in range(n)]
            y = [(-1) ** i for i in range(n)]
            weight = np.ones(n)
            t = None

        self.points = [Node(x[i], y[i], weight[i]) for i in range(0, n)]

        if t is not None:
            self.t = t
        else:
            # define uniform nodes ourselves
            n_t = n + self.p + 1
            self.t = [i / n_t for i in range(n_t)]

        # the first p + 1 t is 0 so that the curve starts from the first point
        if is_clamped_start:
            for i in range(self.p + 1):
                self.t[i] = 0
        # the last p + 1 t equals 1 for the curve to reach the end point
        if is_clamped_end:
            for i in range(self.p + 1):
                self.t[-i - 1] = 1

        self.t_start = self.t[self.p]
        self.t_end = self.t[-self.p - 1]
        # self.print_points()
        return

    def find_sector(self, t):
        if t < 0:
            return -1
        if t > 1:
            return -1
        for i in range(0, len(self.t) - 1):
            cur_t = self.t[i]
            next_t = self.t[i + 1]
            if cur_t <= t < next_t:
                # print(i, cur_t, next_t)
                return i

    def get_point(self, cur_t):

        # print("cur_t: ", cur_t)
        if cur_t == self.t_end:
            ind = len(self.points) - 1
        else:
            ind = self.find_sector(cur_t)
        # print("ind: ", ind)

        key_lines = []
        prev_points = [self.points[g] for g in range(ind - self.p, ind + 1)]
        for k in range(0, self.p):
            cur_points = []
            h = 0
            for j in range(ind - self.p + k + 1, ind + 1):
                t_j = self.t[j]
                t_j_p_k = self.t[j + self.p - k]

                denominator = t_j_p_k - t_j
                if denominator == 0:
                    tmp_alpha = 0
                else:
                    tmp_alpha = (cur_t - t_j) / denominator

                new_x = (1 - tmp_alpha) * prev_points[h].x * prev_points[h].weight + tmp_alpha * \
                    prev_points[h + 1].x * prev_points[h + 1].weight
                new_y = (1 - tmp_alpha) * prev_points[h].y * prev_points[h].weight + tmp_alpha * \
                    prev_points[h + 1].y * prev_points[h + 1].weight
                new_weight = (1 - tmp_alpha) * prev_points[h].weight + tmp_alpha * prev_points[h + 1].weight
                new_point = Node(new_x / new_weight, new_y / new_weight, new_weight)

                cur_points.append(new_point)
                h = h + 1
            key_lines.append([[point.x, point.y] for point in prev_points])
            prev_points = cur_points
        key_lines.append([[point.x, point.y] for point in prev_points])
        x = prev_points[0].x
        y = prev_points[0].y
        return [x, y], key_lines

    def get_curve(self, num_of_segments=500):
        curve = []
        key_lines = []
        step = (self.t_end - self.t_start) / num_of_segments
        for i in range(0, num_of_segments + 1):
            cur_t = self.t_start + i * step
            point, tmp_key_lines = self.get_point(cur_t)

            if point is not None and tmp_key_lines is not None:
                key_lines.append(tmp_key_lines)
                curve.append(point)
        return curve, key_lines
