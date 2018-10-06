$(document).ready(function() {

    $("#registration").submit(function() {

        if (!$("#registration input[name=name]").val())
        {
            alert("Missing username.");
            return false;
        }
        else if (!$("#registration input[name=password]").val())
        {
            alert("Missing password.");
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