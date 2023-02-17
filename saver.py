import typing
import pickle

class GameData(object):
    """Game Data

    Place the game data into this class like GameDataInst.data=...
    """
    def save(self, file:str):
        """Save datato a file.

        Args:
        file: The file which is we want to save.
        """
        with open(file, 'wb') as f:
            pickle.dump(self, f)
            pass
        pass
    def read(self, file:str):
        """Read data from a file.

        Args:
        file: The file which is we want to read from.
        """

