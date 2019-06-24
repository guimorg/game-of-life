import numpy as np
import matplotlib.pyplot as plt

from game import Game

from matplotlib import animation


if __name__ == "__main__":
    game = Game()

    # gen = np.array([
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 1, 0, 0, 0, 0],
    #     [0, 1, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    # ])

    gen = np.round(np.random.random((50, 50)))

    # Plotting Stuff
    fig = plt.figure()
    ax = plt.axes()
    ax.set_axis_off()
    fig.patch.set_facecolor('#d8dcd6')
    im = plt.imshow(gen, cmap='binary')

    def init():
        im.set_data(np.zeros(shape=(10, 10)))
        return im,

    def animate(i):
        global gen  # Hate to use global variables
        gen = game.next_generation(gen)
        im.set_array(gen)
        return im,

    anim = animation.FuncAnimation(
        fig,
        animate,
        init_func=init,
        frames=1000,
        interval=300,
        blit=True
    )

    anim.save('img/conway.gif', writer='imagemagick', fps=60)
