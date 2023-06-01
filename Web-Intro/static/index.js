// Get the button element by its ID
let button = document.querySelector("button#myButton");
let url = "http://127.0.0.1:5000/click";

// Add event listener to the button
button.addEventListener("click", function () {
  // Perform an action when the button is clicked
  //alert("Button clicked!");

  //fetchData(URL + "hello/" + "Itay");
  fetchData(url);
});

function fetchData(url) {
  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Handle the retrieved data
      console.log(data);
    })
    .catch((error) => {
      // Handle any errors
      console.error("Error:", error);
    });
}
