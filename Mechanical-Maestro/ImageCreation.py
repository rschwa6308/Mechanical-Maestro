import numpy as np
from PIL import Image


def get_image(song, width):
    image_data = np.zeros((128, width, 3), dtype=np.uint8)
    image_data.fill(255)
    file = open("ReadableMidis/{0}.csv".format(song))
    lines = file.read().split("\n")

    # Pulses Per Quarter Note
    ppqn = int(lines[0].replace(" ", "").split(",")[-1])

    open_notes = []
    for line in lines:
        if "note" in line.lower():
            track, timestamp, _type, channel, note, velocity = line.replace(" ", "").split(",")
            track, timestamp, channel, note, velocity = int(track), int(timestamp), int(channel), int(note), int(velocity)
            current_beat = timestamp // (ppqn // 4)
            if current_beat >= width:
                break
            print(track)
            if velocity == 0 or _type.lower() == "note_off_c":
                if note in open_notes:
                    open_notes.remove(note)
            else:
                open_notes.append(note)

            for note in open_notes:
                image_data[127 - note, current_beat] = [0, 0, 0]

    image = Image.fromarray(image_data, "RGB")
    return image


if __name__ == "__main__":
    song_name = "elise"
    image = get_image(song_name, 500)
    image.save("Images/{0}.png".format(song_name))
    image.show()
