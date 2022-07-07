from django import views
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

router.register('questions', views.QuestionViewset)
router.register('options', views.OptionViewset)

urlpatterns = router.urls
