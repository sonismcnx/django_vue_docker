from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer, RatingSerializer, UserSerializer
from .models import Movie, Rating

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class =  MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:

            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print('user', user)
            #user = User.objects.get(id=2)
            
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message' : 'Rating updated!', 'result' : serializer.data}
            except:
                try:
                    rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                    serializer = RatingSerializer(rating, many=False)
                    response = {'message' : 'Rating created!', 'result' : serializer.data}
                except:
                    response = {'message' : 'Token Error!'}

            return Response(response, status=status.HTTP_200_OK)
                
        else:
            response = {'message' : 'You need to provide stars'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message' : 'update not implemented yet!'}
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        response = {'message' : 'create not implemented yet!'}
        return Response(response, status=status.HTTP_200_OK)