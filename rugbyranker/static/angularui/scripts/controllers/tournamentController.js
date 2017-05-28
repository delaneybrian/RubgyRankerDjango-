sportModule.controller('tournamentController', function ($scope, $http, $routeParams, $location) {

    var tournamentId = String($routeParams.tournamentId);

    $http.get("/api/tournaments/" + tournamentId + "/")
        .then(function (response) {
            $scope.tournamentdata = response.data;
        }, function errorCallback(response) {
            $location.url('/error');
        });

    console.log("/api/tournaments/" + tournamentId + "/teams/");

    $http.get("/api/tournaments/" + tournamentId + "/matches/")
        .then(function (response) {
            $scope.tournamentmatchdata = response.data;
        });

    $http.get("/api/tournaments/" + tournamentId + "/teams/")
        .then(function (response) {
            $scope.tournamentteamdata = response.data;
        });

    $scope.teamtourlink = function (id) {
        console.log($location.path("teams/"  + id))
    }
});