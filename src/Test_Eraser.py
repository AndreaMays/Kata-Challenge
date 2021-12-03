import unittest
from CreatePencil import Pencil
from Paper import Paper

class TestEraser (unittest):
    def setUpTestEraser (self):
        self.pencil = Pencil()
        self.paper = Paper()
    
    def test_should_delete_text_and_write_deleted_text_instead(self):
        self.paper.text = '123ABC'
        
#given
#when
#then

