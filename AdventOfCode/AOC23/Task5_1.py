with open("Task_Day5.txt","r") as infile:
    lines = infile.readlines()
print(len(lines))
seeds = map(int,lines[0].split()[1:])

seed_to_soil_map = [] # destination start, source start, range len
for i in range(3,13):
    seed_to_soil_map.append(list(map(int,lines[i].split())))
    
soil_to_fertilizer_map = [] # destination start, source start, range len
for i in range(15,24):
    soil_to_fertilizer_map.append(list(map(int,lines[i].split())))
    
fertilizer_to_water_map = [] # destination start, source start, range len
for i in range(26,68):
    fertilizer_to_water_map.append(list(map(int,lines[i].split())))
    
water_to_light_map = [] # destination start, source start, range len
for i in range(70,114):
    water_to_light_map.append(list(map(int,lines[i].split())))
    
light_to_temperature_map = [] # destination start, source start, range len
for i in range(116,162):
    light_to_temperature_map.append(list(map(int,lines[i].split())))

temperature_to_humidity_map = [] # destination start, source start, range len
for i in range(164,191):
    temperature_to_humidity_map.append(list(map(int,lines[i].split())))
    
humidity_to_location_map = [] # destination start, source start, range len
for i in range(193,221):
    humidity_to_location_map.append(list(map(int,lines[i].split())))

def track_foward(sources,target_map):
    destinations = []
    for each in sources:
        destination = -1
        for temp_map in target_map:
            if each > temp_map[1] and each < (temp_map[1] + temp_map[2]):
                destination = each - temp_map[1] + temp_map[0]
                break
        if destination < 0:
            destination = each
        destinations.append(destination)
    return destinations

def track_location(seeds):
    soils = track_foward(seeds,seed_to_soil_map)
    fertilizers = track_foward(soils, soil_to_fertilizer_map)
    waters = track_foward(fertilizers, fertilizer_to_water_map)
    lights = track_foward(waters, water_to_light_map)
    temperatures = track_foward(lights, light_to_temperature_map)
    humiditys = track_foward(temperatures, temperature_to_humidity_map)
    locations = track_foward(humiditys, humidity_to_location_map)
    return locations

print(min(track_location(seeds)))