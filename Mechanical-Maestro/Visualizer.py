import pygame as pg

from ImageCreation import *


if __name__ == "__main__":
    song_name = "elise"
    music_file = "/".join(__file__.split("/")[:-1]) + "/RawMidis/{0}.mid".format(song_name)

    img = get_image(song_name, 1000)
    data, size, mode = img.tobytes(), img.size, img.mode
    image = pg.image.fromstring(data, size, mode)
    image = pg.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))
    screen = pg.display.set_mode((image.get_width(), image.get_height()))
    screen.blit(image, (0, 0))
    pg.display.update()

    freq = 44100    # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 1024    # number of samples

    pg.mixer.init(freq, bitsize, channels, buffer)

    # set volume 0 to 1.0
    pg.mixer.music.set_volume(1.0)

    try:
        pg.mixer.music.load(music_file)
        print("Music file %s loaded!" % music_file)
    except pg.error:
        print("File %s not found! (%s)" % (music_file, pg.get_error()))

    pg.mixer.music.play()

    clock = pg.time.Clock()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
