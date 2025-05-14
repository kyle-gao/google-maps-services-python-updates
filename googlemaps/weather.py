def weather_currentconditions(client, coord_dict, languageCode=None, unitsSystem = "METRIC"):
    """Fetches current weather conditions for a specific location from the Google Weather API.

    This function makes a GET request to the Google Weather API's current conditions endpoint
    to retrieve real-time weather data for the specified coordinates.

    Args:
        client: An authenticated client object for making API requests.
        coord_dict (dict): A dictionary containing latitude and longitude coordinates.
            Required keys:
                - 'latitude': Latitude of the location (float)
                - 'longitude': Longitude of the location (float)
        languageCode (str, optional): The language in which to return results.
            Defaults to None (API will use its default language).
        unitsSystem (str, Optional):
            One of "METRICS" or "IMPERIAL", API will default to imperial

    Returns:
        dict: A dictionary containing the API response with current weather conditions.

    Raises:
        ValueError: If coord_dict is not a dictionary or is missing required latitude/longitude keys.
        Exception: For any API request failures (handled by the client's _request method).



    API Documentation:
        https://developers.google.com/maps/documentation/weather
    """
    url = "/v1/currentConditions:lookup"
    
    params = {}
    
    if isinstance(coord_dict, dict):
        if 'latitude' in coord_dict and 'longitude' in coord_dict:
            params['location.latitude'] = coord_dict['latitude']
            params['location.longitude'] = coord_dict['longitude']
        else:
            raise ValueError("coord_dict must contain 'latitude' and 'longitude'")
    else:
        raise ValueError("coord_dict must be a dictionary containing latitude and longitude")
    
    if languageCode:
        params['languageCode'] = languageCode

    if unitsSystem:
        params["unitsSystem"] = unitsSystem
    
    return client._request(base_url="https://weather.googleapis.com", url=url, params=params, post_json=None)