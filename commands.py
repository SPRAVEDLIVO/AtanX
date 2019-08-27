import importlib, os, utils, discord, difflib
events = {}
commands = {}
modules = {}
banned = ['__pycache__']

class ImportTools():
    def __init__(self, path="commands/"):
        self.path = path
    def ImportFromPath(self):
        for pl in os.listdir(self.path):
            if pl not in banned:
                path = pl.replace(".py", "")
                spec = importlib.util.spec_from_file_location(path, "{}{}".format(self.path, pl))
                foo = importlib.util.module_from_spec(spec)
                modules.update({path:foo})
                spec.loader.exec_module(foo)
    def dynamic_reload(self, module):
        for k, v in modules.items():
            if k == module:
                modules.update({k:importlib.reload(v)})
    def reload_all(self, ):
        for k, v in modules.items():
            modules.update({k:importlib.reload(v)})
    def dynamic_import(self, module):
        spec = importlib.util.spec_from_file_location(module, "{}{}.py".format(self.path, module))
        foo = importlib.util.module_from_spec(spec)
        modules.update({module:foo})
        spec.loader.exec_module(foo)
class Event(object):
    def SetEvent(self, event, s, *args):
        if events.get(event) == None:
            return
        for d in events.get(event):
            for func, types in d.items():
                req = types["require"]
                typeof = types["type"]
                if typeof == "sync":
                    if req == "default":
                        func(*args)
                    elif req == "self":
                        func(s, *args)
                elif typeof == "async":
                    if req == "default":
                        utils.awaiter(func(*args))
                    elif req == "self":
                        utils.awaiter(func(s, *args))
    def event(self, event, require="default", type="sync"):
        def func_wrap(func):
            if event not in events.keys():
                events.update({event:[{func:{"require":require, "type":type}}]})
            else:
                events.get(event).append({func:{"require":require, "type":type}})
        return func_wrap
class Command(object):
    def event(self, command, require="default", type="sync", aliases=[]):
        def func_wrap(func):
            if command not in commands.keys():
                commands.update({command:[{func:{"require":require, "type":type}}]})
                for alias in aliases:
                    commands.update({alias:[{func:{"require":require, "type":type}}]})
            else:
                commands.get(command).append({func:{"require":require, "type":type}})
        return func_wrap
def SetCommand(command, args, s):
    cmds = commands.keys()
    if command in cmds:
        msg = s[Locals.message]
        for d in commands.get(command):
            for func, types in d.items():
                typ = types["type"]
                req = types["require"]
                # Check if LS flag in message
                if args != None and args[-1] == "!ls":
                    del args[-1]
                    ls_flag = True
                    # Then set args to None back
                    if len(args) == 0:
                        args = None
                else:
                    ls_flag = False
                if typ == "sync":
                    if req == "dafault":
                        result = func(args)
                    elif req == "self":
                        result = func(s, args)
                    elif req == "message":
                        result = func(s["message"], args)
                    elif req == "client":
                        result = func(s["client"], args)
                    else:
                        result = func(args)
                    utils.syncsender(command, msg, result, ls_flag=ls_flag)
                elif typ == "async":
                    if req == "dafault":
                        utils.awaiter(func(args))
                    elif req == "self":
                        utils.awaiter(func(s, args))
                    elif req == "messgae":
                        utils.awaiter(func(s["message"], args))
                    elif req == "client":
                        utils.awaiter(func(s["client"], args))
                    utils.awaiter(func(args)) if req == "default" else utils.awaiter(func(s, args))
    else:
        SimillarList = difflib.get_close_matches(command, cmds)
        if len(SimillarList) >= 1:
            return SetCommand(SimillarList[0], args, s) 
    return
# Function to compare that all modules are descriped in packages.json at runtime
def compare():
    import settings
    settings = settings.settings("packages.json")
    print(settings)
    for key in commands.keys():
        if key not in settings.keys():
            print(key)
class Locals:
    client = "client"
    message = "message"