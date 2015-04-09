angular.module('nyuad2015.controllers.articles', [])

.controller('ArticleListController', ['$scope', 'Article',
  function($scope, Article){

    Article.getList().then(function(s){console.log(s);}, function(e){console.log(e);});
}]);
