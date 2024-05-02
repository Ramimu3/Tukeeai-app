<script>
    import { HexagonIcon } from 'svelte-feather-icons';
    import customLight from '../assets/Landing/services/custom-support-light.svg';
    import customDark from '../assets/Landing/services/custom-support-dark.svg';
    import cleaningLight from '../assets/Landing/services/file-cleaning-light.svg';
    import cleaningDark from '../assets/Landing/services/file-cleaning-dark.svg';
    import aifileLight from '../assets/Landing/services/ai-file-light.svg';
    import aifileDark from '../assets/Landing/services/ai-file-dark.svg';
    
    export let isDarkMode = false;

    const services = [
        {
            iconLight: customLight,
            iconDark: customDark,
            title: 'Data Conversion',
            description: "Convert any data into AI-ready formats with our robust tools.",
        },
        {
            iconLight: cleaningLight,
            iconDark: cleaningDark,
            title: 'Data Cleansing',
            description: " Cleanse your data to ensure accuracy and relevancy for AI training.",
        },
        {
            iconLight: aifileLight,
            iconDark: aifileDark,
            title: 'Data Integration',
            description: "Seamlessly integrate multiple data sources for a unified AI training dataset.",
        },
        {
            iconLight: customLight,
            iconDark: customDark,
            title: 'Custom Solutions',
            description: "Tailor-made services to fit your specific AI model training needs.",
        },
    ];
</script>

<section id="features" class:dark={isDarkMode}>
    <div class="container">
        <div class="features-grid">
            <div class="features-content">
                <h3>What We Offer</h3>
                <p>
                    This is just a simple text made for this unique and awesome template, you can replace it with any text.
                </p>
                <button class="learn-more-button">
                    Learn More
                </button>
            </div>
            <div class="services-grid">
                {#each services as service}
                    <div class="service-item">
                        <div class="service-icon">
                            <div class="icon-overlay">
                                <img src={isDarkMode ? service.iconDark : service.iconLight} alt={service.title} class="icon" />
                            </div>
                        </div>
                        <div class="service-details">
                            <a href="/services" class="service-title">
                                {service.title}
                            </a>
                            <p class="service-description">
                                {service.description}
                            </p>
                        </div>
                    </div>
                {/each}
            </div>
        </div>
    </div>
</section>

<style>
    section {
        color: var(--color-black);
        background-color: var(--color-silver);
        padding: 2rem 0;
        }

    section.dark {
        color: var(--color-white);
        background-color: var(--color-jet);
    }

    .container {
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: 1fr;
        place-items: center;
        max-width: 1280px;
        margin: 0 auto;
        padding: 0 2rem;
    }

    .features-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 2rem;
        width: 100%;
        background-color: var(--color-back);
    border-radius: 45px;
    padding: 1rem;
    }

    .dark     .features-grid {
        background-color: var(--color-Myrtle-Green);
    }

    @media (min-width: 768px) {
        .features-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    .features-content {
        display: grid;
        place-items: center;
        text-align: center;
        align-content: center;
    }

    .features-content h3 {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 2rem;
    }

    .features-content p {
        font-size: 1.25rem;
        margin-bottom: 2rem;
    }

    .learn-more-button {
        background-color: var(--color-turquoise);
        color: var(--color-black);
        font-size: 1rem;
        border-radius: 0.5rem;
        transition: background-color 0.3s ease-in-out;
        padding: 0.5rem 1.25rem;
    }

    .learn-more-button:hover {
        background-color: var(--color-turquoise-hover);
    }

    .services-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
    }

    .service-item {
        display: grid;
        place-items: center;
        text-align: center;
        padding: 1.5rem;
        border-radius: 0.75rem;
        color: var(--color-black);
    }

    .service-icon {
        position: relative;
        width: 100%;
        margin-bottom: 1.5rem;
    }

    .icon-overlay {
        width: 100%;
        height: 100%;
        display: grid;
        place-items: center;
    }

    .icon-overlay img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }

    .service-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
        transition: color 0.3s ease-in-out;
    }

    .service-title:hover {
        color: var(--color-turquoise);
    }

    .service-description {
        font-size: 1.125rem;
        color: var(--color-gray);
    }

    .dark .service-description {
        color: var(--color-silver);
    }
</style>
