from all import *

VOID_FUNC=lambda x, y:None

class Scene(object):
    '''A scene.

    Attributes:
    None.
    '''
    def __init__(self, updateFunc:typing.Callable=VOID_FUNC):
        self.handlers:typing.Dict[typing.Any,
            typing.Callable[[int, __init__.Game], typing.Any]
        ]={}
        self.update:typing.Callable=updateFunc
        pass
    def event(self, event, time_passed, game):
        self.handlers[event](time_passed, game)
        pass
