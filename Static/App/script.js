// using single signup page for both type api call as well as single function method using current url method
if (window.location.toString().includes("single"))
console.log("single signup page")
else
console.log("multiple signup page")

const signupPage=document
.getElementById("signup-form")

if(signupPage) {
  signupPage.addEventListener("submit", async function (event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const first_name = document.getElementById("first_name").value;
    const last_name = document.getElementById("last_name").value;
    const contact = document.getElementById("contact").value;
    const password = document.getElementById("password").value;

    const formData = {
      username: username,
      first_name: first_name,
      last_name: last_name,
      contact: contact,
      password: password,
    };

    try {
      const response = await fetch("/api/signup/", {
        method: "POST",
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        console.log(data);
        document.location.replace("/login");
        alert("Successfully signed up");
      } 
      else {
        alert(Object.values(data)[0]);
      }

    } catch (error) {
      console.error("Error:", error);
      alert("Failed to sign up");
    }
  });
}

document
  .getElementById('login-form')
  .addEventListener("submit", async function (event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const formData = {
      username: username,
      password: password,
    };
    try {
      const response = await fetch("/api/login/", {
        method: "POST",
        body: JSON.stringify(formData),
      });
      
      const data = await response.json();
      if (response.ok) {
        console.log(data);
        alert("Successfully Log in");
      } 
      else {
        alert(data.message)
      }

    } catch (error) {
      console.error("Error:", error);
      alert("Failed to Login up");
    }
  });
