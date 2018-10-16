document.addEventListener('DOMContentLoaded', () => {

    /* Make sure a username or password is submitted */
    let form = document.querySelector("#newpassword");
    form.onsubmit = function() {

        if (!form.password.value) {
            alert("Please type your new password.");
            return false;
        }
        else if (form.password.value.length < 4) {
            alert("Pick a password longer than 4 characters.")
            return false;
        }
        else if (!form.confirmation.value) {
            alert("Type your new password again.");
            return false;
        }
        else if (form.confirmation.value != form.password.value) {
            alert("Passwords don't match.")
            return false;
        }
        return true;
    };

});