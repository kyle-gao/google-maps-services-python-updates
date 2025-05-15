import requests
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