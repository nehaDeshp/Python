from django.conf.urls import url
from .views import talk_list , GetTalkWithID, InsertTalk, UpdateTalk, DeleteTalk

urlpatterns=[
    url(r'^talk',talk_list, name='talk_list'),
    url(r'^talkID',GetTalkWithID, name='talk_id'),
    url(r'^talkIns',InsertTalk, name='talk_ins'),
    url(r'^talkUp',UpdateTalk, name='talk_upd'),
    url(r'^talkDel',DeleteTalk, name='talk_del'),

]