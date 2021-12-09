import colorgram

""" Creates color pallete from *.jpg"""
colors = colorgram.extract('../megaman.jpg', 20)

colors_list = []
color_tuple = ()

for x in colors:
    color_tuple = (x.rgb.r, x.rgb.g, x.rgb.b)
    colors_list.append(color_tuple)

print(colors_list)