import os
import json

from typing import List
from testrail import *


def parse_test_case_ids(file_path: str = "./data/uniq_test_case_ids.txt") -> List:
    test_case_ids: List
    with open(file_path, "r") as fp:
        test_case_ids = fp.readlines()

    return test_case_ids

def fetch_test_case_data(client: APIClient, test_case_id: int):
    response = client.send_get(f"get_case/{test_case_id}")
    return response

def create_test_case_update_data(test_case_data: dict):
    custom_stack_label = test_case_data.get("custom_stack_label", [])
    if 4 not in custom_stack_label:
        custom_stack_label.append(4)

    return {
        "custom_stack_label": custom_stack_label
    }

if __name__ == "__main__":
    client = APIClient(base_url="https://netskope.testrail.io/")
    client.user = "sachchidanandk@netskope.com"
    client.password = os.environ.get("TESTRAIL_PASSWORD")

    test_case_ids = parse_test_case_ids()
    for test_id in test_case_ids:
        test_id = int(test_id.strip())
        print(f"Updating test case with id: {test_id}")
        test_case_data = fetch_test_case_data(client, test_id)
        data = create_test_case_update_data(test_case_data)
        client.send_post(f"update_case/{test_id}", data=data)
        updated_test_case_data = fetch_test_case_data(client, test_id)
        with open(f"test_case_{test_id}.json", "w") as fp:
            fp.write(json.dumps(updated_test_case_data, indent=4))
