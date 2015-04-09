angular.module('nyuad2015.services.articles', [])

.constant('DOMAIN', 'http://localhost:8000')

.factory('Article', ['$http', 'DOMAIN', function($http, DOMAIN){
  
  var getList = function(){
    var response = $http({
            url: DOMAIN + '/api/v1/article/',
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
            data: ''
        });
    return response;
  };

  return{
    getList: getList
  };
}])