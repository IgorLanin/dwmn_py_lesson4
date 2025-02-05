from PIL import Image

image = Image.open("monro.jpg")
red_image, green_image, blue_image = image.split()

coordinates_red_left = (50, 0, red_image.width, red_image.height)
monro_red_left = red_image.crop(coordinates_red_left)
coordinates_red_middle = (25, 0, 671, red_image.height)
monro_red_middle = red_image.crop(coordinates_red_middle)

monro_red_blend = Image.blend(monro_red_left, monro_red_middle, 0.3)


coordinates_blue_right = (0, 0, 646, blue_image.height)
monro_blue_right = blue_image.crop(coordinates_blue_right)
coordinates_blue_middle = (25, 0, 671, blue_image.height)
monro_blue_middle = blue_image.crop(coordinates_blue_middle)

monro_blue_blend = Image.blend(monro_blue_right, monro_blue_middle, 0.3)


coordinates_green_middle = (25, 0, 671, green_image.height)

monro_green_middle = green_image.crop(coordinates_green_middle)


final_monro = Image.merge("RGB", (monro_red_blend, monro_green_middle, monro_blue_blend))
final_monro.save("final_monro.jpg")

final_monro.thumbnail((80, 80))
final_monro.save("final_monro_mini.jpg")