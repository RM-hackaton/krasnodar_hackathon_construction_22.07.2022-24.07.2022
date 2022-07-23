from re import findall

from requests import get


def get_number(text: str) -> int | float:
    result = findall(r"\d+\.?\d*", text.replace(' ', ''))[0]
    return float(result) if '.' in result else int(result)


def get_complexes():
    complexes = {
        'ЖК Novella': {},
        'ЖК Fresh': {},
        'ЖК AVrorA': {},
        'ЖК «Смородина»': {},
        'ЖК URAL': {},
        'ЖК «Спортивный Парк»': {},
    }

    url_districts = 'https://ask-yug.com/api/filter/commercial/'
    url_complexes = 'https://ask-yug.com/api/map/commercial/new_map.php'

    response = get(url_districts).json()['cityList'][0]
    city = response['name']
    districts = get(url_districts).json()['cityList'][0]['districts'][1:6]
    complexes_resp = get(url_complexes).json()['filters']['items']

    for district in districts:
        district_name = district["name"]

        for complex in district['complexes']:
            if (complex_name := complex['name']) \
                    in ('The Grand Palace', 'ЖК «Мелодия»'):
                continue

            complexes[complex_name]['district'] = district_name
            complexes[complex_name]['complex_class'] = complex['type'].capitalize()
            complexes[complex_name]['address'] = f"г. {city}, "

    for complex in complexes_resp:
        complex_name = complex['name']
        complexes[complex_name]['img'] = f"https://ask-yug.com/{complex['image']}"
        complexes[complex_name]['min_square'] = get_number(complex['area'])
        complexes[complex_name]['min_price'] = get_number(complex['price_text'])
        complexes[complex_name]['address'] += complex['address']

    complexes['ЖК URAL']['img'] = 'https://ask-yug.com/upload/iblock/17d/17dd85e2367468b6a6ad2d596803fa40.jpg'
    complexes['ЖК URAL']['min_price'] = 3036000
    complexes['ЖК URAL']['min_square'] = 13.8
    complexes['ЖК URAL']['address'] += 'ул. Уральская 87/7'

    return complexes


def get_houses_and_commercials():
    complexes = (
        'ЖК Novella',
        'ЖК Fresh',
        'ЖК AVrorA',
        'ЖК «Смородина»',
        'ЖК URAL',
        'ЖК «Спортивный Парк»',
    )

    urls = (
        'https://ask-yug.com/api/filter/commercial/get/?objects=3536&types=0&price[min]=1200000%20%E2%82%BD&price[max]=12195000%20%E2%82%BD&area[min]=15.00%20%D0%BC%C2%B2&area[max]=127.70%20%D0%BC%C2%B2',
        'https://ask-yug.com/api/filter/commercial/get/?objects=23806&types=0&price[min]=2692200%20%E2%82%BD&price[max]=14116000%20%E2%82%BD&area[min]=18.23%20%D0%BC%C2%B2&area[max]=94.10%20%D0%BC%C2%B2',
        'https://ask-yug.com/api/filter/commercial/get/?objects=51262&types=0&price[min]=4755420%20%E2%82%BD&price[max]=71125600%20%E2%82%BD&area[min]=17.22%20%D0%BC%C2%B2&area[max]=187.17%20%D0%BC%C2%B2',
        'https://ask-yug.com/api/filter/commercial/get/?objects=42702&types=0&price[min]=6107000%20%E2%82%BD&price[max]=9703000%20%E2%82%BD&area[min]=38.40%20%D0%BC%C2%B2&area[max]=58.80%20%D0%BC%C2%B2',
        'https://ask-yug.com/api/filter/commercial/get/?objects=54158&types=0&price[min]=500000%20%E2%82%BD&price[max]=41088200%20%E2%82%BD&area[min]=12.80%20%D0%BC%C2%B2&area[max]=186.76%20%D0%BC%C2%B2',
        'https://ask-yug.com/api/filter/commercial/get/?objects=3169&types=0&price[min]=7974000%20%E2%82%BD&price[max]=9151000%20%E2%82%BD&area[min]=131.90%20%D0%BC%C2%B2&area[max]=152.50%20%D0%BC%C2%B2',
    )

    commercials = {}
    houses = {}

    id = 1
    for url in urls:

        commercials_resp = get(url).json()

        for commercial in commercials_resp:
            complex_name = commercial['object']['name']
            liter = get_number(commercial['liter'])

            house_name = f'{complex_name} лит. {liter}'

            if house_name not in houses:
                houses[house_name] = {}
                houses[house_name]['id'] = id
                id += 1

            houses[house_name].update(
                (('complex_id', complexes.index(complex_name) + 1),
                 ('parking', commercial['parking'].capitalize()),
                 ('finished', commercial['finished']),
                 ('liter', get_number(commercial['liter'])))
            )

            commercial_name = f"{commercial['name']}-{commercial['id']}"
            commercials[commercial_name] = {
                'house_id': houses[house_name]['id'],
                'owner_id': 0,
                'floor': int(commercial['floor']),
                'square': float(commercial['area']),
                'price': float(commercial['price'].replace(' ', '')),
                'price_meter': float(commercial['price_m'].replace(' ', '')),
                'plan': f"https://ask-yug.com/{commercial['plan']}",
                'status': 'Свободно',
            }

    return houses, commercials
