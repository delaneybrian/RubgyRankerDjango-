sportModule.controller('tournamentsController', function ($scope, $http, $location) {

    $http.get("/api/tournaments/")
        .then(function (response) {
            $scope.tournaments = response.data;
        });

    $scope.tournamentlink = function(id){
        console.log($location.path("tournaments/"  + id))
    };
});