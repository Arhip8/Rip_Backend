from django.shortcuts import render

from .models import CONTAINERS, ORDERS, collect_cart, get_container_info, get_order_info, get_search_results


def index(request):
    containers = CONTAINERS
    search = request.GET.get("search")
    if search and search.strip():
        containers = get_search_results(search)
    template = "transport/index.html"
    title = "Контейнеры"
    if search:
        title = f"{title}. Результаты поиска: {search}"
    context = {
        "title": title,
        "containers": containers,
        "collected_cart": collect_cart(),
        "search_value": search if search else "",
    }
    return render(request, template, context)


def cart(request):
    template = "transport/cart.html"
    context = {
        "title": "Корзина",
    }
    return render(request, template, context)


def cont(request, id):
    template = "transport/cont.html"
    context = {
        "title": f"Контейнер {id}",
        "container_info": get_container_info(id),
    }
    return render(request, template, context)


def order(request, id):
    template = "transport/order.html"
    context = {
        "title": f"Заказ {id}",
        "order": get_order_info(id),
    }
    return render(request, template, context)


def add_product_to_cart(request, id):
    template = "transport/cart.html"
    context = {
        "title": "Корзина",
        "products": "Продукт 1",
    }
    return render(request, template, context)