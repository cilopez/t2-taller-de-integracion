from django.urls import path, include
from . import views 
from rest_framework_nested import routers
# from django.conf.urls import handler404


router = routers.SimpleRouter()
router.register('ingrediente', views.IngredientView)
router.register('hamburguesa', views.HamburgerView)
ingredients_router = routers.NestedSimpleRouter(router, 'hamburguesa', lookup='hamburguesa')
ingredients_router.register(r'ingrediente', views.IngredientViewSet, basename='hamburguesa-ingrediente')

# handler404 = views.error_page

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(ingredients_router.urls)),
]