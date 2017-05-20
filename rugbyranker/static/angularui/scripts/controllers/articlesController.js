sportModule.controller('articlesController', function ($scope, $http) {

    $http.get("/api/articles/")
        .then(function (response) {
            $scope.articles = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        }, function errorCallback(response) {
            console.log(response);
            $location.url('/error');
        });
});
