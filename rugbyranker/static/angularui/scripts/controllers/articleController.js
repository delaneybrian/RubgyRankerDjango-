sportModule.controller('articleController', function ($scope, $routeParams, $http) {

    var articleId = String($routeParams.articleId);

    $http.get("/api/articles/" + articleId + "/")
        .then(function (response) {
            $scope.article = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        }, function errorCallback(response) {
            console.log(response);
            $location.url('/error');
        });
});