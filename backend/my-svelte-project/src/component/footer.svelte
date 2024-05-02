<script>
import logo_dark from '../assets/Landing/Tukee-light.svg';
    import logo_light from '../assets/Landing/Tukee-dark.svg';
        import Switcher from './Switcher.svelte';
        export let isDarkMode = false;

</script>

<footer class="footer" class:dark={isDarkMode}>
    <div class="container">
        <div class="footer-content">
            <div class="footer-logo">
                <img src={isDarkMode ? logo_dark : logo_light} alt="Logo" />
                <p>Launch your campaign and benefit from our expertise on designing and managing conversion centered HTML pages.</p>
            </div>

            <ul class="footer-list">
                <li><a href="/services">Services</a></li>
                <li><a href="/aboutus">About Us</a></li>
                <li><a href="/blogs">Blogs</a></li>
                <li><a href="/team">Team</a></li>
                <li><a href="/pricing">Pricing</a></li>
                <li><a href="/contactus">Contact Us</a></li>
            </ul>
        </div>
    </div>
</footer>

<style>
        .footer {
    position: relative;
}

.container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 1rem;
}

.footer-content {
    padding: 3rem 0;
    text-align: center;
}

.footer-logo img {
    display: block;
    margin: 0 auto;
    width: 15%;
}

.footer-logo p {
    max-width: 42rem;
    margin: 2rem auto 0;
}

.footer-list {
    list-style: none;
    margin: 2rem 0 0;
    padding: 0;
    text-align: center;
}

.footer-list li {
    display: inline;
    padding: 0 0.5rem;
}

.footer-list li a {
    transition: color 0.5s ease-in-out;
}

.footer-list li a:hover {
    color: var(--color-turquoise);
}
</style>