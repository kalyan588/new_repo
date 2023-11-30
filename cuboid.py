cd# writing function to calculate cuboid volume
def cuboid_volume(l):
    return (l*l*l)

length = [2, 1.1, -2.5, 2j, 'two']

for i in length:
    print(f'the volume of cuboide is :-->{cuboid_volume(i)}', )