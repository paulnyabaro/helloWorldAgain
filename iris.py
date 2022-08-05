with open('iris.csv', 'r') as iris_data:
    # iris_info = iris_data.read().split('\n')
    iris_info = iris_data.readline()

    # irises = []
    #
    # for row in iris_info[1:]:
    #     row.strip().split(",")
    #     irises.append(row)
    # print(irises)

    headers = iris_info[0].strip().split(",")
    irises = []

    for row in iris_info[1:]:
        iris = row.strip().split(",")
        iris_dict = dict(zip(headers, iris))

        irises.append(iris_dict)
    print(irises)
