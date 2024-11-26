CONTAINERS = [
    {
        "id": 1,
        "name": "Контейнер 1",
        "description": "Описание контейнера 1",
        "image": "1.jpeg",
        "price": 10_000,
    },
    {
        "id": 2,
        "name": "Контейнер 2",
        "description": "Описание контейнера 2",
        "image": "2.jpeg",
        "price": 20_000,
    },
    {
        "id": 3,
        "name": "Контейнер 3",
        "description": "Описание контейнера 3",
        "image": "3.jpeg",
        "price": 25_000,
    },
]

ORDERS = {
    1: {
        "containers": [1, 3],
        "transport": "Поезд",
    },
    2: {
        "containers": [2],
        "transport": "Самолёт",
    },
}


def collect_cart():
    collected_orders = {}
    for order_id, order in ORDERS.items():
        containers = []
        total_price = 0
        for container in CONTAINERS:
            if container["id"] in order["containers"]:
                containers.append(container)
                total_price += container["price"]
        collected_orders[order_id] = {
            "containers": containers,
            "transport": order["transport"],
            "total_price": total_price,
            "count": len(containers),
        }
    return collected_orders


def get_container_info(id):
    for container in CONTAINERS:
        if container["id"] == id:
            return container


def get_order_info(id):
    return collect_cart()[id]


def get_search_results(search_string):
    search_result = []
    search_string = search_string.lower().strip()
    for container in CONTAINERS:
        if any([
            search_string in container["name"].lower(), 
            search_string in container["description"].lower(), 
            search_string in str(container["price"]), 
        ]):
            search_result.append(container)
    return search_result
