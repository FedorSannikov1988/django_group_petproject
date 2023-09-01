from django.urls import reverse
from shop.forms import ShopFaqForm
from django.contrib.messages import error
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, \
                             HttpResponseRedirect
from django.contrib.postgres.search import SearchQuery, \
                                           SearchVector
from shop.models import ImageCollectionForIndex,\
                        FeaturesSoftware, \
                        SoftwareCategory, \
                        DevelopmentTeam, \
                        Software, \
                        Cart, \
                        FAQ

NUMBER_ITEM_PER_CATALOG_PAGE: int = 6


def title_for_basic_template() -> str:
    """
    :return:
    Returns the string 'Thesis'.
    This string is used in other functions
    to form page headers.
    """
    text: str = 'Пет-проект'
    return text


def data_for_basic_template(request) -> dict:
    """
    :param request:

    :return:

    """
    cart_user = None

    if not request.user.is_anonymous:
        cart_user = Cart.objects.filter(user=request.user)

    data = {
        "software_category": SoftwareCategory.objects.all(),
        "cart": cart_user
    }
    return data


def index(request):
    """
    The index function displays the main
    the web application page.

    :param request:
    request: a request object containing
    information about the user's request.

    :return:
    Rendering result
    HTML template "index.html".
    """
    title_index = 'Главная страница - '

    if ImageCollectionForIndex.objects.all().exists():
        all_image = \
            ImageCollectionForIndex.objects.all()
    else:
        all_image = None

    context = {
        "all_image": all_image,
        "page_title": title_index + title_for_basic_template()
    }
    return render(request, 'index.html',
                  {**context, **data_for_basic_template(request)})


def sitemap(request):
    title_sitemap = 'Карта сайта - '

    context = {
        'page_title': title_sitemap + title_for_basic_template()
    }
    return render(request, 'sitemap.html',
                  {**context, **data_for_basic_template(request)})


def about_us(request):
    title_about_us = 'О нас / Наши контакты - '

    context = {
        "page_title": title_about_us + title_for_basic_template(),
        "development_team": DevelopmentTeam.objects.all(),
    }
    return render(request, 'about_us.html',
                  {**context, **data_for_basic_template(request)})


def faq(request):
    """
    Displays a page with useful information and processes the form
    for the user to submit a question.

    :return: Redirect to the FAQ page if the question was successfully submitted.
    Otherwise, display the FAQ page with the form.
    """
    title_faq = 'Полезная информация - '
    if request.method == 'POST':
        form = ShopFaqForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                form_for_user = form.save(commit=False)
                form_for_user.user = request.user
                form_for_user.save()
                return HttpResponseRedirect(reverse('faq'))
            except:
                form.add_error(None, 'Ошибка отправки данных!')
    else:
        form = ShopFaqForm()

    context = {
        'form': form,
        'faq': FAQ.objects.all(),
        'page_title': title_faq + title_for_basic_template(),
    }
    return render(request, 'faq.html',
                  {**context, **data_for_basic_template(request)})


def product(request, software_id):
    title_product = 'Описание програмного обеспечения - '
    software = \
        Software.objects.get(id=software_id)
    software_description = \
        FeaturesSoftware.objects.get(id=software_id)
    category = \
        SoftwareCategory.objects.get(id=software.category_id)

    context = {
        'page_title': title_product + title_for_basic_template(),
        'software_id': software_id,
        'software_name': software.name,
        'software_image': software.image.url,
        'software_price': software.price,
        'software_quantity':software.quantity,
        'software_category_id':
            software.category_id,
        'software_category_name':
            category.name,
        'software_description':
            software_description.description,
        'software_description_min_ram_mb':
            software_description.min_ram_mb,
        'software_description_video_card':
            software_description.video_card,
        'software_description_hard_disk_mb':
            software_description.hard_disk_mb,
        'software_description_operating_system':
            software_description.operating_system,
    }
    return render(request, 'product.html',
                  {**context, **data_for_basic_template(request)})


