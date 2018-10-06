$(document).ready(function() {

    $("#authentication").submit(function() {
        
        if (!$("#authentication input[name=name]").val())
        {
            alert("Missing username.");
            return false;
        }
        else if (!$("#authentication input[name=password]").val())
        {
            alert("Missing password.");
            return false;
        }
        return true;
    });
});