class ManageFiles:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('Get the resource')
        self.filename = open(self.filename, 'r', encoding='utf-8')
        return self.filename
    
    def __exit__(self, type_error, value_error, trace_error):
        print('Close the resourse')
        
        if self.filename:
            self.filename.close()
