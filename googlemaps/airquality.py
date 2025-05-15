#See https://developers.google.com/maps/documentation/air-quality/overview for API documentation.

from googlemaps import convert

def airquality_heat_map(client, map_type="UAQI_INDIGO_PERSIAN", zoom=0, x=0, y=0, key=None):
    """
    Retrieve air quality heatmap tiles from Google's Air Quality API. See https://developers.google.com/maps/documentation/air-quality/heatmaps
    
    Args:
        client: The API client object with _request method.
        map_type (str): Type of air quality map. Allowed values:
            - "MAP_TYPE_UNSPECIFIED": The default value (server ignores this parameter)
            - "UAQI_RED_GREEN": Universal Air Quality Index red-green palette
            - "UAQI_INDIGO_PERSIAN": Universal Air Quality Index indigo-persian palette (default)
            - "PM25_INDIGO_PERSIAN": PM2.5 index indigo-persian palette
            - "GBR_DEFRA": Daily Air Quality Index (UK) color palette
            - "DEU_UBA": German Local Air Quality Index color palette
            - "CAN_EC": Canadian Air Quality Health Index color palette
            - "FRA_ATMO": France Air Quality Index color palette
            - "US_AQI": US Air Quality Index color palette
        zoom (int): Zoom level for the tile (typically 0-20 for map tiles).
        x (int): X coordinate of the tile in the map grid.
        y (int): Y coordinate of the tile in the map grid.
        x,y start at 0,0 on the top left, and increment up to the right and bottom.
        key (str, optional): Your API key if not already handled by the client.
    
    Returns:
        Response from the API containing the heatmap tile image data (usually PNG format).
    
    Raises:
        ValueError: If invalid parameters are provided.
        requests.exceptions.HTTPError: If the API request fails.
    
    Example:
        # Get a US AQI heatmap tile at zoom level 10, tile coordinates (123, 456)
        response = airquality_heat_map(client, "US_AQI", 10, 123, 456)
        
    Note:
        - The API returns image tiles that should be displayed on a map
        - Coordinate values should be valid for the specified zoom level
        - Requires proper authentication via API key
        - See https://developers.google.com/maps/documentation/air-quality for details
    """
    # Validate map_type against known values
    valid_map_types = {
        "MAP_TYPE_UNSPECIFIED",
        "UAQI_RED_GREEN",
        "UAQI_INDIGO_PERSIAN",
        "PM25_INDIGO_PERSIAN",
        "GBR_DEFRA",
        "DEU_UBA",
        "CAN_EC",
        "FRA_ATMO",
        "US_AQI"
    }
    
    if map_type not in valid_map_types:
        raise ValueError(f"Invalid map_type. Must be one of: {', '.join(valid_map_types)}")
    
    url = f"/v1/mapTypes/{map_type}/heatmapTiles/{zoom}/{x}/{y}"
    
    params = {}
    if key:
        params['key'] = key
    
    response = client._request(
        base_url="https://airquality.googleapis.com",
        url=url,
        params = params,
        extract_body=lambda response: response,
        requests_kwargs={"stream": True},
    )
    return response.iter_content()

