import csv


class ImportCsv():


    def __init__(self,path) -> None:
        self.path = path
    
    def set(self):
        file = open(self.path)
        type(file)
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)
        
        return rows




        