sportModule.controller('articleController', function ($scope, $routeParams, $http, $sce) {

    var articleId = String($routeParams.articleId);

    $http.get("/api/articles/" + articleId + "/")
        .then(function (response) {
            $scope.article = response.data;
        }, function errorCallback(response) {
            $location.url('/error');
        });

    $scope.SkipValidation = function(value) {
        return $sce.trustAsHtml(value);
};
});