def airquality_currentconditions(client, coord_dict, uaqiColorPalette=None, customLocalAqis=None, universalAqi=None, languageCode=None, EC_LOCAL_AQI = False,
                                 EC_HEALTH_RECOMMENDATIONS = False, EC_POLLUTANT_ADDITIONAL_INFO = False, EC_POLLUTANT_CONCENTRATION = False, EC_DOMINANT_POLLUTANT_CONCENTRATION = False):
    
    # See https://developers.google.com/maps/documentation/air-quality/reference/rest/v1/currentConditions/lookup for documentation.


    url = "/v1/currentConditions:lookup"

    params_post_json = {}

    if isinstance(coord_dict, dict):
        params_post_json["location"] = coord_dict
    else:
        raise ValueError(
            "Location argument must be a dictionary containing latitude and longitude")
    
    if uaqiColorPalette:
        params_post_json["uaqiColorPalette"] = uaqiColorPalette

    if customLocalAqis:
        params_post_json["customLocalAqis"] = customLocalAqis

    if universalAqi:
        params_post_json["universalAqi"] = universalAqi
        
    if languageCode:
        params_post_json["languageCode"] = languageCode


    extra_computations = []

    if EC_LOCAL_AQI:
        extra_computations.append("LOCAL_AQI")

    if EC_HEALTH_RECOMMENDATIONS:
        extra_computations.append("HEALTH_RECOMMENDATIONS")

    if EC_POLLUTANT_ADDITIONAL_INFO:
        extra_computations.append("POLLUTANT_ADDITIONAL_INFO")

    if EC_POLLUTANT_CONCENTRATION:
        extra_computations.append("POLLUTANT_CONCENTRATION")

    if EC_DOMINANT_POLLUTANT_CONCENTRATION:
        extra_computations.append("DOMINANT_POLLUTANT_CONCENTRATION")


    params_post_json["extraComputations"] = extra_computations    

    return client._request(base_url= "https://airquality.googleapis.com", url = url, params = {}, post_json= params_post_json)



def airquality_history(client, coord_dict, dateTime = None, hours = None, pageSize = None, period = None, pageToken = None, uaqiColorPalette=None, customLocalAqis=None, universalAqi=None, languageCode=None, EC_LOCAL_AQI = False,
                                 EC_HEALTH_RECOMMENDATIONS = False, EC_POLLUTANT_ADDITIONAL_INFO = False, EC_POLLUTANT_CONCENTRATION = False, EC_DOMINANT_POLLUTANT_CONCENTRATION = False):
    #See https://developers.google.com/maps/documentation/air-quality/reference/rest/v1/history/lookup#request-body for documentation.

    """coord_dict: object(latlng)
    and one of:
        -dateTime: string (Timestamp format) MUST BE WITHIN THE LAST 30 DAYS 
        -hours: int: retrive data from last n hours.
        -period: dict, {"startTime": string,"endTime": string}
    """
    

    base_url = "https://airquality.googleapis.com"
    url = "/v1/history:lookup"

    params_post_json = {}

    if isinstance(coord_dict, dict):
        params_post_json["location"] = coord_dict
    else:
        raise ValueError(
            "Location argument must be a dictionary containing latitude and longitude")
    

    if dateTime:
        params_post_json["dateTime"] = dateTime
    if hours:
        params_post_json["hours"] = hours
    if pageSize:
        params_post_json["pageSize"] = pageSize
    if pageToken:
        params_post_json["pageToken"] = pageToken
    if period:
        params_post_json["period"] = period
    



    if uaqiColorPalette:
        params_post_json["uaqiColorPalette"] = uaqiColorPalette

    if customLocalAqis:
        params_post_json["customLocalAqis"] = customLocalAqis

    if universalAqi:
        params_post_json["universalAqi"] = universalAqi
        
    if languageCode:
        params_post_json["languageCode"] = languageCode



    extra_computations = []

    if EC_LOCAL_AQI:
        extra_computations.append("LOCAL_AQI")

    if EC_HEALTH_RECOMMENDATIONS:
        extra_computations.append("HEALTH_RECOMMENDATIONS")

    if EC_POLLUTANT_ADDITIONAL_INFO:
        extra_computations.append("POLLUTANT_ADDITIONAL_INFO")

    if EC_POLLUTANT_CONCENTRATION:
        extra_computations.append("POLLUTANT_CONCENTRATION")

    if EC_DOMINANT_POLLUTANT_CONCENTRATION:
        extra_computations.append("DOMINANT_POLLUTANT_CONCENTRATION")


    params_post_json["extraComputations"] = extra_computations    

    return client._request(base_url = base_url, url = url, params = {}, post_json = params_post_json)
