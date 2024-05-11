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
  import { onMount, onDestroy } from 'svelte';
  import hero from './assets/Landing/Server-amico.svg';
  import question from './assets/Landing/Questions-bro.svg';
  import data from './assets/Landing/Data-extraction-bro.svg';

  let isDarkMode = false;

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
  
  <NavbarSmallLight bind:isDarkMode={isDarkMode} />
  <div class="home-container" class:dark={isDarkMode}>
    <div class="row">
      <div class="col-md-6">
        <div class="top-section">
          <div class="hero-header"><h2>Create AI Datasets From any Data</h2></div>
          <p>Train AI models to fit your needs</p>
        </div>
        <div class="bottom-section">
          <div class="image-container">
            <img src="/static/build/assets/Data-extraction-bro.svg" alt="hero-1" class="img-fluid">
          </div>
          <div class="button-container">
            <button class="btn btn-primary btn-lg">
              Start Now <i class="fas fa-arrow-right"></i>
            </button>
          </div>
        </div>
      </div>
      <div class="col-md-6 right-column">
        <img src="/static/build/assets/Server-amico.svg" alt="hero-2" class="img-fluid">
      </div>
    </div>
  </div>
<About />
<OurServices bind:isDarkMode={isDarkMode} />
<ComfortablePricing bind:isDarkMode={isDarkMode} />
<ClientSreview bind:isDarkMode={isDarkMode}  />
<GetInTouch bind:isDarkMode={isDarkMode}  />
<Footer bind:isDarkMode={isDarkMode} />

<style>
  .home-container {
      color: var(--color-black);
      background-color: var(--color-silver);
      display: grid;
      grid-template-columns: 1fr;
      grid-template-rows: 1fr;
      place-items: center;
      margin: 100px 0 auto;
  }

  .home-container.dark {
      color: var(--color-white);
      background-color: var(--color-jet);
  }

  .row {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 2rem;
      max-width: 1280px;
      width: 100%;
      max-width: 1300px;
    width: 100%;
    padding: 0 2rem;
  }

  @media (max-width: 768px) {
      .row {
          grid-template-columns: 1fr;
      }
  }

  .right-column {
      background-color: var(--color-back);
      border-radius: 45px;
      padding: 20px;
      justify-content: center;
    display: flex;
  }

  .dark .right-column {
      background-color: var(--color-Myrtle-Green);
  }

  .top-section {
      background-color: var(--color-back);
      border-radius: 45px;
      color: var(--color-black);
      display: grid;
      place-items: center;
      text-align: center;
      padding: 2rem;
  }

  .home-container.dark .top-section {
      background-color: var(--color-Myrtle-Green);
      color: var(--color-silver);
  }

  .top-section h2 {
      font-size: 3rem;
      font-weight: 700;
      margin-bottom: 1rem;
      line-height: normal;
      text-align: left;
  }

  .top-section p {
      font-size: 1.25rem;
      margin-bottom: 2rem;
      text-align: left;
  }

  .bottom-section {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 1rem;
      margin-top: 2rem;
  }

  .image-container {
      background-color: var(--color-back);
      border-radius: 45px;
      overflow: hidden;
      justify-content: center;
    display: flex;
  }

  .dark .image-container {
      background-color: var(--color-Myrtle-Green);
  }

  .btn-primary {
      background-color: var(--color-turquoise);
      color: #F2FFFC;
      font-size: 1.5rem;
      padding: 5rem 2rem;
      border-radius: 45px;
      width: 100%;
  }

  .btn-primary i {
      margin-left: 10px;
  }

  .img-fluid {
      max-width: 70%;
      height: auto;
      margin: 0 auto;
  }
</style>
