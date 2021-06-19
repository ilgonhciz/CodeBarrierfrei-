import requests


def get_toilets(lat, lon):
    pass
    # bbox =
    # 'https://overpass-api.de/api/interpreter?data=%5Bout:json%5D%5Btimeout:25%5D;(nwr%5B%22toilets:wheelchair%22%5D({}}););out%20body;%3E;out%20skel%20qt()'.format(bbox)


def main():
    query = 'Sushi Sano München'
    nom_url = 'https://nominatim.openstreetmap.org/search?q={}&limit=1&extratags=1&format=json'.format(query)
    json_obj = get_json(nom_url)

    lat = json_obj[0]['lat']
    lon = json_obj[0]['lon']
    place_id = json_obj[0]['place_id']
    try:
        website = json_obj[0]['extratags']['website']
    except KeyError:
        website = ''
    try:
        wheel = json_obj[0]['extratags']['wheelchair']
    except KeyError:
        wheel = ''

    osm_url = 'https://www.openstreetmap.org/api/0.6/node/{}.json'.format(place_id)
    json_obj = get_json(osm_url)
    fb_link = json_obj['elements']['tags']['contact:facebook']
    tw_link = json_obj['elements']['tags']['contact:twitter']
    insta_link = json_obj['elements']['tags']['contact:instagram']


def get_json(url):
    session = requests.session()
    response = session.get(url)
    if response.ok:
        json_obj = response.json()
    return json_obj


if __name__ == '__main__':
    main()
