import requests, settings
settings = settings.settings()
def VersionCheck():
    try:
        setting = requests.get("https://raw.githubusercontent.com/retart1337/AtanX/master/config.json").json()
        if setting["version"] > settings["version"]:
            updated_files = setting.get("updated-files").split(' ')
            for f in updated_files:
                n = requests.get("https://raw.githubusercontent.com/retart1337/AtanX/master/%s" % f).content.decode("utf-8")
                print("Updates: updating file %s" % f)
                with open(f, "w") as fw:
                    fw.write(n)
            print("Updates: files was succesfully updated")
        else:
            print("Updates: No updates found.")
    except:
        print("Updates: Something went wrong. Continue starting..")
    finally:
        return