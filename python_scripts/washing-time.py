import sys

def unit_mapper(value, ceiling, floor):
    value = max(0, value - floor)
    return min(ceiling - floor, value) / float (ceiling - floor)

def time_mapper(minutes_until_sunset):
    return unit_mapper(minutes_until_sunset, 540, 0)

def temperature_mapper(temperature):
    return unit_mapper(temperature, 40, 5)

def humidity_mapper(humidity):
    return 1 - unit_mapper(humidity, 100, 25)

def confidence(time, temperature, humidity):
    time_weight = 0.5
    temperature_weight = 1
    humidity_weight = 1.3

    weights = time_weight + temperature_weight + humidity_weight

    return (
        time_mapper(time) * time_weight +
        temperature_mapper(temperature) * temperature_weight +
        humidity_mapper(humidity) * humidity_weight
        ) / weights

def confidence_group(confidence):
    return \
        'fantastic' if confidence > 0.9 else \
        'really ideal' if confidence > 0.8 else \
        'great' if confidence > 0.7 else \
        'good' if confidence > 0.6 else \
        'just ok' if confidence > 0.5 else \
        'tollerable' if confidence > 0.4 else \
        'bad'

print(confidence_group(confidence(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))))
