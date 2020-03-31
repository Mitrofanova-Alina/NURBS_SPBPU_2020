from celluloid import Camera
from matplotlib import pyplot as plt

colors = [
    'green', 'r', 'black', 'grey', 'darksalmon',  'silver', 'rosybrown', 'firebrick',   'sienna',
    'sandybrown', 'mediumorchid', 'tan', 'gold', 'darkkhaki', 'lightgoldenrodyellow', 'olivedrab',
    'chartreuse', 'darkolivegreen', 'mediumaquamarine',  'darkslategrey', 'c', 'cadetblue', 'skyblue',
    'indigo', 'slategray', 'darkblue', "slateblue", 'blueviolet', 'purple', 'fuchsia', 'hotpink', 'pink',
    'springgreen', 'bisque', 'moccasin', 'lightgreen', 'mediumseagreen', 'mediumturquoise','dodgerblue', 'darkorange'
]


def draw_iteration(ax, curve, key_lines):
    x = [point[0] for point in curve]
    y = [point[1] for point in curve]
    ax.plot(x, y, color="darkorange")

    c = 0
    for key_line in key_lines:
        x = [point[0] for point in key_line]
        y = [point[1] for point in key_line]
        ax.plot(x, y, color=colors[c])
        ax.plot(x, y, "o", color=colors[c])
        c += 1
    ax.plot(x, y, "*", color=colors[c])


def draw_animation(X, Y, curve, key_lines, name="deBoor"):
    fig, ax = plt.subplots(1, 1)
    camera = Camera(fig)
    for i in range(0, len(curve)):
        ax.plot(X, Y, "o", color="dodgerblue")
        ax.plot(X, Y, color="dodgerblue")
        tmp_curve = curve[0:i]
        tmp_key_lines = key_lines[i]
        draw_iteration(ax, tmp_curve, tmp_key_lines)
        camera.snap()

    anim = camera.animate()
    anim.save("%s.gif" % name, writer='imagemagick')
    plt.close(fig)
