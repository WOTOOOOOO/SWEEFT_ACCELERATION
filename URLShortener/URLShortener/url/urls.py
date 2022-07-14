from django.urls import path
from . import views
app_name = "url"
urlpatterns = [
    path("", views.urlShort, name="shorten"),
    path("a/", views.allUrls, name="all saved urls"),
    path("p/", views.premiumUrlShort, name="premium shorten"),
    path("d/", views.deleteUrl, name="dlete url"),
    path("data/", views.urlData, name="url counter"),
    path("u/<str:slugs>", views.urlRedirect, name="redirect")
]