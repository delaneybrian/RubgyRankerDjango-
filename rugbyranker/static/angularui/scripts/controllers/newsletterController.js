sportModule.controller('newsletterController', function($scope, $http) {

    $scope.emailmessage = "Sign Up To Our Monthly Newsletter:";

    $scope.submit = function(emailaddress){
        $scope.test = emailaddress;

        var dictionary = {
            email_address: emailaddress
        };

        jsondictionary = JSON.stringify(dictionary);

        $http.post('/api/newsletter/', jsondictionary)
            .success(function () {
                $scope.emailmessage = "Thanks for Subscribing";
            })
            .error(function (data, status, header, config) {
                $scope.emailmessage = "Error Subscribing Please Try Again Later";
            });

    };
});