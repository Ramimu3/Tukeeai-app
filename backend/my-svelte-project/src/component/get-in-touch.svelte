<script>
        export let isDarkMode = false;

</script>

<section id="contact" class:dark={isDarkMode}>
    <div class="container">
        <div class="section-header">
            <h3>Get In Touch !</h3>
            <p>Launch your campaign and benefit from our expertise on designing and managing conversion centered HTML pages.</p>
        </div>
        <div class="contact-content">
            <div class="contact-form">
                <div class="form-container">
                    <form>
                        <div class="form-row">
                            <div class="form-group">
                                <input name="name" id="name" type="text" class="form-input" placeholder="Name :" />
                            </div>
                            <div class="form-group">
                                <input name="email" id="email" type="email" class="form-input" placeholder="Email :" />
                            </div>
                        </div>
                        <div class="form-group">
                            <input name="subject" id="subject" class="form-input" placeholder="Subject :" />
                        </div>
                        <div class="form-group">
                            <textarea name="comments" id="comments" class="form-input" placeholder="Message :"></textarea>
                        </div>
                        <button type="submit" id="submit" name="send" class="submit-button">Send Message</button>
                    </form>
                </div>
            </div>
            <div class="contact-info">
                <div class="info-container">
                    <div class="info-item">
                        <div class="icons">
                            <i class="uil uil-phone"></i>
                        </div>
                        <div class="info-content">
                            <h5>Phone</h5>
                            <a href="tel:+152534-468-854">+152 534-468-854</a>
                        </div>
                    </div>
                    <div class="info-item">
                        <div class="icons">
                            <i class="uil uil-envelope"></i>
                        </div>
                        <div class="info-content">
                            <h5>Email</h5>
                            <a href="mailto:contact@example.com">contact@example.com</a>
                        </div>
                    </div>
                    <div class="info-item">
                        <div class="icons">
                            <i class="uil uil-map-marker"></i>
                        </div>
                        <div class="info-content">
                            <h5>Location</h5>
                            <p>C/54 Northwest Freeway, Suite 558, Houston, USA 485</p>
                        </div>
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

.container {
    width: 100%;
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 2rem;
}

.section-header {
    text-align: center;
    margin-bottom: 2rem;
}

.section-header h3 {
    font-size: 1.5rem;
    font-weight: 500;
    margin-bottom: 1rem;
}

.section-header p {
    color: #94a3b8;
    max-width: 42rem;
    margin: 0 auto;
}

.dark .section-header p {
    color: #cbd5e1;
}

.contact-content {
    display: grid;
    grid-template-columns: 1fr;
    gap: 30px;
    margin-top: 2rem;
    align-items: center;
}

.contact-form {
    grid-column: span 8;
}

.form-container {
    padding: 1.5rem;
    border-radius: 30px;
    background-color: var(--color-back);
    border: 1px solid var(--color-border);
}

.dark .form-container {
    padding: 1.5rem;
    border-radius: 30px;
    background-color: var(--color-Myrtle-Green);
    border: 1px solid var(--color-border);
}

.form-row {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
}

.form-group {
    margin-bottom: 1.25rem;
}

.form-input {
    width: 100%;
    padding: 0.5rem 0.75rem;
    height: 2.5rem;
    background-color: transparent;
    border: 1px solid inherit;
    border-radius: 0.25rem;
    outline: none;
}



.form-input:focus {
    border-color: var(--color-turquoise);
}


textarea.form-input {
    height: 7rem;
}

.submit-button {
    display: inline-block;
    padding: 0.5rem 1.25rem;
    font-weight: 500;
    vertical-align: middle;
    transition: background-color 0.5s ease-in-out, border-color 0.5s ease-in-out;
    font-size: 1rem;
    text-align: center;
    background-color: var(--color-turquoise);
    color: var(--color-black);
    border-radius: 0.375rem;
}

.submit-button:hover {
    background-color: var(--color-turquoise-hover);
}


.contact-info {
    grid-column: span 4;
}

.info-container {
    margin-left: 2rem;
}

.info-item {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
}

.icons {
    text-align: center;
    margin-right: 1.5rem;
}

.icons i {
    display: block;
    border-radius: 0.25rem;
    font-size: 1.5rem;
    margin-bottom: 0;
}

.dark .icons i {
    color: #fff;
}

.info-content {
    flex: 1;
}

.info-content h5 {
    font-size: 1.125rem;
    margin-bottom: 0.5rem;
    font-weight: 500;
}

.dark .info-content h5 {
    color: #fff;
}

.info-content a,
.info-content p {
    color: #94a3b8;
}

@media (min-width: 768px) {
    section {
        padding: 6rem 0;
    }

    .section-header h3 {
        font-size: 1.75rem;
    }

    .contact-content {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 1024px) {
    .contact-content {
        grid-template-columns: repeat(12, 1fr);
    }

    .contact-form {
        grid-column: span 8;
    }

    .contact-info {
        grid-column: span 4;
    }
}

</style>