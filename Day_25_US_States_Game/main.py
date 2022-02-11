import pandas

data = pandas.read_csv("squirrel_data.csv")

color_list = data["Primary Fur Color"].to_list()

gray = []
cinnamon = []
black = []

for x in color_list:
    if x == "Gray":
        gray.append(x)
    if x == "Cinnamon":
        cinnamon.append(x)
    if x == "Black":
        black.append(x)

black_count = len(black)
gray_count = len(gray)
cinnamon_count = len(cinnamon)

squirrel_data = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_count, gray_count, cinnamon_count]
}

df = pandas.DataFrame(squirrel_data)
df.to_csv("squirrel_count.csv")



