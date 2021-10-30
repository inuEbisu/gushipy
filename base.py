from gushi import *
import json

def as_gushi(dct) -> Gushi:
    return Gushi(dct["title"], dct["author"], dct["context"], dct["code"])

def get_base() -> GushiList:
    basestr = "[]"
    try:
        with open("base.json", "r", encoding="utf-8") as b:
            basestr = b.read()
    except Exception as e:
        print(e)
    base = GushiList(json.loads(basestr, object_hook=as_gushi))
    return base