import json

with open('result.json') as f:
    data = json.load(f)

    for key in data.keys():
        print(key)

    inn = 0
    for a in data['products']:
        for key in a.keys():
            if inn == 0:
                print("key=", key)

        print("    categoryIds:", a['productParts'])
        for cc in a['productParts']:
            print(cc)
        #      a['name'], "    productOwnEmail :", a['productOwnEmail'], "    image url:", a['image']['imageUrl'])
        # print (a['productParts'])
        # print (inn, "index == top == ",a['name'],  " *=* ",a['displayName'])
        print("len = ", len(a['productParts']))
        for o in a['productParts']:
            for key in o.keys():
                if inn == 0:
                    print("sub key=", key)
            #print("    categoryIds:", o['categoryIds'])
        #    print("    --->displayname:", o)
        inn = inn+1
        print("product id", a['id'])
        print(inn, "==*********=========================********=================")
        # break
