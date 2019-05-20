kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(kingdom[0],kingdom[-1])
print(kingdom[0:3])
print(kingdom[2:5])
print(kingdom[4:])

ids = [4353,2314,2956,3382,9362,3900]
ids.remove(3382) ; print(ids)
location9362 = ids.index(9362) ; print(location9362)
ids.insert(location9362,4499) ; print(ids)
ids.extend([5566,1830]) ; print(ids)
ids.reverse() ; print(ids)
ids.sort() ; print(ids)
