sportModule.controller('newsletterController', function($scope, $http) {

    $scope.emailmessage = "Sign Up To Our Monthly Newsletter:";

    $scope.submit = function(emailaddress){
        $scope.test = emailaddress;

        console.log(host + 'api/newsletter');

        var dictionary = {
            email_address: emailaddress
        };

        jsondictionary = JSON.stringify(dictionary);

        $http.post('/api/newsletter/', jsondictionary)
            .success(function () {
                console.log("HTTP SUCESS");
                $scope.emailmessage = "Thanks for Subscribing";
            })
            .error(function (data, status, header, config) {
                console.log("HTTP ERROR");
                $scope.emailmessage = "Error Subscribing Please Try Again Later";
            });

    };
});