document.getElementById("contactBtn").addEventListener("click", function() {
    alert("Thanks for reaching out! I'll get back to you soon.");
});
// Filter Gallery Logic
const filterButtons = document.querySelectorAll(".filter-btn");
const filterImages = document.querySelectorAll(".filter-gallery img");

filterButtons.forEach(button => {
    button.addEventListener("click", () => {
        // Purane button se 'active' color hatao
        document.querySelector(".active").classList.remove("active");
        // Naye click kiye hue button par 'active' color lagao
        button.classList.add("active");

        let filterName = button.getAttribute("data-name");

        filterImages.forEach(img => {
            let imgName = img.getAttribute("data-name");
            
            // Agar "all" pe click kiya hai, ya fir button ka naam photo ke naam se match karta hai
            if (filterName === "all" || filterName === imgName) {
                img.classList.remove("hide");
            } else {
                img.classList.add("hide"); // Nahi match kiya toh chupa do
            }
        });
    });
});
// Pricing Booking Buttons
document.querySelectorAll(".book-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        alert("Awesome choice! Please fill the Contact form below with your package name, and we will get back to you.");
        // Contact section par scroll karne ke liye
        document.getElementById("contact").scrollIntoView(); 
    });
});
// Scroll Reveal Animation
window.addEventListener('scroll', reveal);

function reveal() {
    let reveals = document.querySelectorAll('.reveal');
    
    for (let i = 0; i < reveals.length; i++) {
        let windowHeight = window.innerHeight;
        let revealTop = reveals[i].getBoundingClientRect().top;
        let revealPoint = 100; // Element kitna screen me aane ke baad show ho
        
        if (revealTop < windowHeight - revealPoint) {
            reveals[i].classList.add('active');
        }
    }
}
// Ek baar run kar dete hain load hote hi
reveal();
