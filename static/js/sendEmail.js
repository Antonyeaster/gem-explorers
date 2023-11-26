function sendMail(contactIdeaForm) {
    emailjs.send("service_zbsha8l", "template_jz8kdor", {
        "from_name": contactIdeaForm.name.value,
        "from_email": contactIdeaForm.emailaddress.value,
        "idea": contactIdeaForm.idea.value,
        "message": contactIdeaForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        });
    return false;
}