def moon_weight(weight, z, age):
    moon= weight*0.165
    for y in range(0,age):
        print(moon)
        moon=moon+z
moon_weight(60, 0.25, 5)