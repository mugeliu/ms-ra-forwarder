import requests


def download_mp3(url: str, data: dict, output_file: str):
    """
    发送 POST 请求到指定的 URL，接收 MP3 格式的音频文件，并将其写入到本地文件中。

    :param url: 请求的 URL
    :param data: POST 请求的数据
    :param output_file: 保存 MP3 文件的本地路径
    """
    cookies = {
        '_ga': 'GA1.1.1155505015.1713263457',
        '_hjSessionUser_2531461': 'eyJpZCI6ImJmZGU5MzVlLTIwZmItNTY3OC05MWEyLWQ2N2M0NjczZWVlZSIsImNyZWF0ZWQiOjE3MTQ2MTY4MTEwMzQsImV4aXN0aW5nIjp0cnVlfQ==',
        '_clck': '8kxi9d%7C2%7Cflq%7C0%7C1583',
        '_ga_39WSEGK1FQ': 'GS1.1.1716772407.22.1.1716774132.0.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'authorization': 'Bearer lin0897@',
        'cache-control': 'no-cache',
        'content-type': 'text/plain',
        # 'cookie': '_ga=GA1.1.1155505015.1713263457; _hjSessionUser_2531461=eyJpZCI6ImJmZGU5MzVlLTIwZmItNTY3OC05MWEyLWQ2N2M0NjczZWVlZSIsImNyZWF0ZWQiOjE3MTQ2MTY4MTEwMzQsImV4aXN0aW5nIjp0cnVlfQ==; _clck=8kxi9d%7C2%7Cflq%7C0%7C1583; _ga_39WSEGK1FQ=GS1.1.1716772407.22.1.1716774132.0.0.0',
        'dnt': '1',
        'format': 'audio-24khz-48kbitrate-mono-mp3',
        'origin': 'https://tts.pushforward.fun',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://tts.pushforward.fun/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    try:
        response = requests.post(url, headers=headers, cookies=cookies,  data=data)
        response.raise_for_status()  # 检查请求是否成功

        # 假设响应内容是 MP3 文件的字节流
        with open(output_file, 'wb') as file:
            file.write(response.content)
        
        print(f"MP3 文件已成功保存到 {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")


url = 'https://tts.pushforward.fun/api/ra'
data = '        <speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">          <voice name="zh-CN-XiaoxiaoNeural">              <prosody rate="0%" pitch="0%">                  如果喜欢这个项目的话请点个 Star 吧。              </prosody >          </voice >        </speak > '.encode()

download_mp3(url=url, data=data, output_file='output.mp3')