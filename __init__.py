"""A game library with pygame.
"""

from all import *

def init():
    """Init the library.

    Must call it to init the game first.
    """
    pygame.init()

class Game(object):
    """Game object.

    Must create this object ONCE when game init.
    Attributes:
    title: The title of the game(define by @property)
    windowsize: The size of the window of the game (define by @property)
    window: The pygame surface of the window of the game (define by @poperty) (READONLY ARGUMENT)
    windowflags: The flags of the window of the game. (define by @property)
    """
    def __init__(self, title:str='Untitled game',
            windowsize:typing.List[int, int]=[800, 608], windowflags:int=0,
            startwith:extend_types.NoneType | ):
        """Init the game.

        Args:
        title: The title of the game.
        windowsize: A list like [x,y] to identify game window's size.
        """
        self.__title=title
        self.__windowsize=windowsize
        self.__windowflags=windowflags
        
        self.__init_display()
        pygame.display.set_caption(title)
        self.now=startwith
        self.pressed=set()
        self.key_mod=0
        pass
    def __init_display(self):
        self.__window=pygame.display.set_mode(self.windowsize, self.windowflags, 32)
        pass
    @property
    def windowsize(self):
        return self.__windowsize
    @windowsize.setter
    def windowsize_setter(self, newsize):
        self.__windowsize=newsize
        self.__init_display()
        pass
    @property
    def title(self):
        return self.__title
    @title.setter
    def title_setter(self, newtitle):
        pygame.display.set_caption(newtitle)
        self.__title=newtitle
        pass
    @property
    def window(self):
        return self.__window
    @property
    def windowflags(self):
        return self.__windowflags
    @windowflags.setter
    def windowflags_setter(self, newflags):
        self.__windowflags=newflag
        self.__init_display
        pass
    
    def run(self:Game):
        while self.now is not None:
            for i in pygame.event.get():
                match i.type:
                    case KEYDOWN:
                        self.pressed.add(i.key)
                        pass
                    case KEYUP:
                        self.pressed.remove(i.key)
                        pass
                if i.type in [KEYDOWN, KEYUP]:
                    self.key_mod=i.type
                    pass

                self.now.event(i, self)
                pass

            self.now.update(self)
            pass
