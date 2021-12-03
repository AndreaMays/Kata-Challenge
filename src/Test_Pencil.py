import unittest
from CreatePencil import Pencil
from Paper import Paper

class TestPencil (unittest):
    def setUpTest (self):
        self.pencil = Pencil()
        self.paper = Paper()

    def test_needs_to_write_to_paper(self):
        text_to_write = "She sells sea shells"
        self.pencil.write(text_to_write, self.paper)

    def test_needs_to_append_text_to_the_end_of_the_string(self):
        self.paper.text = "She sells sea shells"
        text_to_write = "By the sea shore"


#given
#when
#then