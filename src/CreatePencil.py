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
            
        super().__init__()