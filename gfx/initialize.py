import cv2 as cv
from os import path
from tkinter import filedialog as fd
from .util.effectdictionary import effect_dictionary


class GFX:
    _PROMPT = 'Select an image file'
    _FILE_TYPES = (('JPG', '*.jpg'), ('PNG', '*.png'))
    _SRC = None
    _TEMP = None
    _DEST = None

    @property
    def source_image(self):
        return self._SRC

    @property
    def dest_image(self):
        return self._DEST

    def __init__(self):

        # load file

        file_name = fd.askopenfilename(title=self._PROMPT, filetypes=self._FILE_TYPES)
        print(f'Opening file: {file_name}')
        print(f'Size: {path.getsize(file_name)}')
        self._SRC = cv.imread(file_name, cv.IMREAD_COLOR)
        self._TEMP = self._SRC
        self._DEST = self._SRC

    def __str__(self):
        return f'GFX'

    def __del__(self):
        print('Done')

    @staticmethod
    def get_effect_request():
        return input('Enter effect (or x to exit): ').split('/')

    # Try and apply the effect
    def apply_effect(self, effect_name, **kwargs):
        try:
            self._DEST = effect_dictionary[effect_name](self._TEMP, **kwargs)
            print(f'{effect_name} applied')
            self._TEMP = self._DEST
        except KeyError:
            print(f'{effect_name} is not a valid effect name')

    def revert_to_last(self):
        self._DEST = self._TEMP

    def save_image(self):
        save_file_name = fd.asksaveasfilename(filetypes=self._FILE_TYPES)
        cv.imwrite(save_file_name, self._DEST)
        print(f'Saved image: {save_file_name}')
        print(f'Size: {path.getsize(save_file_name)}')

    def show_src_image(self):
        cv.imshow('Source Image', self._SRC)

    def show_dest_image(self):
        cv.imshow('Edited Image', self._DEST)

