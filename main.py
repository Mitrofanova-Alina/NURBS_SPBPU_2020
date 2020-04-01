from matplotlib import pyplot as plt
import numpy as np

from nurbs import NURBSpline
from animation import draw_animation


def test_function(key_point_x, key_point_y, weight, knots, degree, num_of_segments, filename="spline",
                  is_clamped_start=False, is_clamped_end=False):
    spline_maker = NURBSpline(degree)
    spline_maker.set_points(key_point_x, key_point_y, weight, knots, is_clamped_start, is_clamped_end)
    curve, key_lines = spline_maker.get_curve(num_of_segments)
    # take the real points where the spline was calculated
    draw_x = spline_maker.get_key_point_x()
    draw_y = spline_maker.get_key_point_y()

    draw_animation(draw_x, draw_y, curve, key_lines, filename)
    # spline graph
    fig, ax = plt.subplots(1, 1)
    ax.plot(draw_x, draw_y, "o", color="dodgerblue")
    ax.plot(draw_x, draw_y, color="dodgerblue")
    x = [point[0] for point in curve]
    y = [point[1] for point in curve]
    # print(x)
    # print(y)
    ax.plot(x, y, color="darkorange")
    ax.plot(x, y, "*", color="green")

    fig.show()
    plt.close(fig)


def main():

    """
    # Example 1
    
    filename = "rounding"
    key_point_x = [0.25, 0, 0.4, 0.75, 1.5, 2, 0.9]
    key_point_y = [0, 0.25, 1, 1.25, 1.1, 0.3, 0]
    weight = np.ones(len(key_point_x))
    degree = 3
    n = len(key_point_x) + degree + 1
    knots = [i / n for i in range(n)]
    num_of_segments = 100
    is_clamped_end = True
    is_clamped_start = True
    """

    """
    # Example 2

    filename = "wave"
    key_point_x = [0, 0.25,  0.5,  0.75,     1, 1.25,  1.5, 1.75,     2,  2.25, 2.5]
    key_point_y = [0, 0.25, 0.25, -0.25, -0.25,    0, 0.25, 0.25, -0.25, -0.25, 0]
    weight = np.ones(len(key_point_x))
    degree = 3
    n = len(key_point_x) + degree + 1
    knots = [i / n for i in range(n)]
    num_of_segments = 100
    is_clamped_end = True
    is_clamped_start = True
    """

    """
    # Example 3

    filename = "short_wave"
    key_point_x = [0, 0.25,  0.5,  0.75,     1, 1.25]
    key_point_y = [0, 0.25, 0.25, -0.25, -0.25,    0]
    weight = np.ones(len(key_point_x))
    degree = 3
    n = len(key_point_x) + degree + 1
    knots = [i / n for i in range(n)]
    num_of_segments = 100
    is_clamped_end = True
    is_clamped_start = True
    """

    # Example 3

    filename = "heart"
    key_point_x = [5, -5, -2, 0, 2, 5, -5]
    key_point_y = [-5, 2, 5, 2, 5, 2, -5]
    weight = np.ones(len(key_point_x))
    degree = 2
    knots = [0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.7, 0.8, 0.9]
    num_of_segments = 100
    is_clamped_end = False
    is_clamped_start = False

    test_function(key_point_x=key_point_x, key_point_y=key_point_y, weight=weight, knots=knots, degree=degree,
                  num_of_segments=num_of_segments, filename=filename,
                  is_clamped_start=is_clamped_start, is_clamped_end=is_clamped_end)


if __name__ == "__main__":
    main()
