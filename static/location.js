/* written in jQuery */
$(document).ready(function() {

    $("#comment").submit(function() {

        if (!$("#comment input[name=comment]").val())
        {
            alert("No comment to submit.")
            return false;
        }
        else if ($("#comment input[name=comment]").val().length > 100)
        {
            alert("Comment is too long. Please make it less than 100 characters.");
            return false;
        }
        return true;
    });
    
});