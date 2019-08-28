import requests, settings
settings = settings.settings()
def VersionCheck():
    try:
        setting = requests.get("https://raw.githubusercontent.com/retart1337/AtanX/master/config.json").json()
        if setting["version"] != settings["version"]:
            for file in setting["updated-files"]:
                n = requests.get("https://raw.githubusercontent.com/retart1337/AtanX/master/%s" % file)
                with open(n, "w") as f:
                    f.write(n.content)
            print("Updates: Successfully updated repo.")
        print("Updates: No updates found.")
    except:
        print("Updates: Something went wrong. Continue starting..")
    finally:
        return