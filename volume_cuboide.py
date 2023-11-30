def cuboid_volume(l):
    if type(l) not in [int, float]:
        raise TypeError('the length of cuboide can only be a valid integer of float')
    return(l**3)