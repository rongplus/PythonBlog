import json

with open('orders.json') as f:
    data = json.load(f)

    for order in data:
        # for key in order.keys():
        #    print(key)
        # break
        print("=========================")
        print(order['partName'], order['imageUrl'], order['printerName'])
        if (order['productAdditionals'] is None):
            print("none")
        else:
            print(order['productAdditionals']
                  ['materialTypeName'], order['printTime'], order['productAdditionals']['materialTypeName'])
        # break
