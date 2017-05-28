sportModule.controller('rankingsController', function ($scope, $http, $location) {

    $http.get("/api/rankings/")
        .then(function (response) {
            $scope.rankingdata = response.data;
        });

    $http.get("/api/rankings/highest/")
        .then(function (response) {
            $scope.highestlowest = response.data;
        });

    $scope.sortType     = 'position';
    $scope.sortReverse  = false;
    $scope.searchRanking   = '';

    $scope.clickrank = function(name){
        console.log($location.path("teams/"  + name))
    };


});