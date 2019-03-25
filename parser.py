import json

def number_item():
    with open('sales_with_goods.csv') as file:
        data = {}
        for line in file.readlines()[1:]:
            line = line.split(',')
            document_number = line[8][1:-1]
            product_id = line[4][1:-1]
            if not document_number in data:
                data[document_number] = []
            data[document_number].append(product_id)
    data = json.dumps(data)
    with open('number-item.txt', 'w') as file:
        file.write(data)

def user_number_item():
    data = {}
    with open('sales_with_goods.csv') as file:
        for line in file.readlines()[1:]:
            line = line.split(',')
            customer_item = line[1][1:-1]
            document_number = line[8][1:-1]
            product_id = line[4][1:-1]
            if not customer_item in data:
                data[customer_item] = {}
            if not document_number in data[customer_item] :
                data[customer_item][document_number] = []
            data[customer_item][document_number].append(product_id)
    # for value in data.values():
    #     if len(value) > 1:
    #         print(True)
    with open('user-number-item.txt', 'w') as file:
        data = json.dumps(data)
        file.write(data)

if __name__=='__main__':
    number_item()
    user_number_item()
