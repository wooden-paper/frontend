import sys
import json
import requests


def get_data(url: str, from_date: str, to_date: str):
    return requests.get(f"{url}/api/validate?from={from_date}&to={to_date}").json()


def main():

    args = sys.argv
    if args[1] == "download_all_valid":
        if len(args) == 2:
            print("Download URL required")
            exit(-1)
        try:
            req = get_data(args[2], "0001-01-01", "9999-12-31")
        except:
            print("Invalid download URL")
            exit(-1)
        valid = [x for x in req if x["valid"]]
        print(f"Downloading {len(valid)} files...")
        for file in valid:
            with open(file["name"], "wb") as f:
                f.write(requests.get(args[2] + "/api/get/" + file["name"]).content)
        print("Completed downloading")
        exit(0)

    if args[1] == "download_all":
        if len(args) == 2:
            print("Download URL required")
            exit(-1)
        try:
            req = get_data(args[2], "0001-01-01", "9999-12-31")
        except:
            print("Invalid download URL")
            exit(-1)
        print(f"Downloading {len(req)} files...")
        for file in req:
            with open(file["name"], "wb") as f:
                f.write(requests.get(args[2] + "/api/get/" + file["name"]).content)
        print("Completed downloading")
        exit(0)

    if args[1] == "download_all_invalid":
        if len(args) == 2:
            print("Download URL required")
            exit(-1)
        try:
            req = get_data(args[2], "0001-01-01", "9999-12-31")
        except:
            print("Invalid download URL")
            exit(-1)
        valid = [x for x in req if not x["valid"]]
        print(f"Downloading {len(valid)} files...")
        for file in valid:
            with open(file["name"], "wb") as f:
                f.write(requests.get(args[2] + "/api/get/" + file["name"]).content)
        print("Completed downloading")
        exit(0)

    if args[1] == "download_logs":
        if len(args) == 2:
            print("Download URL required")
            exit(-1)
        try:
            with open("logs.txt", "wb") as f:
                f.write(requests.get(args[2] + "/api/get/logs").content)
        except:
            print("Invalid download URL")
            exit(-1)
        print("Completed downloading")
        exit(0)


if __name__ == "__main__":
    main()
