const menuBtn = document.getElementById("menuBtn");
      const mobileMenu = document.getElementById("mobileMenu");
      const closeMenu = document.getElementById("closeMenu");

      menuBtn.addEventListener("click", () => {
        mobileMenu.classList.remove("hidden");
      });
      closeMenu.addEventListener("click", () => {
        mobileMenu.classList.add("hidden");
      });


    
const container = document.getElementById("logoContainer");
  const nextBtn = document.getElementById("nextBtn");
  const prevBtn = document.getElementById("prevBtn");

  nextBtn.addEventListener("click", () => {
    container.scrollBy({ left: 300, behavior: "smooth" });
  });
  prevBtn.addEventListener("click", () => {
    container.scrollBy({ left: -300, behavior: "smooth" });
  });
