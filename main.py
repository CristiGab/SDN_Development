import time
import requests
import json
from datetime import date, datetime
from data_structures.datacenter import Datacenter

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    for retries in range(0, max_retries):
        try:
            response = requests.get(url)
            data = response.json()
            return data
        except ValueError:
            print("Request failed, try again... Request number: {}".format(retries + 1))
            time.sleep(delay_between_retries)


def to_json(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    else:
        return obj.__dict__


def main():
    """
    Main entry to our program.
    """
    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [Datacenter(key, value) for key, value in data.items()]
    # Using the json.dumps to format processed data in json format, for further processing if necessary
    json_datacenters = json.dumps(datacenters, default=to_json, indent=4)

    # Display the json data and writing the output in parsed_output.json, for visibility
    print(json_datacenters)
    f = open('parsed_output.json', 'w')
    f.write(str(json_datacenters))


if __name__ == '__main__':
    main()
