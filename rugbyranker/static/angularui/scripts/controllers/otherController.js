sportModule.controller('faqController', function ($scope, $http, $location) {

    $http.get("/api/faq/")
        .then(function (response) {
            $scope.faqs = response.data;
        });

});
