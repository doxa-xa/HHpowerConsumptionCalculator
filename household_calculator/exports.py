import csv
import json
from os import path

#used for saving data in various formats
class Save:

    #writes room or household data to csv file

    @staticmethod
    def to_csv(data,file_name,operation = 'w'):
        filename = path.join(path.abspath('files'),file_name)  
        with open(filename,operation,newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_ALL)
            for item in data:
                writer.writerow(item.values())
        print(f'"{filename}" csv file has been saved')

    @staticmethod
    def to_txt(data,file_name):
        pass

    # writes data to json file
    @staticmethod
    def to_json(data,file_name,operation='w'):
        filename = path.join(path.abspath('files'),file_name) 
        with open(filename,operation) as f:
            f.write(json.dumps(data))
        print(f'{file_name} file has benn saved')