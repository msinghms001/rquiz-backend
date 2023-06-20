from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


from apiv1.controller import LandingController

class CustPagination(PageNumberPagination):
    page_size=10
    page_query_param="next"

class Landing(ViewSet):

    @action(methods=['get'],detail=False,url_path='hello')
    def land(self,request):

        resp=LandingController.show_it()
        return Response({
            'error':{},
            'response':{
                'detail':{
                    'data':[]
                },
                'msg':'thanks to '+resp
            }
        })