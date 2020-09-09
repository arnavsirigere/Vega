class Error:
    def __init__(self, pos_start, pos_end, name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.name = name
        self.details = details

    # TODO: Better __str__ result,  string_with_arrows, formatting (EP2)
    def __str__(self):
        return f"{self.name} : {self.details}, File: {self.pos_start.file_name}, Line: {self.pos_start.ln + 1}, Col: {self.pos_start.col + 1}"


class IllegalCharErr(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)


class InvalidSyntaxErr(Error):
    def __init__(self, pos_start, pos_end, details=''):
        super().__init__(pos_start, pos_end, 'Invalid Syntax', details)
