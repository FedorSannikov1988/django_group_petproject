from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from shop.models import SoftwareCategory, Software, DevelopmentTeam, FAQ, Cart
from shop.forms import NumberBuySoftwareLicense


def title_for_basic_template():
    text = 'Дипломный проект студентов GB'
    return text


def data_for_basic_template(request):
    cart_user = None

    if not request.user.is_anonymous:
        cart_user = Cart.objects.filter(user=request.user)

    data = {
        "software_category": SoftwareCategory.objects.all(),
        "cart": cart_user
    }
    return data


def all_soft():
    data = {
        "all_soft": Software.objects.all(),
        "software_operating_systems": Software.objects.filter(category__name='Операционные системы'),
        "software_office": Software.objects.filter(category__name='Офисное ПО'),
        "software_antivirus_protection": Software.objects.filter(category__name='Антивирусная защита')
    }
    return data


def index(request):
    title_index = 'Главная страница - '

    context = {
        "page_title": title_index + title_for_basic_template()
    }
    return render(request, 'index.html', {**context, **data_for_basic_template(request), **all_soft()})


def sitemap(request):
    title_sitemap = 'Карта сайта - '

    context = {
        'page_title': title_sitemap + title_for_basic_template()
    }
    return render(request, 'sitemap.html', {**context, **data_for_basic_template(request)})


def about_us(request):
    title_about_us = 'О нас / Наши контакты - '

    context = {
        "page_title": title_about_us + title_for_basic_template(),
        "development_team": DevelopmentTeam.objects.all(),
    }
    return render(request, 'about_us.html', {**context, **data_for_basic_template(request)})


def faq(request):
    title_faq = 'Полезная информация - '

    context = {
        'page_title': title_faq + title_for_basic_template(),
        'faq': FAQ.objects.all(),
    }
    return render(request, 'faq.html', {**context, **data_for_basic_template(request)})


def product(request):
    title_product = 'Описание програмного обеспечения - '

    context = {
        'page_title': title_product + title_for_basic_template(),
    }
    return render(request, 'product.html', {**context, **data_for_basic_template(request)})


def product_catalog(request):
    title_product_catalog = 'Главная страница - '

    context = {
        "page_title": title_product_catalog + title_for_basic_template(),
    }
    return render(request, 'product_catalog.html', {**context, **data_for_basic_template(request), **all_soft()})


@login_required
def cart(request):
    title_cart = 'Корзина покупателя - '

    if request.method == 'POST':
        form = NumberBuySoftwareLicense(data=request.POST)
        if form.is_valid():
            number_license = form.cleaned_data["quantity_license"]
            print(number_license)
            print(request.POST.get("software_id"))
    else:
        form1 = NumberBuySoftwareLicense(initial={'quantity_license': 1})

    context = {
        'form': form,
        'page_title': title_cart + title_for_basic_template(),
    }
    return render(request, 'cart_v2.html', {**context, **data_for_basic_template(request)})


@login_required
def cart_add_one(request, software_id):
    user = request.user
    software = Software.objects.get(id=software_id)
    carts = Cart.objects.filter(user=user, software=software)

    if not carts.exists():
        Cart.objects.create(user=user, software=software, quantity=1)
    else:
        cart = carts.last()
        if software.quantity > cart.quantity:
            cart.quantity += 1
            cart.save()

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
        # else:
        #    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def cart_remove(request, cart_id):
    Cart.objects.get(id=cart_id).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
