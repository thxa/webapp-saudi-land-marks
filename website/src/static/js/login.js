document.getElementsById("alerts").remove(document.getElementsById(("alerts").children));

function validateRegisterForm()
{
    var registerFormObj = document.getElementById("registerForm");
    var firstName = registerFormObj.first_name.value;
    var lastName = registerFormObj.last_name.value;
    var email = registerFormObj.email.value;
    var everyThingsOK = true;

    if (!validateName(firstName))
    {
        alert("Error: Invalid First Name.");
        everyThingsOK = false;
    } 

    if (!validateName(lastName))
    {
        alert("Error: Invalid Last Name.");
        everyThingsOK = false;
    } 
    
    if (!validateEmail(email))
    {
        alert("Error: Invalid E-mail.");
        everyThingsOK = false;
    }

 
    if (everyThingsOK)
    {
        if (registerFormObj.email.checked)
            alert("Warning: The E-mail feature is currently not supported.");

        alert("Your request has been submitted successfully.\n Thank you!");
        return true;
    }
    else
        return false;
}
function validateName(name) { return (name.search(/^[-'\w\s]+$/) == 0);  }
function validateEmail(email) { return (email.search(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})$/) == 0); }

function printalert(text)
{
    alerts.appendChild("<p>Hello, </p>");
}