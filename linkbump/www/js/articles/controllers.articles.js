angular.module('nyuad2015.controllers.articles', [])

.controller('ArticleListController', ['$scope', 'Article',
  function($scope, Article){

    $scope.articleList = [];
    Article.getList().then(
      function(s){
        if(s.status==200){
          $scope.articleList = s.data.results;
        }
      },function(e){console.log(e);});
}]);
