from django.core.urlresolvers import reverse
from django.views.generic import FormView
from shop.util.order import get_order_from_request
from django import forms
from shop.models import Order
from shop.views import ShopListView, ShopTemplateView
from .models import Category, Product, Manufacture
from django.views import generic

class WelcomeView(ShopTemplateView):
    template_name="shop/welcome.html"

    def get_context_data(self):
        context = {
            'products': Product.objects.all()[0:3],
            "lastest_products": Product.objects.all().order_by("-id")[0:4],
            "manufactures":Manufacture.objects.all(),
            }
        return context

welcome_view = WelcomeView.as_view()

class ProductListView(ShopListView):
    model = Product
    template_name = "shop/product_list.html"

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context.update({'categories':Category.objects.all()})
        return context 
products_view = ProductListView.as_view()


class CategoryView(generic.DetailView):
    model = Category
    template_name = "shop/product_list.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context.update({'object_list':self.object.products.active()})
        return context 
        
category_view = CategoryView.as_view()

class TermsOfServiceForm(forms.Form):
    agree = forms.BooleanField(required=True, initial=False, label='I agree to the Terms of Service')

class MyOrderConfirmView(FormView):
    template_name = 'myshop/order_confirm.html'
    form_class = TermsOfServiceForm

    def form_valid(self, form):
        self.confirm_order()
        return super(MyOrderConfirmView, self).form_valid(form)

    def confirm_order(self):
        order = get_order_from_request(self.request)
        order.status = Order.CONFIRMED
        order.save()

    def get_success_url(self):
        return reverse('checkout_payment')

    def get_context_data(self, **kwargs):
        ctx = super(MyOrderConfirmView, self).get_context_data(**kwargs)
        order = get_order_from_request(self.request)
        ctx.update({
            'order': order,
        })
        return ctx
