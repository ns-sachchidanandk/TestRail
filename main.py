import json
import pandas
from testrail import *

client = APIClient(base_url="https://netskope.testrail.io/")
client.user = "sachchidanandk@netskope.com" # Add your email
client.password = "****" # Add your password

PROJECT_ID = 34
SUITE_ID = 921

df = pandas.read_csv("datapath_inline.csv")

ids = []
data = {
    "case_ids": ids,
    "custom_ui_case": 1,
}

def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

for row in df.itertuples(index=True):
    if row.Suite == "SWG/N4W" and f"{row._14}".strip().lower() == "no":
        ids.append(int(row.ID.lstrip("C")))

# for index, lst in enumerate(split_list(ids, 10)):
for index in range(445, 714):
    # data["case_ids"] = lst

    with open(f"data_{index}.json", "r") as fp:
        data = json.load(fp)

    response = client.send_post(f"update_cases/{SUITE_ID}", data=data)

    with open(f"update_cases_{index}.json", "w") as fp:
        fp.write(json.dumps(response, indent=4))
