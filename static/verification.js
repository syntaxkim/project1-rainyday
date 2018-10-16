document.addEventListener('DOMContentLoaded', () => {

    /* Make sure password is submitted */
    let form = document.querySelector("#verification");
    form.onsubmit = function() {

        if (!form.password.value) {
            alert("Missing password.");
            return false;
        }
        return true;
    };

});