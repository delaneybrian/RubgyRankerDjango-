sportModule.controller('countriesController', function ($scope, $http) {

    $http.get("/api/country/")
            .then(function (response) {
                $scope.countries = response.data;
                console.log("Http Sucess");
                console.log(response.data);
            });
});