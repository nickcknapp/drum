
from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from .views import LinkList, LinkCreate, LinkDetail, CommentList


urlpatterns = patterns("mezzit.views",
    url("^$", LinkList.as_view(),
        name="home"),
    url("^newest/$", LinkList.as_view(), {"by_score": False},
        name="link_list_latest"),
    url("^comments/$", CommentList.as_view(), {"by_score": False},
        name="comment_list_latest"),
    url("^link/create/$", login_required(LinkCreate.as_view()),
        name="link_create"),
    url("^link/(?P<slug>.*)/$", LinkDetail.as_view(),
        name="link_detail"),
    url("^users/(?P<username>.*)/links/$", LinkList.as_view(),
        {"by_score": False},
        name="link_list_user"),
    url("^users/(?P<username>.*)/links/$", LinkList.as_view(),
        {"by_score": False},
        name="link_list_user"),
    url("^users/(?P<username>.*)/comments/$", CommentList.as_view(),
        {"by_score": False},
        name="comment_list_user"),
)
