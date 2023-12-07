import sys
sys.path.append("../")
# data_processor.py
from ariad import Ariad

proj = Ariad.register("demo_project")

def data_processor(data):
    # More complex data processing
    # take all json data, any float should be an int
    def process_data(item):
        if isinstance(item, dict):
            for k, v in item.items():
                item[k] = process_data(v)
            return item
        elif isinstance(item, float):
            return int(item)
        else:
            return item
    processed_data = [process_data(item) for item in data]
    return processed_data
proj.register_module("data_processor", data_processor)

if __name__ == "__main__":
    testing = [{'id': '2dc6dbb2-0439-496b-b26e-5ed4e705d94b', 'value': {'id': 'e2e814c5-78ce-44c0-8efb-d84f8fceeed3', 'value': {'id': '628d3227-f126-494f-b565-6ab0a869a0de', 'value': {'id': '6a0608ad-c562-41e2-badb-efb0e79d5b93', 'value': 3377831795.99}}}}, {'id': '406c0817-a086-47eb-8596-d94e565f272b', 'value': {'id': '373e8748-043d-4a59-955f-77feec003279', 'value': {'id': '48f8de84-d027-4199-87f0-a3de1db62b30', 'value': {'id': 'c49a3fdd-49e3-4e7e-bca8-fffa1b4b5ec7', 'value': 590474.105642784}}}}, {'id': '456490d5-42cf-45cd-9be6-f477e1c5d9b9', 'value': {'id': '7032a01e-9852-4fe1-b0fd-f19bc5302815', 'value': {'id': 'a03019b5-d78e-4927-946f-6ab7bd6715ae', 'value': {'id': '5bfdbfe2-28a2-4fa8-babc-d9e055b91db6', 'value': -392.28770320374}}}}, {'id': 'b431039a-63ac-4ddb-aac3-fc014709e9a7', 'value': {'id': 'b202eda0-c0e0-4880-b7ad-96001713910a', 'value': {'id': '803edece-4445-4f68-ab8f-a7918701bb0d', 'value': {'id': 'e8c6d8f1-4b02-4528-9ee7-1f82b2c452b4', 'value': -2469182776.40128}}}}, {'id': '35898136-6f18-4538-83e4-27025effe726', 'value': {'id': 'f105be21-f2ed-40b6-9db8-e586db789e83', 'value': {'id': '8e4c30f3-4338-479f-ae96-1698fa4f38f9', 'value': {'id': '08cb4210-a19d-4cfc-b42a-a14c0397a4d1', 'value': 967895.481942205}}}}, {'id': 'aef0829a-7762-4aa6-bfbf-57a762fc0e10', 'value': {'id': '361b699f-7840-4a71-ae1d-7bd53928e985', 'value': {'id': 'e4ec0080-253b-40b7-ba2e-95833e682d16', 'value': {'id': '2e4232a7-30c0-45a9-9205-c14154ab963a', 'value': 628482178.993104}}}}, {'id': '188b48e3-9caf-4e03-849d-d490673362b3', 'value': {'id': '696d64d3-e57e-4142-8efe-d1ef1d16b7c5', 'value': {'id': 'c085b170-3c80-495a-b8ef-8b27acf1710b', 'value': {'id': '5ed38ea0-6fcd-431c-b9b1-3e7afadcf6d9', 'value': 655338.898153419}}}}, {'id': '8d0fceae-a831-4328-abd7-723cc4c98624', 'value': {'id': '5a297e55-224c-46cb-b7f9-eb96a8685500', 'value': {'id': '260598e0-f548-4d95-89ce-49679dd09d6d', 'value': {'id': '1356758b-1929-4959-98e0-16785ab1bd6e', 'value': 722174164.630474}}}}, {'id': 'e426dea5-8b46-44cc-8c9d-af880b915012', 'value': {'id': '0a3729ea-1d96-477a-8865-7e68f5f95a24', 'value': {'id': 'e6155cf4-0566-40e7-b8f3-f6102de4f6e2', 'value': {'id': 'f0cb8ad0-0225-468a-b85c-995338e05f04', 'value': 703850.245399434}}}}, {'id': 'bb4cd9ce-6fe1-41b1-ab17-a01f7591f2db', 'value': {'id': 'bc6ca376-5f19-4bf6-a3c6-95bed9894ff1', 'value': {'id': '6a6873a4-22e8-45cf-8fe0-e4620cd69463', 'value': {'id': 'cd40b81b-9b38-46ea-9336-704776468519', 'value': -61604967619148.1}}}}]
    r=data_processor(testing)
    print(r)