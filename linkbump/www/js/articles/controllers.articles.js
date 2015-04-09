angular.module('nyuad2015.controllers.articles', [])

.controller('ArticleListController', ['$scope', '$ionicModal', 'Article',
  function($scope, $ionicModal, Article){

    // load the articles
    $scope.articleList = [];
    Article.getList().then(
      function(s){
        if(s.status==200){
          $scope.articleList = s.data.results;
        }
      },function(e){console.log(e);});



    // set up the modal
    $ionicModal.fromTemplateUrl('js/articles/views/add_article_modal.tmpl.html', {
      scope: $scope,
      animation: 'slide-in-up'
    }).then(function(modal) {
      $scope.modal = modal;
    });
    $scope.openModal = function() {
      $scope.modal.show();
    };
    $scope.closeModal = function() {
      $scope.modal.hide();
    };
    //Cleanup the modal when we're done with it!
    $scope.$on('$destroy', function() {
      $scope.modal.remove();
    });
    // Execute action on hide modal
    $scope.$on('modal.hidden', function() {
      // Execute action
    });
    // Execute action on remove modal
    $scope.$on('modal.removed', function() {
      // Execute action
    });


    // listener for url form
    $scope.submitUrl = function(url){

      Article.parseUrl(url).then(function(s){
        if(s.status==200){
          // add the response to our array
          $scope.articleList.unshift(s.data);
          // close the modal
          $scope.closeModal();

        }


      },function(e){console.log(e);});

    };
}]);
