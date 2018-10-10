/* This JavaScript code is written in jQuery */

$(document).ready(function() {

    /* Make sure all information is correct before request to server */
    $("#registration").submit(function() {

        if (!$("#registration input[name=name]").val())
        {
            alert("Missing username.");
            return false;
        }
        else if ($("#registration input[name=name]").val().length < 2)
        {
            alert("Pick a username longer than 2 characters.");
            return false;
        }
        else if (!$("#registration input[name=password]").val())
        {
            alert("Missing password.");
            return false;
        }
        else if ($("#registration input[name=password]").val().length < 4)
        {
            alert("Pick a password longer than 4 characters.");
            return false;
        }
        else if (!$("#registration input[name=confirmation]").val())
        {
            alert("Missing password (again).");
            return false;
        }
        else if ($("#registration input[name=password]").val() != $("#registration input[name=confirmation]").val())
        {
            alert("Passwords don't match.");
            return false;
        }
        return true;
    });
    
});