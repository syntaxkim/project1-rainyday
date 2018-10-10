/* This JavaScript code is written in jQuery */

$(document).ready(function() {

    $("#search").submit(function() {
        if (!$("#search input[name=location]").val())
        {
            alert("Nothing to search.")
            return false;
        }
        return true;
    });

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
    
    $(".delete").submit(function() {
        confirm({
            title: 'Confirmation',
            content: 'Are your sure you want to delete this comment?'
        });
    });

    /* $(".delete").submit(function () {
        alert("hi");
        return true;
    }); */

});