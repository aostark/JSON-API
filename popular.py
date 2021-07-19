import json


def install_sort(package):
    return package["analytics"]["30d"]


with open("package_info.json", "r") as f:
    data = json.load(f)

# data = [item for item in data if "video" in item["desc"]]
# allows to filter and show only packages with 'video' in the description

data.sort(key=install_sort, reverse=True)

data_str = json.dumps(data, indent=2)
print(data_str)
