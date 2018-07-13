class marks:
    def __init__(self, a, b):
        self.english = a
        self.hindi = b
        
    def get_marks(self):
        markslist = [self.hindi, self.english]
        return markslist
    
    def set_marks(self, values):
        if values[0] < 0 or values[1] < 0:
            print("Marks must be a positive number")
        else:
            self.hindi = values[0]
            self.english = values[1]
        return
    
    score = property(get_marks, set_marks)
