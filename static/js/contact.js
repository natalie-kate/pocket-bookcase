// Declared constant variables.
const sendForm = document.getElementById("contact-form");
const response = document.getElementById("response");
const submitbutton = document.getElementById("submit-button");

// Added event listener to submit button on form
sendForm.addEventListener('submit', contactForm);

// Event handler function
function contactForm(event) {
    event.preventDefault();
    let firstName = sendForm.elements[1].value;
    let email = sendForm.elements[3].value;
    let comment = sendForm.elements[4].value;
    let secondName = sendForm.elements[2].value;

// Assign personalised HTML to modal
    let responseText = `
    <h4>Thanks ${firstName}</h4>
    <p>The message submitted was:<br>
     "${comment}"<br>
    We'll get back to you as soon as possible via ${email}.<br>
    Have a great day of reading <i class="fas fa-book"</p>`;
    response.innerHTML = responseText;  

// Stars rating to be sent in email
    let stars = document.getElementsByName("rating");
    let rating;
    if (stars[0].checked == true) {
        rating = stars[0].value;
    } else if (stars[1].checked == true) {
        rating = stars[1].value;
    } else if (stars[2].checked == true) {
        rating = stars[2].value;
    } else if (stars[3].checked == true) {
        rating = stars[3].value;
    } else {
        rating = stars[4].value;
    }

// Change Submit to Sent on submit button
    submitbutton.innerText = "Sent!";
     
// Show personalised modal
    $('#submit-modal').modal('show');

// Send contact form info via emailJS
    return sendMail(this);

    function sendMail (sendForm) {
        emailjs.init("user_wAOlLN2zYLGpP3C5ZlKTc");
        emailjs.send("service_vk0diqa","pocket-bookcase", {
            "first-name" : firstName,
            "second-name" : secondName,
            "email-address" : email,
            "comment" : comment,
            "rating" : rating
        }); 
    }
} 