
import numpy as np
import cv2
import screeninfo
import sys


def main():
    screens = screeninfo.get_monitors()

    for screen_id in range(0, len(screens)):
        screen = screens[screen_id]
        window_name = 'projector ' + str(screen_id)

        width, height = screen.width, screen.height

        cx = int(width/2)
        cy = int(height/2)

        marker_size = int(width * 0.004)
        marker_halfsize = int(width * 0.004 / 2)

        image = np.zeros((int(width), height, 3), dtype=np.float32)
        image = cv2.resize(image, (width, height),
                           interpolation=cv2.INTER_CUBIC)

        # center
        image[cy-marker_halfsize:cy+marker_size-marker_halfsize, cx -
              marker_halfsize:cx+marker_size-marker_halfsize] = np.ones((1, 3))

        # top left
        image[0: marker_size, 0: marker_size] = np.ones((1, 3))

        # top right
        image[0: marker_size, width-marker_size:width] = np.ones((1, 3))

        # bottom left
        image[height-marker_size:height, 0: marker_size] = np.ones((1, 3))

        # bottom right
        image[height-marker_size:height, width -
              marker_size:width] = np.ones((1, 3))

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.moveWindow(window_name, screen.x -
                       screen_id, screen.y - screen_id)
        cv2.setWindowProperty(window_name, cv2.WINDOW_NORMAL,
                              cv2.WINDOW_FULLSCREEN)
        cv2.imshow(window_name, image)

    pass


if __name__ == "__main__":
    main()

    cv2.waitKey()
    cv2.destroyAllWindows()
