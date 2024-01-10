import requests
import json
from bs4 import BeautifulSoup

cookies = {
    '__cf_bm': 'NeGJP4WLOkFhROaTNeTvgokAE24jfbiXXHlGsNJo01U-1704853632-1-AcKoQvaC36NrGt14GchMveQQGBmDoYxiPp/Tsuz5swEJl7WZKcs4wRq0q4kV4UFXoymKqPBMTgoM8k81tajvsBOnFxYhFsD74Gu790uKC2+m',
    'PRIVATE-CSRF-TOKEN': '%2FZ70l%2Bdm8Nk7O7NrDe5Y7sNfAlFRlzNc6e0wpkvBQUY%3D',
}

headers = {
    'authority': 'www.artstation.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '__cf_bm=NeGJP4WLOkFhROaTNeTvgokAE24jfbiXXHlGsNJo01U-1704853632-1-AcKoQvaC36NrGt14GchMveQQGBmDoYxiPp/Tsuz5swEJl7WZKcs4wRq0q4kV4UFXoymKqPBMTgoM8k81tajvsBOnFxYhFsD74Gu790uKC2+m; PRIVATE-CSRF-TOKEN=%2FZ70l%2Bdm8Nk7O7NrDe5Y7sNfAlFRlzNc6e0wpkvBQUY%3D',
    'referer': 'https://www.artstation.com/?sort_by=community&dimension=all',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

# params = {
#         'page': 1,
#         'per_page': '30',
#     }

# response = requests.get(
#     'https://www.artstation.com/api/v2/neighborhoods/projects/community.json',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )

# result = response.json()

# with open('open.json', 'w') as file:
#     json.dump(result, file)



all_results = []  # Initialize an empty list to store results from all pages
last_id = 0  # Initialize the last ID

for page_number in range(1, 6):  # Assuming you want to collect data from pages 1 to 5
    params = {
        'page': str(page_number),
        'per_page': '30',
    }

    response = requests.get(
        'https://www.artstation.com/api/v2/neighborhoods/projects/community.json',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    result = response.json()

    filtered_result = [
        {
            "id": last_id + index + 1,
            "url": item['url'],
            "title": item['title'],
            "image": item['smaller_square_cover_url'],
            "author": {
                "username": item['user']['username'],
                "avatar": item['user']['medium_avatar_url'],
                "full_name": item['user']['full_name'],
            }
        }
        for index, item in enumerate(result['data'])
    ]

    all_results.extend(filtered_result)

    # Update the last ID for the next page
    last_id = all_results[-1]["id"]

# Save the combined results to a single JSON file
with open('combined_output.json', 'w') as file:
    json.dump(all_results, file, indent=2)
