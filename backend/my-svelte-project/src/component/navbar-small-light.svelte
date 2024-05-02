<script>
    import { onMount } from "svelte";

    import logo_dark from '../assets/Landing/Tukee-light.svg';
    import logo_light from '../assets/Landing/Tukee-dark.svg';

    let isMobileMenuOpen = false;
    export let isDarkMode = false;
    let isNavbarVisible = true;
    let lastScrollPosition = 0;
    let isLoggedIn = false;
  let userName = '';
  let isDropdownOpen = false;
  let csrfToken = '';
    onMount(async () => {
        window.addEventListener("scroll", handleScroll);
        try {
      const response = await fetch('/api/check-login/');
      if (response.ok) {
        const data = await response.json();
        isLoggedIn = data.isLoggedIn;
        userName = data.userName;
        // Check if the login was successful
        const loginSuccess = localStorage.getItem('loginSuccess');
        if (loginSuccess === 'true') {
          // Navigate to the dashboard route
          push('/dashboard');
          // Remove the loginSuccess flag from localStorage
          localStorage.removeItem('loginSuccess');
        }
      }
    } catch (error) {
      console.error('Error checking login status:', error);
    }
  try {
      const response = await axios.get('/api/csrf-token/');
      csrfToken = response.data.csrfToken;
    } catch (err) {
      console.error('Error fetching CSRF token:', err);
    }
  });

  function handleLogin(event) {
    console.log('Received login event:', event.detail); // Add this line
    isLoggedIn = true;
    userName = event.detail.userName;
    console.log('Updated isLoggedIn:', isLoggedIn); // Add this line
    console.log('Updated userName:', userName); // Add this line
  }

  async function handleLogout() {
    try {
      const response = await fetch('/api/logout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
        },
      });

      if (response.ok) {
        isLoggedIn = false;
        userName = '';
        window.location.href = '/'; // Redirect to the home page
      } else {
        console.error('Logout failed:', response.statusText);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  function toggleDropdown() {
    isDropdownOpen = !isDropdownOpen;
  }

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + '=') {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
$: {
    // Reactive statement to update the UI when isLoggedIn or userName changes
    if (isLoggedIn) {
      // Perform any necessary actions when the user is logged in
      console.log('User is logged in:', userName);
    } else {
      // Perform any necessary actions when the user is logged out
      console.log('User is logged out');
    }
  }

    function handleScroll() {
        const currentScrollPosition = window.scrollY;

        if (currentScrollPosition > lastScrollPosition) {
            // Scrolling down
            isNavbarVisible = false;
        } else {
            // Scrolling up
            isNavbarVisible = true;
        }

        lastScrollPosition = currentScrollPosition;
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

    function toggleMobileMenu() {
        isMobileMenuOpen = !isMobileMenuOpen;
    }

    function toggleDarkMode() {
        isDarkMode = !isDarkMode;
        if (isDarkMode) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    }
</script>

<nav class="nav" class:dark={isDarkMode} class:hidden={!isNavbarVisible}>
    <div class="logo">
        <a href="#home">
            <img class="light-logo" src={logo_light} alt="Light Logo">
            <img class="dark-logo" src={logo_dark} alt="Dark Logo">
        </a>
    </div>
    <button class="menu-icon" class:open={isMobileMenuOpen} on:click={toggleMobileMenu}>
      <span></span>
      <span></span>
    </button>
    <ul class="nav-links" class:open={isMobileMenuOpen}>
        <li><a href="#home" on:click={handleAnchorClick}>Home</a></li>
        <li><a href="#features" on:click={handleAnchorClick}>Services</a></li>
        <li><a href="#pricing" on:click={handleAnchorClick}>Pricing</a></li>
        <li><a href="#contact" on:click={handleAnchorClick}>Contact us</a></li>
    </ul>
    <div class="navbar-actions">
        <!-- Dark mode toggle -->
        <button type="button" class="navbar-dark-mode-toggle" on:click={toggleDarkMode}>
          <span class="sr-only">Toggle dark mode</span>
          <svg class={`navbar-icon ${isDarkMode ? 'hidden' : 'block'}`} fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
          </svg>
          <svg class={`navbar-icon ${isDarkMode ? 'block' : 'hidden'}`} fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.718 9.718 0 0118 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 003 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 009.002-5.998z" />
          </svg>
        </button>
      
        <!-- Profile dropdown -->
        {#if isLoggedIn}
          <div class="navbar-profile-dropdown">
            <button type="button" class="navbar-profile-button" on:click={toggleDropdown}>
              <span class="sr-only">Open user menu</span>
              <img class="navbar-profile-image" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
            </button>
            {#if isDropdownOpen}
              <div class="navbar-dropdown-menu">
                <a href="/account-settings" class="navbar-dropdown-item">Account Settings</a>
                <button type="button" class="navbar-dropdown-item" on:click={handleLogout}>Logout</button>
              </div>
            {/if}
          </div>
        {:else}
          <a href="/#/signup" class="navbar-signup-link">Sign Up</a>
        {/if}
      </div>
</nav>

<style>
    @import url('https://fonts.googleapis.com/css?family=Quicksand:400,500,700');

    .nav {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 80px;
        background-color: var(--color-silver);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 clamp(0.625rem, -11.786rem + 33.095vw, 18rem);        z-index: 999;
        transition: transform 0.3s ease-in-out;
    }

    :global(.dark) .nav {
    background-color: var(--color-jet);
    color: #fff;
}

    .nav.hidden {
        transform: translateY(-100%);
    }

    .logo {
        font-size: 24px;
        font-weight: bold;
        color: #333;
        text-decoration: none;
    }

    .light-logo,
    .dark-logo {
        height: 130px;
        }

    .light-logo {
    display: block;
}

.dark-logo {
    display: none;
}

:global(.dark) .light-logo {
    display: none;
}

:global(.dark) .dark-logo {
    display: block;
}

    .menu-icon {
        display: none;
        cursor: pointer;
    }

    .menu-icon span {
        display: block;
        width: 25px;
        height: 3px;
        background-color: #333;
        margin: 5px;
        transition: transform 0.3s ease-in-out;
    }

    .nav-links {
        display: flex;
        justify-content: space-around;
        align-items: center;
        width: 40%;
        list-style: none;
        margin: 0;
        padding: 0;
    }

    .nav-links li {
        margin: 0 10px;
    }

    .nav-links a {
        color: #333;
        text-decoration: none;
        font-size: 18px;
        font-weight: bold;
        transition: color 0.3s ease-in-out;
    }

    .nav-links a:hover {
        color: var(--color-turquoise);
    }

    .navbar-actions {
        display: flex;
        align-items: center;
    }

    :global(.dark) .nav-links a {
    color: var(--color-silver);
}

:global(.dark) .nav-links a:hover {
    color: var(--color-turquoise);
}

    .navbar-dark-mode-toggle {
        padding: 0.25rem;
        border-radius: 9999px;
        background-color: #1f2937;
        color: #9ca3af;
        margin-right: 10px;
    }

    .navbar-dark-mode-toggle:hover {
        color: #fff;
    }

    .navbar-dark-mode-toggle:focus {
        outline: none;
        box-shadow: 0 0 0 2px #fff, 0 0 0 4px #1f2937;
    }

    .navbar-profile-dropdown {
        position: relative;
    }

    .navbar-profile-button {
        display: flex;
        align-items: center;
        padding: 0.25rem;
        border-radius: 9999px;
        background-color: #1f2937;
        color: #fff;
    }

    .navbar-profile-button:focus {
        outline: none;
        box-shadow: 0 0 0 2px #fff, 0 0 0 4px #1f2937;
    }

    .navbar-profile-image {
        width: 2rem;
        height: 2rem;
        border-radius: 9999px;
    }

    @media screen and (max-width: 768px) {
        .menu-icon {
            display: block;
        }

        .nav-links {
            position: absolute;
            top: 80px;
            left: 0;
            width: 100%;
            height: calc(100vh - 80px);
            background-color: var(--color-silver);            flex-direction: column;
            justify-content: center;
            align-items: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease-in-out;
        }

        .nav-links.open {
            opacity: 1;
            pointer-events: auto;
        }

        .nav-links li {
            margin: 20px 0;
        }

        .menu-icon.open span:nth-child(1) {
            transform: translateY(8px) rotate(45deg);
        }

        .menu-icon.open span:nth-child(2) {
            opacity: 0;
        }

        .menu-icon.open span:nth-child(3) {
            transform: translateY(-8px) rotate(-45deg);
        }
    }
</style>
