<script>
  import { onMount } from "svelte";

  import logo_dark from '../assets/Landing/Tukee-dark.svg';
  import logo_light from '../assets/Landing/Tukee-light.svg';

  let isDarkMode = false;
  let menu = false;

  onMount(async () => {
      window.addEventListener("scroll", windowScroll);
  });

  function windowScroll() {
      const navbar = document.getElementById("navbar");
      if (
          document.body.scrollTop >= 50 ||
          document.documentElement.scrollTop >= 50
      ) {
          if (navbar !== null) {
              navbar?.classList.add("is-sticky");
          }
      } else {
          if (navbar !== null) {
              navbar?.classList.remove("is-sticky");
          }
      }

      const mybutton = document.getElementById("back-to-top");
      if (mybutton != null) {
          if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
              mybutton.classList.add("flex");
              mybutton.classList.remove("hidden");
          } else {
              mybutton.classList.add("hidden");
              mybutton.classList.remove("flex");
          }
      }

      const sections = document.querySelectorAll("section");
      const navLi = document.querySelectorAll(".navbar ul.navbar-nav li > a");
      var current = "";

      sections.forEach((section) => {
          const sectionTop = section.offsetTop;
          if (pageYOffset >= sectionTop - 60) {
              current = section.getAttribute("id");
          }
      });

      navLi.forEach((li) => {
          li.classList.remove("active");
          if (li.classList.contains(current)) {
              li.classList.add("active");
          }
      });
  }

  function handleAnchorClick(event) {
      event.preventDefault();
      const link = event.currentTarget;
      const anchorId = new URL(link.href).hash.replace('#', '');
      const anchor = document.getElementById(anchorId);
      window.scrollTo({
          top: anchor.offsetTop,
          behavior: 'smooth'
      });
  }

  function toggleDarkMode() {
      isDarkMode = !isDarkMode;
  }
</script>

<nav class="navbar" id="navbar" class:dark={isDarkMode}>
  <div class="container flex flex-wrap items-center justify-end">
      <a class="navbar-brand md:me-8" href="/index">
          <img src={logo_dark} class:hidden={isDarkMode} alt="Dark Logo">
          <img src={logo_light} class:hidden={!isDarkMode} alt="Light Logo">
      </a>

      <div class="nav-icons flex items-center lg_992:order-2 ms-auto lg:ms-4">
          <ul class="list-none menu-social mb-0">
              <li class="inline">
                  <a href="/login" class="h-9 w-9 inline-flex items-center text-center justify-center text-base font-normal tracking-wide border align-middle transition duration-500 ease-in-out rounded-full bg-violet-600 hover:bg-violet-700 border-violet-600 hover:border-violet-700 text-white">
                      <i class="uil uil-user"></i>
                  </a>
              </li>
          </ul>

          <button on:click={toggleDarkMode} class="inline-flex items-center ms-3 text-slate-950 dark:text-white lg_992:hidden">
              {#if isDarkMode}
                  <i class="uil uil-sun text-[24px]"></i>
              {:else}
                  <i class="uil uil-moon text-[24px]"></i>
              {/if}
          </button>

          <button data-collapse="menu-collapse" type="button" on:click={() => menu = !menu} class="collapse-btn inline-flex items-center ms-3 text-slate-950 dark:text-white lg_992:hidden" aria-controls="menu-collapse" aria-expanded="false">
              <span class="sr-only">Navigation Menu</span>
              <i class="mdi mdi-menu text-[24px]"></i>
          </button>
      </div>

      <div class={`${menu === false ? "hidden" : "block"} navigation lg_992:order-1 lg_992:flex mx-auto`} id="menu-collapse">
          <ul class="navbar-nav nav-light" id="navbar-navlist">
              <li class="nav-item">
                  <a href="#home" on:click={handleAnchorClick} spy={true} smooth={true} duration={500} class="nav-link active home">Home</a>
              </li>
              <li class="nav-item">
                  <a href="#features" on:click={handleAnchorClick} spy={true} smooth={true} duration={500} class="nav-link features">Services</a>
              </li>
              <li class="nav-item">
                  <a href="#pricing" on:click={handleAnchorClick} spy={true} smooth={true} duration={500} class="nav-link pricing">Pricing</a>
              </li>
              <li class="nav-item">
                  <a href="#testi" on:click={handleAnchorClick} spy={true} smooth={true} duration={500} class="nav-link testi">Review</a>
              </li>
              <li class="nav-item">
                  <a href="#blog" on:click={handleAnchorClick} spy={true} smooth={true} duration={500} class="nav-link blog">Blog</a>
              </li>
              <li class="nav-item">
                  <a href="#contact" on:click={handleAnchorClick} spy={true} smooth={true} duration={500} class="nav-link contact">Contact us</a>
              </li>
          </ul>
      </div>
  </div>
</nav>
