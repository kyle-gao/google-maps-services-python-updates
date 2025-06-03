import requests
import numpy as np

def download_map(request_iter, save_file):
    with open(save_file, "wb") as file:
        for chunk in request_iter:
            if chunk:  # Filter out keep-alive new chunks
                file.write(chunk)

def fetch_geo_tiff(
    url: str,
    api_key: str,
    save_path: str = None
) -> bytes:
    """
    Retrieve GeoTIFF data from a Google Solar API endpoint and optionally save it.

    Args:
        url: Full endpoint URL including the id query parameter.
        api_key: Your Google API key.
        save_path: Local file path to save the GeoTIFF. If None, data is not saved.

    Returns:
        Raw GeoTIFF bytes on success.

    Raises:
        requests.HTTPError: If the request fails.
    """
    params = {'key': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.content

    if save_path:
        with open(save_path, 'wb') as f:
            f.write(data)

    return data                

def latlon_to_tile_coords(lat, lon, zoom):
    """
    Convert latitude and longitude to tile x, y coordinates using numpy.
    
    Args:
        lat (float or np.ndarray): Latitude in degrees.
        lon (float or np.ndarray): Longitude in degrees.
        zoom (int): Zoom level.

    Returns:
        tuple: (x_tile, y_tile) as integers or np.ndarrays of integers.
    """
    lat = np.asarray(lat, dtype=np.float64)
    lon = np.asarray(lon, dtype=np.float64)

    lat_rad = np.radians(lat)
    n = 2 ** zoom

    x_tile = np.floor((lon + 180.0) / 360.0 * n).astype(int)
    y_tile = np.floor(
        (1.0 - np.log(np.tan(lat_rad) + 1.0 / np.cos(lat_rad)) / np.pi) / 2.0 * n
    ).astype(int)

    return x_tile, y_tile