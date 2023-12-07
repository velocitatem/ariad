import sys
sys.path.append("../")
from ariad import Ariad

proj = Ariad.register("demo_project")


def data_loader():
    # Simulate a more complex data loading process
    from faker import Faker
    fake = Faker()
    # fake completely random nested various depth json data
    def generate_data(depth=0):
        if depth == 0:
            return {"id": fake.uuid4(), "value": fake.pyfloat()}
        else:
            return {"id": fake.uuid4(), "value": generate_data(depth - 1)}
    data = [generate_data(3) for i in range(10)]


    return data

proj.register_module("data_loader", data_loader)

if __name__ == "__main__":
    l=data_loader()
    print(l)
