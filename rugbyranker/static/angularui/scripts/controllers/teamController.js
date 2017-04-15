sportModule.controller('teamController', function ($scope, $http, $routeParams) {

    var teamId = String($routeParams.teamId);


    $http.get(host + "api/teams/" + teamId + '/details/')
        .then(function (response) {
            $scope.details = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get(host + "api/teams/" + teamId + '/matches/home/')
        .then(function (response) {
            $scope.homematchdata = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get(host + "api/teams/" + teamId + '/matches/away/')
        .then(function (response) {
            $scope.awaymatchdata = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get(host + "api/teams/" + teamId + '/information/')
        .then(function (response) {
            $scope.information = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/teams/" + teamId + '/rivals/')
        .then(function (response) {
            $scope.rivals = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/teams/" + teamId + '/history/')
        .then(function (response) {
            $scope.history = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/teams/" + teamId + '/currentranking/')
        .then(function (response) {
            $scope.currentranking = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $scope.sortType     = 'position';
    $scope.sortReverse  = false;
    $scope.searchRivals   = '';



});