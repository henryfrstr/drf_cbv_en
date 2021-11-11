from django.urls import path, include
from .views import (home,
                    todoList,
                    todoListCreate,
                    toDo_list,
                    todoListUpdate,
                    todoListDelete,
                    toDo_detail,
                    TodoList,
                    TodoDetail,
                    TodoListCreate,
                    TodoRetreiveUpdateDelete,
                    TodoConcListCreate,
                    TodoConcRetreiveUpdateDelete,
                    TodoListRetreive,
                    TodoAll
                    )
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todovs', TodoListRetreive)
router.register('todomvs', TodoAll)

urlpatterns = [
    path('', home),
    # path('todoList/', todoList),
    # path('todoListCreate/', todoListCreate),
    # path('toDo_list/', toDo_list),
    # path('todoListUpdate/<int:pk>/', todoListUpdate),
    # path('todoListDelete/<int:pk>/', todoListDelete),
    # path('toDo_detail/<int:pk>/', toDo_detail),
    # path('todo/', TodoList.as_view()),
    # path('todo/<int:pk>', TodoDetail.as_view()),
    # path('todo/', TodoListCreate.as_view()),
    # path('todo/<int:pk>', TodoRetreiveUpdateDelete.as_view()),
    path('todo/', TodoConcListCreate.as_view()),
    path('todo/<int:pk>', TodoConcRetreiveUpdateDelete.as_view()),
    # path('', include(router.urls))

]

urlpatterns += router.urls
