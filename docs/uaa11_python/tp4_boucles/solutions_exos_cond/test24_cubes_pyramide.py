def cubes_pyramide(nbcote):
    vol = 0
    while nbcote >0:
        vol = vol + nbcote**3
        nbcote = nbcote -2
    return vol
assert cubes_pyramide(1) == 1
assert cubes_pyramide(11) == 2556
assert cubes_pyramide(15) == 8128