/* This JavaScript code is written in jQuery */

$(document).ready(function() {

    /* If nothing to search */
    $("#search").submit(function() {
        if (!$("#search input[name=location]").val())
        {
            alert("Nothing to search.")
            return false;
        }
        return true;
    });

    /* If no comment to submit */
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
    
    /* Confirm before deleteion of a comment */
    $(".delete").submit(function() {
        let answer = confirm('Are your sure you want to delete this comment?');
        if (answer)
        {
            return true;
        } else {
            return false;
        }
    });

});