from celluloid import Camera
from matplotlib import pyplot as plt

colors = [
    'green', 'r', 'black', 'grey', 'darksalmon',  'silver', 'rosybrown', 'firebrick',   'sienna',
    'sandybrown', 'mediumorchid', 'tan', 'gold', 'darkkhaki', 'lightgoldenrodyellow', 'olivedrab',
    'chartreuse', 'darkolivegreen', 'mediumaquamarine',  'darkslategrey', 'c', 'cadetblue', 'skyblue',
    'indigo', 'slategray', 'darkblue', "slateblue", 'blueviolet', 'purple', 'fuchsia', 'hotpink', 'pink',
    'springgreen', 'bisque', 'moccasin', 'lightgreen', 'mediumseagreen', 'mediumturquoise', 'dodgerblue', 'darkorange'
]


def draw_iteration(ax, curve, key_lines):
    c = 0
    c_max = len(colors)
    draw_x = []
    draw_y = []
    for key_line in key_lines:
        draw_x = [point[0] for point in key_line]
        draw_y = [point[1] for point in key_line]
        ax.plot(draw_x, draw_y, color=colors[c])
        ax.plot(draw_x, draw_y, "o", color=colors[c])
        c = (c + 1) % c_max
    ax.plot(draw_x, draw_y, "*", color=colors[c])

    draw_x = [point[0] for point in curve]
    draw_y = [point[1] for point in curve]
    ax.plot(draw_x, draw_y, color="darkorange")


def draw_animation(x, y, curve, key_lines, name="deBoor"):
    fig, ax = plt.subplots(1, 1)
    camera = Camera(fig)
    for i in range(0, len(curve)):
        ax.plot(x, y, "o", color="dodgerblue")
        ax.plot(x, y, color="dodgerblue")
        tmp_curve = curve[0:i+1]
        tmp_key_lines = key_lines[i]
        draw_iteration(ax, tmp_curve, tmp_key_lines)
        camera.snap()

    anim = camera.animate()
    anim.save("%s.gif" % name, writer="imagemagick")
    plt.close(fig)
