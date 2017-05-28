sportModule.controller('teamAllMatchesController', function ($scope, $http, $routeParams, $location) {

    var teamId = String($routeParams.teamId);

    $http.get("/api/teams/" + teamId + '/details/')
        .then(function (response) {
            $scope.details = response.data;
        });

    $http.get("/api/teams/" + teamId + '/rankedmatches/')
        .then(function (response) {
            $scope.teamId = teamId;
            $scope.teamRankedMatches = response.data;
        });

    $scope.sortType = 'match.match_date';
    $scope.sortReverse  = false;
    $scope.searchRankedMatches   = '';

});