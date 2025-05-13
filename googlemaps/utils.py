def download_map(request_iter, save_file):
    with open(save_file, "wb") as file:
        for chunk in request_iter:
            if chunk:  # Filter out keep-alive new chunks
                file.write(chunk)