from matplotlib import pyplot as plt
from nurbs import NURBS
from animation import draw_animation


def main():
    # name = "rounding"
    # X = [0.25, 0, 0.4, 0.75, 1.5, 2, 0.9]
    # Y = [0, 0.25, 1, 1.25, 1.1, 0.3, 0]

    name = "wave"
    X = [0, 0.25,  0.5,  0.75,     1, 1.25,  1.5, 1.75,     2,  2.25, 2.5]
    Y = [0, 0.25, 0.25, -0.25, -0.25,    0, 0.25, 0.25, -0.25, -0.25, 0]

    #X = [0, 0.25,  0.5,  0.75,     1, 1.25]
    #Y = [0, 0.25, 0.25, -0.25, -0.25,    0]

    W = [1 for i in range(len(X))]
    # the degree of the spline
    p = 3
    n = len(X) + p + 1
    T = [i / n for i in range(n)]

    # the number of partition samples
    # if num_of_segments = 10, it is convenient to watch the construction of the iteration
    # if num_of_segments = 100 the curve itself
    num_of_segments = 100

    spline_maker = NURBS(p)
    spline_maker.set_points(X, Y, W, T, True, True)
    curve, key_lines = spline_maker.get_curve(num_of_segments)
    # take the real points where the spline was calculated
    draw_x = spline_maker.get_key_point_x()
    draw_y = spline_maker.get_key_point_y()

    draw_animation(draw_x, draw_y, curve, key_lines, name)
    # spline graph
    fig, ax = plt.subplots(1, 1)
    ax.plot(draw_x, draw_y, "o", color="dodgerblue")
    ax.plot(draw_x, draw_y, color="dodgerblue")
    x = [point[0] for point in curve]
    y = [point[1] for point in curve]
    #print(x)
    #print(y)
    ax.plot(x, y, color="darkorange")
    ax.plot(x, y, "*", color="green")

    fig.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
