from django import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = DefaultRouter()

router.register('questions', views.QuestionViewset)
router.register('options', views.OptionViewset)
router.register('candidates', views.CandidateViewset)
router.register('respones', views.ResponseViewset)

urlpatterns = router.urls
