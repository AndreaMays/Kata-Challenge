class Pencil (object):
    def __init__(self, durable_point=50, length=4, durable_eraser=50):
        self.start_duarble_point= durable_point
        self.durable_point = durable_point
        self.durable_eraser = durable_eraser
        self.length = length

    def write(self, paper, write_string):
        for letter in write_string:
            if self.durable_point <= 0:
                paper.text += ''
                break
                
            paper.text += letter
            
            if letter == " " or letter == "/n":
                continue

            if letter.isupper():
                self.durable_point -= 2
            else:
                self.durable_point -= 1
    
    def sharpen(self):
        if self.durable_point <= 0:
            return

        self.durable_point = self.start_duarble_point
        self.length -= 1

    def erase(self, paper, string_to_erase):

        erased_text = " "
        for letter in erased_text:
            if self.durable_eraser <= 0 or letter.isspace():
                erase_text = letter + erased_text
                continue

            erased_text = " " + erased_text
            self.durable_eraser -= 1
    
    def edit(self):
        

        super().__init__()