<script>
    import { push } from 'svelte-spa-router';
    import { Modal, Content, Trigger } from "sv-popup";
      import NavbarSmallLight from './component/navbar-small-light.svelte';
      import About from './component/about.svelte';
      import ComfortablePricing from './component/comfortable-pricing.svelte';
      import Footer from './component/footer.svelte';
      import GetInTouch from './component/get-in-touch.svelte';
      import BlogsNews from './component/blogs-news.svelte';
      import ClientSreview from './component/clientsreview.svelte';
      import OurServices from './component/our-services.svelte';
    import BackgroudImage from "./assets/images/bg/bg.jpg";
    import cta from './assets/images/cta.jpg';
    import { onMount, onDestroy } from 'svelte';
  
    onMount(() => {
      const appElement = document.getElementById('app');
  
      if (appElement) {
        appElement.style.margin = '0';
        appElement.style.padding = '0';
        appElement.style.textAlign = 'center';
        appElement.style.width = '100%';
        appElement.style.marginLeft = '0';
      }
    });
  
    onDestroy(() => {
      const appElement = document.getElementById('app');
  
      if (appElement) {
        appElement.style.margin = '';
        appElement.style.padding = '';
        appElement.style.textAlign = '';
        appElement.style.width = '';
        appElement.style.marginLeft = '';
      }
    });
    
    </script>
    
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-4xl font-bold mb-4">Welcome to My App</h1>
      <p class="text-lg mb-8">Discover the amazing features of our application.</p>
      <div class="space-x-4">
        <button class="bg-primary text-white px-6 py-3 rounded-lg font-bold" on:click={() => push('/signin')}>Sign In</button>
        <button class="bg-secondary text-white px-6 py-3 rounded-lg font-bold" on:click={() => push('/signup')}>Sign Up</button>
        <button class="bg-accent text-white px-6 py-3 rounded-lg font-bold" on:click={() => push('/dashboard')}>Go to Dashboard</button>
      </div>
    </div>
    <NavbarSmallLight menualignclass="ms-auto" />
    
    <main class="content">
      <section class="hero">
        <div class="hero-content">
          <h1>Hero Title</h1>
          <p>Hero subheading goes here.</p>
          <button>Call to Action</button>
        </div>
        <div class="hero-image">
          <img src="path/to/your/image.jpg" alt="Hero Image" />
        </div>
      </section>
      
      <section class="box">
        <div class="box-item">
          <h3>Title 1</h3>
          <p>Subtext for Title 1</p>
        </div>
        <div class="box-item">
          <h3>Title 2</h3>
          <p>Subtext for Title 2</p>
        </div>
        <div class="box-item">
          <h3>Title 3</h3>
          <p>Subtext for Title 3</p>
        </div>
      </section>
    </main>
    <section class="section">
      <div class="section-image">
        <img src="path/to/your/image.jpg" alt="Section Image" />
      </div>
      <div class="section-content">
        <h2>Section Headline</h2>
        <p>Section subheading goes here.</p>
      </div>
    </section>
    <section class="services">
      <h2>How Building with us will go</h2>
      <div class="services-grid">
        <div class="service-item">
          <div class="service-icon">
            <!-- Replace with your icon code or image -->
            <i class="fas fa-icon1"></i>
          </div>
          <h3>Service 1</h3>
          <p>Description of Service 1</p>
        </div>
        <div class="service-item">
          <div class="service-icon">
            <!-- Replace with your icon code or image -->
            <i class="fas fa-icon2"></i>
          </div>
          <h3>Service 2</h3>
          <p>Description of Service 2</p>
        </div>
        <div class="service-item">
          <div class="service-icon">
            <!-- Replace with your icon code or image -->
            <i class="fas fa-icon3"></i>
          </div>
          <h3>Service 3</h3>
          <p>Description of Service 3</p>
        </div>
        <div class="service-item">
          <div class="service-icon">
            <!-- Replace with your icon code or image -->
            <i class="fas fa-icon4"></i>
          </div>
          <h3>Service 4</h3>
          <p>Description of Service 4</p>
        </div>
      </div>
    </section>
  <ComfortablePricing />
  <ClientSreview />
  <GetInTouch />
  <Footer />
  
  <style>
   .hero {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 2rem;
    }
  
    .hero-content {
      max-width: 50%;
    }
  
    .hero-image {
      max-width: 40%;
    }
  
    .hero-image img {
      width: 100%;
      height: auto;
    }
  
    .box {
      display: flex;
      justify-content: space-around;
      padding: 2rem;
    }
  
    .box-item {
      text-align: center;
    }
    /* Section Styles */
    .section {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 2rem;
    }
  
    .section-image {
      max-width: 40%;
    }
  
    .section-image img {
      width: 100%;
      height: auto;
    }
  
    .section-content {
      max-width: 50%;
    }
    /* CTA Section Styles */
    .services {
      text-align: center;
      padding: 2rem;
    }
  
    .services-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 2rem;
      margin-top: 2rem;
    }
  
    .service-item {
      text-align: center;
    }
  
    .service-icon {
      font-size: 2rem;
      margin-bottom: 1rem;
    }
    
  </style>