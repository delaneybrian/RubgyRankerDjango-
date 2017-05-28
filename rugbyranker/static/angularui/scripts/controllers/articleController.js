sportModule.controller('articleController', function ($scope, $routeParams, $http) {

    var articleId = String($routeParams.articleId);

    $http.get("/api/articles/" + articleId + "/")
        .then(function (response) {
            $scope.article = response.data;
        }, function errorCallback(response) {
            $location.url('/error');
        });
});