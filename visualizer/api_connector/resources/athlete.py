import requests

from visualizer.util import api_callout

from ..connector import Connector

class AthleteApi:
    """Provides access to the api for athlete-related resources"""
    def __init__(self, athleteId):
        self.athleteId = str(athleteId)
        self.connector = Connector()

    @api_callout
    def get_info(self):
        urlComponents = ['athletes', self.athleteId]
        url = self.connector.create_api_url(urlComponents)
        return requests.get(url, params=self.connector.payload)

    @api_callout
    def get_stats(self):
        urlComponents = ['athletes', self.athleteId, 'stats']
        url = self.connector.create_api_url(urlComponents)
        return requests.get(url, params=self.connector.payload)

    @api_callout
    def get_activities(self):
        urlComponents = ['athlete', 'activities']
        url = self.connector.create_api_url(urlComponents)
        payload = self.connector.payload
        response = requests.get(url, params=payload)
        return response

