import os

class Connector:

    @property
    def payload(self):
        """Payload for the API url"""
        return {'Authorization': f'Bearer {os.environ["ACCESS_TOKEN"]}'}

    @property
    def api_url(self):
        """THe url for the API"""
        return 'https://www.strava.com/api/v3'

    def create_api_url(self, urlComponents):
        components = [self.api_url]
        components.extend(urlComponents)
        return '/'.join(components)
