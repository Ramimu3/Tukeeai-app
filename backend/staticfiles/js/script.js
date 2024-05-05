const categories = document.querySelectorAll(".categorie");

const updateMaxHeight = () => {
  for (const categorie of categories) {
    const titleHeight =
      categorie.querySelector(".categorie-title").offsetHeight;
    if (!categorie.classList.contains("active")) {
      categorie.style.maxHeight = `${titleHeight + 64}px`;
    }
  }
};

const handleCategorieClick = (e) => {
  const currentElement = e.currentTarget;
  for (const categorie of categories) {
    if (categorie !== currentElement) {
      categorie.classList.remove("active");
    }
  }
  currentElement.classList.toggle("active");
  updateMaxHeight();
};

updateMaxHeight();

for (const categorie of categories) {
  categorie.addEventListener("click", handleCategorieClick);
}

// SCROLLED ANIMATION

let lastScrollY = 0; // Variable to store the last scroll position

window.addEventListener("scroll", function () {
  // Get the section element
  const section = document.querySelector(".hero-section-content"); // Adjust the selector as per your HTML structure

  // Get the bottom position of the section
  const sectionBottom = section.offsetTop + section.offsetHeight;
  const sectionTop = section.offsetTop;

  // Calculate the upper part of the screen
  const upperScreen = window.scrollY;

  // Check if the upper part of the screen hits 200px from the bottom of the section
  if (
    upperScreen >= sectionBottom - 200 &&
    upperScreen <= sectionTop + section.offsetHeight
  ) {
    // Calculate the distance scrolled since the last scroll event
    const scrollDelta = window.scrollY - lastScrollY;

    // Calculate the scale factor based on the scroll position
    let scaleFactor =
      1 - (upperScreen - sectionBottom + 200) / (section.offsetHeight + 200);
    scaleFactor = Math.max(0.9, Math.min(1, scaleFactor));

    // Calculate the translateY value based on the scroll position and section height
    const translateY = (section.offsetHeight / 2) * (1 - scaleFactor) * 4; // Adjust the factor to increase translation towards the bottom

    // Update the new translateY value by adding the scrollDelta
    const newTranslateY = translateY + scrollDelta;

    // Apply the new translateY and scale values to the section
    section.style.transition = "none"; // Disable transition during scroll
    section.style.transform = `scale(${scaleFactor}) translateY(${newTranslateY}px)`;

    // Update the last scroll position within the condition
    lastScrollY = window.scrollY;
  } else if (upperScreen === 0) {
    // Reset the transform when scrolling back to the top
    section.style.transition = "none";
    section.style.transform = `scale(1) translateY(0)`;
  }
});
