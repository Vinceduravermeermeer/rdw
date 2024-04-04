import requests
import sys


def import_cars_plate(plate):
    """
    
    Import the cars by plate from the RDW data

    """
    # rdw endpoint (l609fr)
    endpoint = f'https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate}'

    # execute the request
    response = requests.get(endpoint)

    # check if the status_code is okay
    if not response.status_code == 200:
        print("Wrong link")
        sys.exit()

    # get the data from the response
    data = response.json()

    # if the list of cars is empty
    if len(data) == 0:
        print(f"❌ No cars found for license plate: {plate}")

    return data


def import_cars_brand(brand, large_amount=False):
    """
    
    Import the cars by brand from the RDW data

    """
    # rdw endpoint (l609fr)
    endpoint = f'https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}'

    # in case of more data
    if large_amount:
        endpoint = f"{endpoint}&$limit=150000" 

    # execute the request
    response = requests.get(endpoint)

    # check if the status_code is okay
    if not response.status_code == 200:
        print("Wrong link")
        sys.exit()

    # get the data from the response
    data = response.json()

    # if the list of cars is empty
    if len(data) == 0:
        print(f"❌ No cars found for brand: {brand}")

    return data