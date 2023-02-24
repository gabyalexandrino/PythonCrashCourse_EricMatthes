cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'fact': 'mountains andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'fact': 'mountains alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975453,
        'fact': 'mountains himilaya',
        }
}

for city, city_info in cities.items():
    print("\n" + city.title())
    county = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].title()
    print(f"Fica no {county}, com a população de {population} habitantes, e fica proximo das {fact}" )
