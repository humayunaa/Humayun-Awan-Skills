def filter_star(dict, num):
    dict2 = {}
    for k, v in dict.items():
        if len(v) == num:
            dict2[k] = v
    print(dict2)

filter_star({"Luxury Chocolates" : "*****",
             "Tasty Chocolates" : "****",
             "Big Chocolates" : "*****",
             "Generic Chocolates" : "***"},
             4)
