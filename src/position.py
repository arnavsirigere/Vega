class Position:
    def __init__(self, index, ln, col, file_name, file_text):
        self.index = index
        self.ln = ln
        self.col = col
        self.file_name = file_name
        self.file_text = file_text

    def advance(self, current_char):
        self.index += 1
        self.col += 1
        if current_char == "\n":
            self.ln += 1
            self.col = 0
        return self

    def copy(self):
        return Position(self.index, self.ln, self.col, self.file_name, self.file_text)