<script>
    import image from '../assets/images/client/01.jpg';
    import image1 from '../assets/images/client/05.jpg';
    import image2 from '../assets/images/client/02.jpg';
    import image3 from '../assets/images/client/04.jpg';
    import image4 from '../assets/images/client/03.jpg';
    import image5 from '../assets/images/client/06.jpg';
    export let isDarkMode = false;

</script>
<section id="testi" class:dark={isDarkMode}>
    <div class="container">
        <div class="section-header">
            <h3>Client's Review</h3>
            <p>This is just a simple text made for this unique and awesome template, you can replace it with any text.</p>
        </div>

        <div class="testimonial-grid">
            <ul class="testimonial-list">
                <li class="testimonial-item">
                    <div class="testimonial-header">
                        <img src="/static/build/assets/01.jpg" alt="" />
                        <div class="testimonial-author">
                            <a href="/">Thomas Israel</a>
                            <p>C.E.O</p>
                        </div>
                    </div>
                    <div class="testimonial-content">
                        <p>I didn't know a thing about icon design until I read this book. Now I can create any icon I need in no time. Great resource!</p>
                        <ul class="rating">
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                        </ul>
                    </div>
                </li>

                <li class="testimonial-item">
                    <div class="testimonial-header">
                        <img src="/static/build/assets/02.jpg" alt="" />
                        <div class="testimonial-author">
                            <a href="/">Barbara McIntosh</a>
                            <p>C.E.O</p>
                        </div>
                    </div>
                    <div class="testimonial-content">
                        <p>There are so many things I had to do with my old software that I just don't do at all with Techwind. Suspicious but I can't say I don't love it.</p>
                        <ul class="rating">
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                        </ul>
                    </div>
                </li>
            </ul>

            <ul class="testimonial-list hidden-sm">
                <li class="testimonial-item">
                    <div class="testimonial-header">
                        <img src="/static/build/assets/03.jpg" alt="" />
                        <div class="testimonial-author">
                            <a href="/">Carl Oliver</a>
                            <p>C.E.O</p>
                        </div>
                    </div>
                    <div class="testimonial-content">
                        <p>The best part about Techwind is every time I pay my employees, my bank balance doesn't go down like it used to. Looking forward to spending this extra cash when I figure out why my card is being declined.</p>
                        <ul class="rating">
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                        </ul>
                    </div>
                </li>

                <li class="testimonial-item">
                    <div class="testimonial-header">
                        <img  src="/static/build/assets/04.jpg" alt="" />
                        <div class="testimonial-author">
                            <a href="/">Jill Webb</a>
                            <p>C.E.O</p>
                        </div>
                    </div>
                    <div class="testimonial-content">
                        <p>I'm trying to get a hold of someone in support, I'm in a lot of trouble right now and they are saying it has something to do with my books. Please get back to me right away.</p>
                        <ul class="rating">
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                        </ul>
                    </div>
                </li>
            </ul>

            <ul class="testimonial-list hidden-lg">
                <li class="testimonial-item">
                    <div class="testimonial-header">
                        <img src="/static/build/assets/05.jpg" alt="" />
                        <div class="testimonial-author">
                            <a href="/">Barbara McIntosh</a>
                            <p>C.E.O</p>
                        </div>
                    </div>
                    <div class="testimonial-content">
                        <p>I used to have to remit tax to the EU and with Techwind I somehow don't have to do that anymore. Nervous to travel there now though.</p>
                        <ul class="rating">
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                        </ul>
                    </div>
                </li>

                <li class="testimonial-item">
                    <div class="testimonial-header">
                        <img src="/static/build/assets/06.jpg" alt="" />
                        <div class="testimonial-author">
                            <a href="/">Janisha Doll</a>
                            <p>C.E.O</p>
                        </div>
                    </div>
                    <div class="testimonial-content">
                        <p>This is the fourth email I've sent to your support team. I am literally being held in jail for tax fraud. Please answer your damn emails, this is important.</p>
                        <ul class="rating">
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                            <li><i class="mdi mdi-star"></i></li>
                        </ul>
                    </div>
                </li>
            </ul>
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

.section-header {
    text-align: center;
    margin-bottom: 2rem;
}

.section-header h3 {
    font-size: 1.5rem;
    font-weight: 500;
    margin-bottom: 1.5rem;
}

@media (min-width: 768px) {
    .section-header h3 {
        font-size: 1.75rem;
    }
}

.section-header p {
    color: #94a3b8;
    max-width: 42rem;
    margin: 0 auto;
}

.testimonial-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 30px;
    margin-top: 2rem;
}

@media (min-width: 640px) {
    .testimonial-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 1024px) {
    .testimonial-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

.testimonial-list {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.testimonial-item {
    border-radius: 30px;
    padding: 1.5rem;
    background-color: var(--color-back);
}
.dark .testimonial-item {
    border-radius: 30px;
    padding: 1.5rem;
    background-color: var(--color-Myrtle-Green);
}

.testimonial-header {
    display: flex;
    align-items: center;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #e5e7eb;
}

.testimonial-header img {
    width: 4rem;
    height: 4rem;
    border-radius: 50%;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.dark .testimonial-header img {
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.8), 0 2px 4px -1px rgba(0, 0, 0, 0.8);
}

.testimonial-author {
    margin-left: 1rem;
}

.testimonial-author a {
    font-size: 1.125rem;
    transition: color 0.5s ease-in-out;
}

.testimonial-author a:hover {
    color: var(--color-turquoise);
}

.testimonial-author p {
    color: var(--color-black);
    font-weight: 600;
}

.dark .testimonial-author p {
    color: var(--color-silver);
    font-weight: 600;
}

.testimonial-content {
    margin-top: 1.5rem;
}

.testimonial-content p {
    color: var(--color-black);
}

.dark .testimonial-content p {
    color: var(--color-sliver);
}


.rating {
    list-style: none;
    margin: 0;
    padding: 0;
    color: #fbbf24;
    margin-top: 0.5rem;
}

.rating li {
    display: inline;
    margin-right: 0.25rem;
}

.hidden-sm {
    display: none;
}

@media (min-width: 640px) {
    .hidden-sm {
        display: flex;
    }
}

.hidden-lg {
    display: none;
}

@media (min-width: 1024px) {
    .hidden-lg {
        display: flex;
    }
}

</style>