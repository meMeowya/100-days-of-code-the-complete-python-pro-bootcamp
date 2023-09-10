import os

import requests

# Important Sheety API key, Sheety username are stored as environment variables.
SHEETY_API = os.environ["SHEETY_AUTH_BEARER"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/prices"


class DataManager:

    headers = {
        "Authorization": SHEETY_API
    }

    def get_column(self, column_name):
        """Retrieves column_name data from Google Sheet. Returns column_name data."""

        column = []

        column_response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)
        column_response.raise_for_status()
        sheety_data = column_response.json()['prices']

        for each_entry in sheety_data:
            column.append(each_entry[column_name])

        return column

    def update_column(self, column, column_name):
        """Updates column_name data in the Google Sheet."""

        object_id = 2
        for each_entry in range(len(column)):
            column_endpoint = f"{SHEETY_ENDPOINT}/{id}"
            column_param = {
                "price": {
                    column_name: column[each_entry]
                }
            }
            column_response = requests.put(url=column_endpoint, json=column_param, headers=self.headers)
            object_id += 1