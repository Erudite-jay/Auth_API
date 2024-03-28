document
  .getElementById("signup-form")
  .addEventListener("submit", async function (event) {
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

      if (!response.ok) {
        alert("Network response was not ok");
        return;
      }

      const data = await response.json();
      console.log(data);
      document.location.replace("/login");
      alert("Successfully signed up");

    } catch (error) {
      console.error("Error:", error);
      alert("Failed to sign up");
    }
  });


  document
  .getElementById("login-form")
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

      if (!response.ok) {
        alert("Network response was not ok");
        return;
      }

      const data = await response.json();
      console.log(data);
      document.location.replace("/login");
      alert("Successfully signed up");

    } catch (error) {
      console.error("Error:", error);
      alert("Failed to sign up");
    }
  });
