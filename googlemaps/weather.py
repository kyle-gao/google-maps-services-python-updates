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

def weather_history_hourly(
    client,
    coord_dict,
    unitsSystem=None,
    pageSize=None,
    pageToken=None,
    hours=None,
    languageCode=None
):
    """Fetches historical hourly weather data from the Google Weather API.

    This function makes a GET request to retrieve past weather conditions
    for the specified coordinates with optional pagination and filtering.

    Args:
        client: Authenticated client object for API requests
        coord_dict (dict): Location coordinates with keys:
            - 'latitude': Location latitude (float)
            - 'longitude': Location longitude (float)
        unitsSystem (str, optional): Unit system (METRIC/IMPERIAL/METRIC_UK)
        pageSize (int, optional): Records per page (1-24, default 24)
        pageToken (str, optional): Pagination token for subsequent pages
        hours (int, optional): Total hours to retrieve (1-24, default 24)
        languageCode (str, optional): Response language (BCP-47 format)

    Returns:
        dict: API response containing historical weather data

    Raises:
        ValueError: For invalid coordinates or parameter ranges
        Exception: API request failures


    API Documentation:
        https://developers.google.com/maps/documentation/weather
    """
    url = "/v1/history/hours:lookup"
    params = {}

    # Validate coordinates
    if isinstance(coord_dict, dict):
        if 'latitude' in coord_dict and 'longitude' in coord_dict:
            params['location.latitude'] = coord_dict['latitude']
            params['location.longitude'] = coord_dict['longitude']
        else:
            raise ValueError("coord_dict must contain 'latitude' and 'longitude'")
    else:
        raise ValueError("coord_dict must be a dictionary")

    # Validate and add optional parameters
    if unitsSystem:
        params['unitsSystem'] = unitsSystem

    if pageSize:
        if not 1 <= pageSize <= 24:
            raise ValueError("pageSize must be between 1-24")
        params['pageSize'] = pageSize

    if pageToken:
        params['pageToken'] = pageToken

    if hours:
        if not 1 <= hours <= 24:
            raise ValueError("hours must be between 1-24")
        params['hours'] = hours

    if languageCode:
        params['languageCode'] = languageCode

    return client._request(
        base_url="https://weather.googleapis.com",
        url=url,
        params=params,
        post_json=None
    )

def weather_forecast_hourly(
    client,
    coord_dict,
    unitsSystem=None,
    pageSize=None,
    pageToken=None,
    hours=None,
    languageCode=None
):
    """Retrieves hourly weather forecast data from the Google Weather API.

    This function makes a GET request to fetch future weather predictions
    for the specified location with configurable time window and units.

    Args:
        client: Authenticated client object for API requests
        coord_dict (dict): Location coordinates with keys:
            - 'latitude': Location latitude (float)
            - 'longitude': Location longitude (float)
        unitsSystem (str, optional): Unit system (METRIC/IMPERIAL/METRIC_UK)
        pageSize (int, optional): Records per page (1-24, default 24)
        pageToken (str, optional): Pagination token for subsequent pages
        hours (int, optional): Total hours to forecast (1-240, default 240)
        languageCode (str, optional): Response language (BCP-47 format)

    Returns:
        dict: API response containing hourly forecast data

    Raises:
        ValueError: For invalid coordinates or parameter ranges
        Exception: API request failures

    Example:
        >>> coords = {'latitude': 40.7128, 'longitude': -74.0060}
        >>> forecast = weather_forecast_hourly(client, coords, hours=48)
        >>> print(forecast['hourlyForecasts'][0]['temperature'])
        65.8

    API Documentation:
        https://developers.google.com/maps/documentation/weather
    """
    url = "/v1/forecast/hours:lookup"
    params = {}

    # Validate coordinates
    if isinstance(coord_dict, dict):
        if 'latitude' in coord_dict and 'longitude' in coord_dict:
            params['location.latitude'] = coord_dict['latitude']
            params['location.longitude'] = coord_dict['longitude']
        else:
            raise ValueError("coord_dict must contain 'latitude' and 'longitude'")
    else:
        raise ValueError("coord_dict must be a dictionary")

    # Add optional parameters with validation
    if unitsSystem:
        params['unitsSystem'] = unitsSystem

    if pageSize:
        if not 1 <= pageSize <= 24:
            raise ValueError("pageSize must be between 1-24")
        params['pageSize'] = pageSize

    if pageToken:
        params['pageToken'] = pageToken

    if hours:
        if not 1 <= hours <= 240:
            raise ValueError("hours must be between 1-240")
        params['hours'] = hours

    if languageCode:
        params['languageCode'] = languageCode

    return client._request(
        base_url="https://weather.googleapis.com",
        url=url,
        params=params,
        post_json=None
    )

def weather_forecast_daily(
    client,
    coord_dict,
    unitsSystem=None,
    pageSize=None,
    pageToken=None,
    days=None,
    languageCode=None
):
    """Retrieves daily weather forecast data from the Google Weather API.

    This function makes a GET request to fetch multi-day weather predictions
    for the specified location with configurable duration and units.

    Args:
        client: Authenticated client object for API requests
        coord_dict (dict): Location coordinates with keys:
            - 'latitude': Location latitude (float)
            - 'longitude': Location longitude (float)
        unitsSystem (str, optional): Unit system (METRIC/IMPERIAL/METRIC_UK)
        pageSize (int, optional): Records per page (1-10, default 5)
        pageToken (str, optional): Pagination token for subsequent pages
        days (int, optional): Total days to forecast (1-10, default 10)
        languageCode (str, optional): Response language (BCP-47 format)

    Returns:
        dict: API response containing daily forecast data

    Raises:
        ValueError: For invalid coordinates or parameter ranges
        Exception: API request failures

    Example:
        >>> coords = {'latitude': 51.5074, 'longitude': -0.1278}
        >>> forecast = weather_forecast_daily(client, coords, days=7)
        >>> print(forecast['dailyForecasts'][0]['highTemp'])
        22.5

    API Documentation:
        https://developers.google.com/maps/documentation/weather
    """
    url = "/v1/forecast/days:lookup"
    params = {}

    # Validate coordinates
    if isinstance(coord_dict, dict):
        if 'latitude' in coord_dict and 'longitude' in coord_dict:
            params['location.latitude'] = coord_dict['latitude']
            params['location.longitude'] = coord_dict['longitude']
        else:
            raise ValueError("coord_dict must contain 'latitude' and 'longitude'")
    else:
        raise ValueError("coord_dict must be a dictionary")

    # Add optional parameters with validation
    if unitsSystem:
        params['unitsSystem'] = unitsSystem

    if pageSize:
        if not 1 <= pageSize <= 10:
            raise ValueError("pageSize must be between 1-10")
        params['pageSize'] = pageSize

    if pageToken:
        params['pageToken'] = pageToken

    if days:
        if not 1 <= days <= 10:
            raise ValueError("days must be between 1-10")
        params['days'] = days

    if languageCode:
        params['languageCode'] = languageCode

    return client._request(
        base_url="https://weather.googleapis.com",
        url=url,
        params=params,
        post_json=None
    )