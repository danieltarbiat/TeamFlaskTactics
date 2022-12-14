from urllib.request import Request, urlopen
import json


def fetch_unit_images(dictionary, json_url, path_url):
    unit_image_links = {}
    request = Request(json_url, headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(request).read()
    data_json = json.loads(response)
    for unit in dictionary:
        for element in data_json:
            if element == "setData":
                for items in data_json[element]:
                    for properties in items:
                        if properties == "champions":
                            for values in items[properties]:
                                if values["apiName"] == unit:
                                    path = values["icon"].lower()
                                    end = path.find(".dds")
                                    path = path[:end] + ".png"
                                    unit_image_links[unit] = path_url + path
    return unit_image_links
