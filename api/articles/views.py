from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer, ArticleParserSerializer
from .parsers import parse_article


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleParse(APIView):
    def post(self, request, format=None):
        serializer = ArticleParserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                article = Article.objects.get(url=serializer.data['url'])
            except Exception:
                parsed_article = parse_article(self.request.data['url'])
                article = Article.objects.create(url=parsed_article['url'],
                                                 domain=parsed_article['domain'],
                                                 title=parsed_article['title'],
                                                 excerpt=parsed_article['excerpt'],
                                                 image=parsed_article['lead_image_url'])

            response = {
              "id": article.pk,
              "url": article.url,
              "domain": article.domain,
              "title": article.title,
              "excerpt": article.excerpt,
              "image": article.image,
              "bumpCount": article.bumpCount
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ArticleBump(APIView):
    def post(self, request, pk, forma=None):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        article.bumpCount += 1
        article.save()

        return Response(status=status.HTTP_200_OK)
