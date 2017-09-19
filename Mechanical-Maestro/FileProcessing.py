import os


def make_readable(song_name):
    in_filename = "RawMidis/{0}".format(song_name)
    out_filename = "ReadableMidis/" + in_filename.split("/")[-1][:-3] + "csv"

    cmd = '"midicsv-1.1\\Midicsv.exe" {0} {1}'.format(in_filename, out_filename)
    os.system(cmd)


if __name__ == "__main__":
    root = "/".join(__file__.split("/")[:-1])
    os.chdir(root)

    converted_songs = os.listdir("ReadableMidis")

    all_songs = os.listdir("RawMidis")

    for song in all_songs:
        if song.replace("mid", "csv") not in converted_songs:
            make_readable(song)
            print("processed " + song)
