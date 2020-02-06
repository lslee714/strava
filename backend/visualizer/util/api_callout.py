class ApiError(Exception):
    """Generic exception for API callouts"""


def api_callout(decoratedFn):
    def wrapped_fn(*args):
        response = decoratedFn(*args)
        if response.status_code != 200:
            errorMessage = response.json()['message']
            raise ApiError(f"Error in calling the API: {errorMessage}")
        else:
            return response.json()
    return wrapped_fn
