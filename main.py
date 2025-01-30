import json
import pandas

from testrail import *

client = APIClient(base_url="https://netskope.testrail.io/")
client.user = "sachchidanandk@netskope.com" # your testrail email address goes here
client.password = "2Ur!$%B7A$@8GivK&" # your testrail password goes here

PROJECT_ID = 34
SUITE_ID = 921

df = pandas.read_csv("datapath_inline.csv")

ids = []
data = {
    "case_ids": ids,
    "custom_ui_case": 1,
}

breakpoint()
response = client.send_get("get_case/1498430")
print(json.dump(response, indent=4))

# def split_list(lst, chunk_size):
#     return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
#
# for row in df.itertuples(index=True):
#     if row.Suite == "SWG/N4W" and f"{row._14}".strip().lower() == "no":
#         ids.append(int(row.ID.lstrip("C")))
#
# for index, lst in enumerate(split_list(ids, 10)):
#     if index < 445:
#         continue
#
#     data["case_ids"] = lst
#
#     response = client.send_post(f"update_cases/{SUITE_ID}", data=data)
#
#     with open(f"data_{index}.json", "w") as fp:
#         fp.write(json.dumps(data, indent=4))
#
#     with open(f"update_cases_{index}.json", "w") as fp:
#         fp.write(json.dumps(response, indent=4))
