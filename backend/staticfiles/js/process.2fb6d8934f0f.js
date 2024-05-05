document.addEventListener('DOMContentLoaded', function() {
    const steps = document.querySelectorAll('.progress-step');
    let currentStep = 0;

    function advanceStep() {
        if (currentStep > 0) {
            steps[currentStep - 1].classList.remove('active');
        }
        if (currentStep < steps.length) {
            steps[currentStep].classList.add('active');
            currentStep++;
        } else {
            clearInterval(progressInterval); // Stop the animation once all steps are completed
        }
    }

    // Simulate progress every 4 seconds to give more time to appreciate the loading animation
    let progressInterval = setInterval(advanceStep, 4000);
});
