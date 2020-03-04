from django.conf.urls import url

from . import view,testdb,search,search2
from django.contrib import admin

urlpatterns = [
    url(r'^hello$',         view.hello),
    url(r'^testAdd$',       testdb.testAdd),
    url(r'^testQuery$',     testdb.testQuery),
    url(r'^testModify$',    testdb.testModify),
    url(r'^testDel$',       testdb.testDel),
    url(r'^search-form$',   search.search_form),
    url(r'^search$',        search.search),
    url(r'^search-post$',   search2.search_post),
    url(r'^admin/',        admin.site.urls),
]
