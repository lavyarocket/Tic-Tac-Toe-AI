import sys

import engine as game


if __name__ == "__main__":
    p1_name = sys.argv[1]
    p2_name = sys.argv[2]

    game.play(p1_name, p2_name)