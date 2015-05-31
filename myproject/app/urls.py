from django.conf.urls import include, url
from django.contrib import admin
from app.home import views as home
#from  import cached_javascript_catalog
from django.views.i18n import javascript_catalog
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import activate


js_info_dict = {
    'domain': 'django',
    'packages': ('myproject',),
}

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^i18n/', include('django.conf.urls.i18n')),
    
    url(r'^admin/', include(admin.site.urls)),
]


urlpatterns += i18n_patterns(
    url(r'^$', home.index ,name="home"),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict),
    url(r'^about/$', home.about, name='about'),
)
