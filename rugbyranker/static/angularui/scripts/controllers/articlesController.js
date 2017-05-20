sportModule.controller('articlesController', function ($scope, $location, $http) {

    $http.get("/api/articles/")
        .then(function (response) {
            $scope.articles = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        }, function errorCallback(response) {
            console.log(response);
            $location.url('/error');
        });

    $scope.newpage = function(next){
        $http.get(next)
        .then(function (response) {
            $scope.articles = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });
    };

    $scope.clickarticle = function(articleid){
        console.log($location.path("articles/"  + articleid))
    };
});
