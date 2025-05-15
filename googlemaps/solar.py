#See https://developers.google.com/maps/documentation/solar/overview for API documentation.


def solar_building_insights_closest(
    client,
    coord_dict,
    requiredQuality=None,
    experiments=None
):
    """Retrieves solar potential data for the nearest building from the Solar API.

    This function makes a GET request to find the closest known building
    with solar potential information for the specified coordinates.

    Args:
        client: Authenticated client object for API requests
        coord_dict (dict): Location coordinates with keys:
            - 'latitude': Location latitude (float)
            - 'longitude': Location longitude (float)
        requiredQuality (str, optional): Minimum imagery quality requirement.
            Allowed values depend on API implementation. Defaults to HIGH.
        experiments (list, optional): List of experimental features to enable.

    Returns:
        dict: API response containing solar potential insights

    Raises:
        ValueError: For invalid coordinates or parameter types
        Exception: API request failures

    Example:
        >>> coords = {'latitude': 37.7749, 'longitude': -122.4194}
        >>> response = solar_building_insights_closest(client, coords)
        >>> print(response['solarPotential'])
        {...}

    API Documentation:
        https://developers.google.com/solar
    """
    url = "/v1/buildingInsights:findClosest"
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

    # Add optional parameters
    if requiredQuality:
        params['requiredQuality'] = requiredQuality

    if experiments:
        if not isinstance(experiments, list):
            raise ValueError("experiments must be a list of strings")
        params['experiments[]'] = experiments

    return client._request(
        base_url="https://solar.googleapis.com",
        url=url,
        params=params,
        post_json=None
    )


def solar_data_layers_get(
    client,
    coord_dict,
    radiusMeters,
    view=None,
    requiredQuality=None,
    pixelSizeMeters=None,
    exactQualityRequired=None,
    experiments=None
):
    """Retrieves solar data layers for a specified geographic region from the Solar API.

    Args:
        client: Authenticated client object for API requests
        coord_dict (dict): Location coordinates with keys:
            - 'latitude': Location latitude (float)
            - 'longitude': Location longitude (float)
        radiusMeters (float): Required. Radius in meters for the analysis region.
        view (str, optional): Data layer view type to return
        requiredQuality (str, optional): Minimum imagery quality requirement
        pixelSizeMeters (float, optional): Resolution in meters/pixel (0.1, 0.25, 0.5, 1.0)
        exactQualityRequired (bool, optional): Require exact quality match
        experiments (list, optional): Experimental features to enable

    Returns:
        dict: API response containing solar data layers

    Raises:
        ValueError: For invalid parameters or coordinates
        Exception: API request failures

    Example:
        >>> coords = {'latitude': 34.0522, 'longitude': -118.2437}
        >>> data = solar_data_layers_get(client, coords, 50.0, pixelSizeMeters=0.25)
        >>> print(data['imageryDate'])
        '2023-07-15'

    API Documentation:
        https://developers.google.com/solar
    """
    url = "/v1/dataLayers:get"
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

    # Validate radius
    if not isinstance(radiusMeters, (int, float)) or radiusMeters <= 0:
        raise ValueError("radiusMeters must be a positive number")
    params['radiusMeters'] = radiusMeters

    # Validate pixel size
    if pixelSizeMeters:
        allowed_pixel_sizes = {0.1, 0.25, 0.5, 1.0}
        if pixelSizeMeters not in allowed_pixel_sizes:
            raise ValueError(f"pixelSizeMeters must be one of {allowed_pixel_sizes}")
        params['pixelSizeMeters'] = pixelSizeMeters

    # Handle boolean conversion
    if exactQualityRequired is not None:
        if not isinstance(exactQualityRequired, bool):
            raise ValueError("exactQualityRequired must be a boolean")
        params['exactQualityRequired'] = str(exactQualityRequired).lower()

    # Add optional parameters
    if view:
        params['view'] = view
        
    if requiredQuality:
        params['requiredQuality'] = requiredQuality

    if experiments:
        if not isinstance(experiments, list):
            raise ValueError("experiments must be a list of strings")
        params['experiments[]'] = experiments

    return client._request(
        base_url="https://solar.googleapis.com",
        url=url,
        params=params,
        post_json=None
    )