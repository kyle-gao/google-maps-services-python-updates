



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
        params_post_json["uaqiColorPalette"] = customLocalAqis

    if customLocalAqis:
        params_post_json["universalAqi"] = universalAqi
        
    if customLocalAqis:
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
        params_post_json["pageToken"] = pageSize
    if period:
        params_post_json["period"] = period
    



    if uaqiColorPalette:
        params_post_json["uaqiColorPalette"] = uaqiColorPalette

    if customLocalAqis:
        params_post_json["uaqiColorPalette"] = customLocalAqis

    if customLocalAqis:
        params_post_json["universalAqi"] = universalAqi
        
    if customLocalAqis:
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
