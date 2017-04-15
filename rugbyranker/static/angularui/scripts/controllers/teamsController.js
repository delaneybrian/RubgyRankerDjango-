sportModule.controller('teamsController', function ($scope, $http, $location) {

    $http.get("/api/teams/")
        .then(function (response) {
            $scope.teams = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $scope.newpage = function(next){
        $http.get(next)
        .then(function (response) {
            $scope.teams = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });
    };

    $scope.clickteam = function(teamid){
        console.log($location.path("teams/"  + teamid))
    };

});