# This moves the arm directly above the head (for calibrating height).
# https://github.com/byronknoll/robot-barber

import requests
import argparse
import time
import json

commands = [
['{"T":122,"b":0,"s":-1,"e":2.35,"h":1.1,"spd":10,"acc":10}',2],
]

def main():
    parser = argparse.ArgumentParser(description='Http JSON Communication')
    parser.add_argument('ip', type=str, help='IP address: 192.168.10.104')

    args = parser.parse_args()

    ip_addr = args.ip

    try:
        for command in commands:
            data = json.loads(command[0])
            if ("b" in data):
            	data["b"] *= 57.2958
            	data["s"] *= 57.2958
            	data["e"] *= 57.2958
            	data["h"] *= 57.2958
            command[0] = json.dumps(data)
            print(command[0])
            url = "http://" + ip_addr + "/js?json=" + command[0]
            response = requests.get(url)
            content = response.text
            print(content)
            time.sleep(command[1])
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
