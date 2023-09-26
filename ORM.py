import csv

class CSV_Saver:
    def __init__(self, filename, headings): 
        self.filename = filename
        self.headings = headings

    def create(self, data):
        with open (self.filename,'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headings)
            writer.writerow(data)

    def read(self):
        with open (self.filename,'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
        
    def update(self, search_key, search_value, new_data):
        rows = self.read()
        for row in rows:
            if row[search_key] == search_value:
                row.update(new_data)

        with open (self.filename, 'w', newline='') as file:
            writer =csv.DictWriter(file, fieldnames=self.headings)
            writer.writeheader()
            writer.writerows(rows)
    
    def delete(self, search_key, search_value):
        rows = self.read()
        updated_rows = [row for row in rows if row[search_key] != search_value]

        with open(self.filename,'w', newline='') as file
        writer = csv.DictWriter(file, fieldnames=self.headings)
        writer.writeheader
        writer.writerows(updated_rows)

        

