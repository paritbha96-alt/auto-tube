import requests
import os

def download_video_from_pexels(api_key, video_url, save_path):
    headers = {'Authorization': api_key}
    response = requests.get(video_url, headers=headers)

    if response.status_code == 200:
        with open(os.path.join(save_path, 'pexels_video.mp4'), 'wb') as f:
            f.write(response.content)
        print('Downloaded video from Pexels!')
    else:
        print('Error downloading from Pexels:', response.status_code)


def download_video_from_pixabay(api_key, video_id, save_path):
    video_url = f'https://pixabay.com/api/videos/{video_id}/?key={api_key}'
    response = requests.get(video_url)

    if response.status_code == 200:
        video_data = response.json()
        download_url = video_data['hits'][0]['videos']['large']['url']
        video_response = requests.get(download_url)

        if video_response.status_code == 200:
            with open(os.path.join(save_path, 'pixabay_video.mp4'), 'wb') as f:
                f.write(video_response.content)
            print('Downloaded video from Pixabay!')
        else:
            print('Error downloading video:', video_response.status_code)
    else:
        print('Error fetching video data from Pixabay:', response.status_code)


if __name__ == '__main__':
    pexels_api_key = 'YOUR_PEXELS_API_KEY'
    pixabay_api_key = 'YOUR_PIXABAY_API_KEY'
    save_directory = 'downloaded_videos'

    os.makedirs(save_directory, exist_ok=True)
    video_url = 'https://api.pexels.com/videos/videos_id'
    video_id = 'pixabay_video_id'

    download_video_from_pexels(pexels_api_key, video_url, save_directory)
    download_video_from_pixabay(pixabay_api_key, video_id, save_directory)