def order_tuples_by_list(test_list, ord_list):
    return sorted(test_list, key=lambda x: ord_list.index(x[0]))

test_list = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]
ord_list = ['Geeks', 'best', 'CS', 'Gfg']
print(order_tuples_by_list(test_list, ord_list))