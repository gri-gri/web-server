from PIL import Image


def func(path, filename, exclusion=(4, 4)):
    img = Image.open(path + '/' + filename)
    pixels = img.load()
    x, y = img.size

    step = x // 4

    for i in range(1, 5):
        for j in range(1, 5):
            if (j, i) != exclusion:
                im = img.crop(((i - 1) * step, (j - 1) * step, i * step, j * step))
                im.save(path + '/' + "image{}{}.png".format(j, i))


if __name__ == '__main__':
    func("image.bmp")
