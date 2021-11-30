"""This module contains business_trip function"""



def business_trip(graph, array):
    """
    business_trip calculates if trips between cities are possible and calculates their total cost.
    Arguments:
        graph: graph of available flights and their costs
        array: an array containing destinations
    Return: Str, the cost or None
    """
    price = 0
    cost=0
    if len(array) >=2:
        for city in range(len(array)):
            city_to_check=array[city]
            neighbors=graph.get_neighbors(city_to_check)

            if city+2 > len(array):
                return  f'${price}'
            cost=price

            for neighbor in neighbors:

                if neighbor.vertex == array[city+1]:
                    price+=neighbor.weight

            if price==cost:
                return None








