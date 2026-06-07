import json
import csv
from pathlib import Path

DATA_DIR = Path('data')

Data_file = DATA_DIR/'events.json'

class loadData:

    def getData(self):
        if Data_file.exists():
            with open(Data_file,'r') as f:
                content = f.read()
                if content.strip():
                    return json.loads(content)
                
        return []
    
    def loadData(self,data):
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        with open(Data_file,'w') as f:
            json.dump(data,f,indent=2)



obj = loadData()




           