def products_catalog(request, category_id=None,
                     page_number: int = 1):
    title_product_catalog = \
        'Каталог программного обеспечения - '

    start_number: int = 1
    stop_number: int = \
        NUMBER_ITEM_PER_CATALOG_PAGE

    if page_number != 1:
        start_number = \
            NUMBER_ITEM_PER_CATALOG_PAGE + 1
        stop_number = \
            NUMBER_ITEM_PER_CATALOG_PAGE * page_number

    if category_id:
        software = \
            Software.objects.filter(category_id=
                                    category_id)
    else:
        software = Software.objects.all()

    count_all_software: int = software.count()

    if count_all_software < stop_number:
        stop_number = count_all_software

    paginator = Paginator(object_list=software.order_by('id'),
                          per_page=NUMBER_ITEM_PER_CATALOG_PAGE)
    software_paginator = paginator.page(page_number)

    context = {
        "page_title": title_product_catalog + title_for_basic_template(),
        "categories": SoftwareCategory.objects.all(),
        "software": software_paginator,
        "count_all_software": count_all_software,
        "start_number": start_number,
        "stop_number": stop_number,
    }
    return render(request, 'catalog.html',
                  {**context, **data_for_basic_template(request)})


def search_product(request):
    title_search_product = \
        'Результаты поиска - '

    q = request.GET.get('q')
    if q:
        vector = SearchVector('name')
        query = SearchQuery(q)

        software = \
            Software.objects.annotate(search=vector).filter(search=query)
    else:
        software = \
            Software.objects.all()

    start_number: int = 0
    software_count: int = \
        software.count()

    if software_count != 0:
        start_number: int = \
            software_count - (software_count - 1)

    context = {
        "software": software,
        "start_number": start_number,
        "stop_number": software_count,
        "count_all_software": software_count,
        "page_title": title_search_product + title_for_basic_template(),
    }
    return render(request, 'catalog.html',
                  {**context, **data_for_basic_template(request)})


@login_required
def cart(request):
    title_cart = \
        'Большая корзина (для сравнения товаров) - '

    cart_user_small = \
        Cart.objects.filter(user=request.user)

    cart_user_big: list = []

    for one_purchase in \
            cart_user_small.order_by('id'):

        features_software = \
            FeaturesSoftware.objects.filter(id=one_purchase.software.id).first()

        new_line = {
                    'image': one_purchase.software.image,
                    'name': one_purchase.software.name,
                    'software_id': one_purchase.software.id,
                    'one_purchase_id': one_purchase.id,
                    'description': features_software.description,
                    'operating_system': features_software.operating_system,
                    'video_card': features_software.video_card,
                    'hard_disk_mb': features_software.hard_disk_mb,
                    'min_ram_mb': features_software.min_ram_mb,
                    'quantity_in_card': one_purchase.quantity,
                    'software_price': one_purchase.software.price,
                    'one_purchase_sum': one_purchase.sum
        }
        cart_user_big.append(new_line)

    context = {
        'cart': cart_user_small,
        'big_cart': cart_user_big,
        'big_cart_total_sum': cart_user_small.total_sum,
        'page_title': title_cart + title_for_basic_template(),
    }
    return render(request, 'cart.html',
                  {**context, **data_for_basic_template(request)})


@login_required
def cart_add_one(request, software_id):
    user = request.user
    software = \
        Software.objects.get(id=software_id)
    carts = \
        Cart.objects.filter(user=user,
                            software=software)

    if not carts.exists():
        Cart.objects.create(user=user,
                            software=software,
                            quantity=1)
    else:
        cart = carts.last()
        if software.quantity > cart.quantity:
            cart.quantity += 1
            cart.save()
        else:
            message_error_for_user = \
                'Больше данного тавара нет ' \
                'на складе.'
            error(request, message_error_for_user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def cart_delete_one(request, software_id):
    user = request.user
    software = Software.objects.get(id=software_id)
    carts = Cart.objects.filter(user=user, software=software)

    if carts.exists():
        cart = carts.last()

        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def cart_remove(request, cart_id):
    if Cart.objects.filter(id=cart_id).exists():
        Cart.objects.get(id=cart_id).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
