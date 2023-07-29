// Close messages after 5 seconds
$(document).ready(function () {
    setTimeout(function () {
        let messages = document.getElementsByClassName("message-container");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 5000);
});