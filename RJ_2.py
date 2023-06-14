import json
count = 0
jacket = []
with open('catalog.json') as f:
    df = json.load(f)
for i in range(len(df)):
    if df[i]["name"] == "jacket":
        count += 1
        jacket.append(df[i]["price"])
print("個数",count)
print("最高価格",max(jacket))
print("最低価格",min(jacket))