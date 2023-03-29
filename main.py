import requests
import pandas as pd
import json
from jsonpath_ng import jsonpath, parse
import os
apikey = os.getenv('apikey')
token=f"token {apikey}"

req = requests.get("https://demo.vectra.io/api/v2.3/detections",headers={"Authorization":f"{apikey}")
r=json.loads(req.content)

jsonpath_expression=parse('$..summary,detection_url,category,detection,src_host')
with open("Vectra_Detections.txt", "w") as file:

        for match in jsonpath_expression.find(r):
                print(match.value)
                filter=str(match.value)
                file.writelines(filter)
                if filter.startswith("{'id':"):
                        print("\n")
                        print("\n")
                        print("---")
                        file.writelines("\n")
                        file.writelines("\n")
                        file.writelines("---")
                        file.writelines("\n")
                        file.writelines("\n")










