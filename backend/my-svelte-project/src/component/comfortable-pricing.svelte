<script>
        export let isDarkMode = false;

</script>
<section id="pricing" class:dark={isDarkMode}>
    <div class="container">
        <div class="pricing-header">
            <h3>Our Comfortable Pricing</h3>
            <p>Launch your campaign and benefit from our expertise on designing and managing conversion centered HTML pages.</p>
        </div>

        <div class="pricing-grid">
            <div class="pricing-card corporate">
                <div class="pricing-details">
                    <h3>Free Tier: Starter Pack
                    </h3>
                    <div class="price">
                        <span class="currency">$</span>
                        <span class="amount">0</span>
                        <span class="period">/ month</span>
                    </div>
                    <p>Corporate features for up to 100 users.</p>
                    <a href="/" class="btn btn-violet">Signup Now</a>
                </div>
                <div class="pricing-divider"></div>
                <ul class="pricing-features">
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>Daily Data Conversion </span>
                    </li>
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>WAccess to Basic Data Cleansing Tools</span>
                    </li>
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>Community Support</span>
                    </li>
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>One-time help training an AI model </span>
                    </li>
                </ul>
            </div>

            <div class="pricing-card corporate">
                <div class="pricing-details">
                    <h3>Standard Tier: Professional Growth
                    </h3>
                    <div class="price">
                        <span class="currency">$</span>
                        <span class="amount">9</span>
                        <span class="period">/ month</span>
                    </div>
                    <p>Corporate features for up to 100 users.</p>
                    <a href="/" class="btn btn-violet">Signup Now</a>
                </div>
                <div class="pricing-divider"></div>
                <ul class="pricing-features">
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>Unlimited Data Conversion</span>
                    </li>
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span> Advanced Data Cleansing Tools</span>
                    </li>
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>Data Integration Capabilities</span>
                    </li>
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>Priority Support</span>
                    </li>
                </ul>
            </div>

            <div class="pricing-card corporate">
                <div class="pricing-details">
                    <h3>Premium Tier: AI Innovator
                    </h3>
                    <div class="price">
                        <span class="currency">$</span>
                        <span class="amount">99</span>
                        <span class="period">/ Year</span>
                    </div>
                    <p>Corporate features for up to 100 users.</p>
                    <a href="/" class="btn btn-violet">Signup Now</a>
                </div>
                <div class="pricing-divider"></div>
                <ul class="pricing-features">
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>All Standard Tier Features </span>
                    </li>
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>Custom Conversion Scripts</span>
                    </li>
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>Exclusive Webinars and Training</span>
                    </li>
                    <li>
                        <i class="uil uil-check-circle"></i>
                        <span>Dedicated Account Manager</span>
                    </li>
                </ul>
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
        padding: 6rem 0;
    }
}

.container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 2rem;
}

.pricing-header {
    text-align: center;
    margin-bottom: 2rem;
}

.pricing-header h3 {
    font-size: 1.5rem;
    font-weight: 500;
    margin-bottom: 1rem;
}

@media (min-width: 768px) {
    .pricing-header h3 {
        font-size: 1.75rem;
    }
}

.pricing-header p {
    color: #94a3b8;
    max-width: 42rem;
    margin: 0 auto;
}

.dark .pricing-header p {
    color: #cbd5e1;
}

.pricing-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 30px;
    align-items: center;
    margin-top: 2rem;
}

@media (min-width: 768px) {
    .pricing-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

.pricing-card {
    padding: 1.5rem;
    border-radius: 0.375rem;
}

.pricing-card.corporate {
    background-color: var(--color-back);
    color: var(--color-black);
    border-radius: 30px;
}

.dark .pricing-card.corporate {
    background-color: var(--color-Myrtle-Green);
    color: var(--color-silver);
    border-radius: 30px;
}

.pricing-details {
    padding-bottom: 2rem;
}

.pricing-details h3 {
    font-size: 1.25rem;
    font-weight: 500;
    margin-bottom: 1.5rem;
}

.price {
    margin-bottom: 1.5rem;
}

.price .currency {
    position: relative;
    top: -1.25rem;
    font-size: 1.25rem;
}

.price .amount {
    font-size: 3rem;
    font-weight: 700;
}

.pricing-card.free .price .amount {
    font-weight: 500;
}

.price .period {
    display: inline-block;
    margin-left: 0.25rem;
}

.pricing-details p {
    margin-bottom: 1.5rem;
}

.pricing-card.business .pricing-details p {
    color: rgba(255, 255, 255, 0.5);
}

.pricing-card.free .pricing-details p,
.pricing-card.corporate .pricing-details p {
    color: #94a3b8;
}

.btn {
    display: inline-block;
    padding: 0.5rem 1.25rem;
    font-weight: 400;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    user-select: none;
    border: 1px solid transparent;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: 0.375rem;
    width: 100%;
}

.btn-violet {
    color: var(--color-black);
    background-color: var(--color-turquoise);
}

.btn-violet:hover {
    color: var(--color-black);
    background-color: var(--color-turquoise-hover);
}




.pricing-divider {
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    margin-bottom: 2rem;
}

.pricing-card.corporate .pricing-divider {
    border-color: #2f3742;
}

.dark .pricing-card.corporate .pricing-divider {
    border-color: rgba(255, 255, 255, 0.05);
}

.pricing-features {
    list-style: none;
    padding: 0;
    margin: 0;
}

.pricing-features li {
    display: flex;
    align-items: center;
    margin-bottom: 0.5rem;
}

.pricing-features li i {
    font-size: 1.25rem;
    margin-right: 0.5rem;
}

.pricing-card.business .pricing-features li {
    color: var(--color-black);
}

</style>