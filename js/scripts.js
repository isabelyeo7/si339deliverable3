// DOMContentLoaded to ensure the DOM is fully loaded before running script
document.addEventListener('DOMContentLoaded', () => {
    // function to toggle navigation menu
    console.log('DOM fully loaded and parsed')

    const preloadImage = new Image();
    preloadImage.src = '../images/default_image.jpg';
    
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        console.log('nav menu clicked');
    });

    // function to toggle comments visibility
    document.querySelectorAll('.collapse-btn').forEach(button => {
        button.addEventListener('click', () => {
            const commentSection = button.nextElementSibling;
            if(commentSection.style.display == "none" || commentSection.style.display == "") {
                commentSection.style.display = "block";
                button.textContent = "Hide Comments";
                console.log('hide comments');
            } else {
                commentSection.style.display = "none";
                button.textContent = "Show Comments";
                console.log('comments shown');
            }
        });
    });

    // function to set theme mode
    function setTheme(mode) {
        document.body.classList.remove('dark-mode', 'high-contrast-mode');
        if(mode == 'dark') {
            document.body.classList.add('dark-mode');
            console.log('dark mode set');
        } else if (mode == 'high-contrast') {
            document.body.classList.add('high-contrast-mode');
            console.log('high contrast mode set');
        }
    }

    // add event listeners to theme buttons
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', () => {
            if(button.textContent.includes('Dark Mode')) {
                console.log('dark mode selected')
                setTheme('dark');
            } else if (button.textContent.includes('High Contrast')) {
                setTheme('high-contrast');
                console.log('high contrast mode selected')
            } else if (button.textContent.includes('Normal Mode')) {
                document.body.classList.remove('dark-mode', 'high-contrast-mode');
            }
        });
    });

    // smooth scroll animation for anchor links
    document.querySelectorAll('a[href^="#').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // interactive gallery lightbox
    document.querySelectorAll('#gallery img').forEach(img => {
        img.addEventListener('click', () => {
            const lightbox = document.createElement('div');
            lightbox.classList.add('lightbox');
            document.body.appendChild(lightbox);

            const imgClone = img.cloneNode();
            lightbox.appendChild(imgClone);

            lightbox.addEventListener('click', () => {
                document.body.removeChild(lightbox);
            });
        });
    });

    // interactive lightbox for the profile image
    document.addEventListener('DOMContentLoaded', () => {
        const observer = new MutationObserver((mutationsList, observer) => {
            const profileImg = document.querySelector('.athlete-img');
            if (profileImg) {
                console.log('Profile image found with MutationObserver.');
                profileImg.addEventListener('click', () => {
                    const lightbox = document.createElement('div');
                    lightbox.classList.add('lightbox');
                    document.body.appendChild(lightbox);

                    const imgClone = profileImg.cloneNode();
                    imgClone.style.maxWidth = '90%';
                    imgClone.style.maxHeight = '90%';
                    lightbox.appendChild(imgClone);

                    lightbox.addEventListener('click', () => {
                        document.body.removeChild(lightbox);
                    });
                });
                observer.disconnect(); // Stop observing once the image is found
            }
        });
        observer.observe(document.body, { childList: true, subtree: true});
    });
    // Select all images on the page
    document.querySelectorAll('img').forEach(img => {
        // Add an event listener for the 'error' event
        img.addEventListener('error', () => {
            // Set a default image when the current image fails to load
            img.src = '../images/default_image.jpg'; // Path to your default image
            img.alt = 'Default image'; // Update the alt text for accessibility
            console.log('Image failed to load. Default image displayed.');
        });
    });
    
})