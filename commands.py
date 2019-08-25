import importlib, os, utils, discord, difflib
events = {}
commands = {}
modules = {}
banned = ['__pycache__']

class ImportTools():
    def ImportFromPath(self):
        for pl in os.listdir("commands/"):
            if pl not in banned:
                path = pl.replace(".py", "")
                spec = importlib.util.spec_from_file_location(path, "commands/{}".format(pl))
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
        spec = importlib.util.spec_from_file_location(module, "commands/{}.py".format(module))
        foo = importlib.util.module_from_spec(spec)
        modules.update({module:foo})
        spec.loader.exec_module(foo)
class Event(object):
    def SetEvent(self, event, s, *args):
        if events.get(event) == None:
            events.update({event:{}})
        for d in events.get(event):
            for func, req in d.items():
                if req == "default":
                    func(*args)
                elif req == "self":
                    func(s, *args)
    def event(self, event, require="default", type="sync"):
        def func_wrap(func):
            if event not in events.keys():
                events.update({event:[{func:require}]})
            else:
                events.get(event).append({func:require})
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
                if typ == "sync":
                    result = func(args) if req == "default" else func(s, args)
                    utils.syncsender(command, msg, result)
                elif typ == "async":
                    utils.awaiter(func(args)) if req == "default" else utils.awaiter(func(s, args))
    else:
        SimillarList = difflib.get_close_matches(command, cmds)
        if len(SimillarList) >= 1:
            return SetCommand(SimillarList[0], args, s) 
    return
# Function to compare that all modules are descriped in packages.json at runtime
def compare():
    import settings
    settings = settings.settigns("packages.json")
    print(settings)
    for key in commands.keys():
        if key not in settings.keys():
            print(key)
class Locals:
    client = "client"
    message = "message"