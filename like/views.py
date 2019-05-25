from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializer import PostLikeSerializer
from .models import Like
from rest_framework import status


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        like = Like.objects.latest('create_date')
        like.user_that_likes.liked_tutoring_sessions.add(like)
        like.tutoring_session.likes.add(like)
        like.tutoring_session.total_likes += 1
        like.tutoring_session.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) 