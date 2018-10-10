document.addEventListener('DOMContentLoaded', () => {

    /* Make sure a username or password is submitted */
    let form = document.querySelector("#authentication");
    form.onsubmit = function() {

        if (!form.name.value) {
            alert("Missing username.");
            return false;
        }
        else if (!form.password.value) {
            alert("Missing password.");
            return false;
        }
        return true;
    };

});

/* the same code in jQuery */
/* $(document).ready(function() {

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
}); */