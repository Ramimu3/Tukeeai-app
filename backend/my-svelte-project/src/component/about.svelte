<script>
    import about from '../assets/Landing/About-us-page-bro.svg';
</script>

<section id="about">
    <div class="container">
        <div class="about-content">
            <div class="about-image">
                <div class="image-container">
                    <img src="/static/build/assets/About-us-page-bro.svg" alt="About Us" class="img-fluid">


                    <div class="image-overlay"></div>
                </div>
            </div>
            <div class="about-text">
                <div class="text-container">
                    <h3>About Us</h3>
                    <p>At Tukee, we are driven by the vision of democratizing AI development. Our platform bridges the gap between raw data and AI training by providing powerful, user-friendly tools that convert and prepare your data, no matter the size or complexity. Founded by experts in data science and artificial intelligence, we are committed to empowering developers, innovators, and businesses to unlock the full potential of their data.</p>
                    <div class="button-container">
                        <a href="/aboutus" class="read-more-button">
                            Read More <i class="uil uil-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section> 
<style>
    section {
        position: relative;
        padding: 4rem 0;
    }
    
    @media (min-width: 768px) {
        section {
            padding: 3rem 0;
        }
    }
    
    .container {
        max-width: 1280px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    .about-content {
        display: grid;
        grid-template-columns: 1fr;
        gap: 2.5rem;
        align-items: center;
    }
    
    @media (min-width: 768px) {
        .about-content {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    
    @media (min-width: 1024px) {
        .about-content {
            grid-template-columns: repeat(12, 1fr);
        }
    
        .about-image {
            grid-column: span 5;
        }
    
        .about-text {
            grid-column: span 7;
        }
    }
    
    .image-container {
        position: relative;
    }
    
    .image-container img {
        border-radius: 0.5rem;
        position: relative;
    }
    
    .image-overlay {
        position: absolute;
        bottom: 50%;
        transform: translateY(50%);
        left: 0;
        right: 0;
        text-align: center;
    }
    
    .text-container {
        margin-left: 1.75rem;
    }
    
    .text-container h3 {
        margin-bottom: 1rem;
        font-size: 1.25rem;
        font-weight: 500;
        
    }
    
    @media (min-width: 768px) {
        .text-container h3 {
            font-size: 1.5rem;
        }
    }
    
    .text-container p {
        color: #94a3b8;
        max-width: 42rem;
        margin: 0 auto;
        text-align: left;
    }
    
    .dark .text-container p {
        color: #cbd5e1;
    }
    
    .button-container {
        margin-top: 2rem;
    }
    
    .read-more-button {
        display: inline-block;
        padding: 0.5rem 1.25rem;
        font-weight: 400;
        letter-spacing: 0.025em;
        border: 1px solid;
        vertical-align: middle;
        transition: background-color 0.5s ease-in-out, border-color 0.5s ease-in-out;
        font-size: 1rem;
        text-align: center;
        background-color: var(--color-turquoise);
        color: #fff;
        border-radius: 0.375rem;
    }
    
    .read-more-button:hover {
        background-color: var(--color-turquoise-hover);
    }
    
    .read-more-button i {
        margin-left: 0.5rem;
    }
    </style>