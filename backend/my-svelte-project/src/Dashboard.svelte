<!-- Dashboard.svelte -->
<script>
  import { onMount, onDestroy } from 'svelte';
  import { AppBar } from '@skeletonlabs/skeleton';
  import Home from './Home.svelte';
  import Files from './Files.svelte';
  import Settings from './Settings.svelte';
  import Support from './Support.svelte';
  import { fly } from 'svelte/transition';
  import { scale } from 'svelte/transition';
  import infinityIcon from './assets/infinity.svg';
  import customizeIcon from './assets/customize-icon.svg';
  import dashboardIcon from './assets/dashboard.svg';
  import supportIcon from './assets/support.svg';
  import logo_dark from './assets/Landing/Tukee-light.svg';
  import logo_light from './assets/Landing/Tukee-dark.svg';
  import HomeIcon from './assets/Dashboardicons/home-icon.svg';
  import FilesIcon from './assets/Dashboardicons/files-icon.svg';
  import SettingsIcon from './assets/Dashboardicons/settings-icon.svg';
  import HelpIcon from './assets/Dashboardicons/help-icon.svg';
  import HomeIconlight from './assets/Dashboardicons/home-icon-light.svg';
  import FilesIconlight from './assets/Dashboardicons/files-icon-light.svg';
  import SettingsIconlight from './assets/Dashboardicons/settings-icon-light.svg';
  import HelpIconlight from './assets/Dashboardicons/help-icon-light.svg';
  
  export let currentRoute = '';
  let isSidebarOpen = false;
  let isPopupOpen = false;
  let isLoggedIn = false;
  let userName = '';
  let isDropdownOpen = false;
  let csrfToken = '';
  let isDarkMode = false;

  function toggleDarkMode() {
        isDarkMode = !isDarkMode;
        if (isDarkMode) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    }

  function navigateTo(route) {
    window.history.pushState({}, '', `#${route}`);
    currentRoute = route;
    isSidebarOpen = false;
  }

  function toggleSidebar() {
    isSidebarOpen = !isSidebarOpen;
  }

  function handleOutsideClick(event) {
    if (isSidebarOpen && !event.target.closest('.sidebar') && !event.target.closest('.hamburger-menu')) {
      isSidebarOpen = false;
    }
  }

  onMount(async () => {
    const sidebar = document.getElementById('sidebar');
    const nanoContent = sidebar.querySelector('.nano-content');

    const updateSidebarHeight = () => {
      const windowHeight = window.innerHeight;
      const appBarHeight = document.querySelector('.app-bar').offsetHeight;
      const sidebarHeight = windowHeight - appBarHeight;
      sidebar.style.height = `${sidebarHeight}px`;
      nanoContent.style.height = `${sidebarHeight}px`;
    };

    updateSidebarHeight();
    window.addEventListener('resize', updateSidebarHeight);

    // Handle initial route based on URL hash
    const initialRoute = window.location.hash.slice(1) || '/dashboard';
    currentRoute = initialRoute;

    // Handle hash change event
    window.addEventListener('hashchange', () => {
      const newRoute = window.location.hash.slice(1);
      currentRoute = newRoute;
    });

    // Check if the user is already logged in
    try {
      const response = await fetch('/api/check-login/');
      if (response.ok) {
        const data = await response.json();
        isLoggedIn = data.isLoggedIn;
        userName = data.userName;
      }
    } catch (error) {
      console.error('Error checking login status:', error);
    }

    return () => {
      window.removeEventListener('resize', updateSidebarHeight);
    };
  });

  function openPopup() {
    isPopupOpen = true;
  }

  function closePopup(event) {
    if (event.target.classList.contains('close-btn') || event.key === 'Escape') {
      isPopupOpen = false;
    }
  }

  function handleKeyDown(event) {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      event.target.click();
    }
  }

  function toggleDropdown() {
    isDropdownOpen = !isDropdownOpen;
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
</script>


<svelte:window on:click={handleOutsideClick} />

<div class="app-container">
  <AppBar class="appbar-main">
    <div class="appbar">
    <div class="appbar-content">
      <div class="appbar-left">
        <button class="hamburger-menu" on:click={toggleSidebar}>&#9776;</button>
        {#if currentRoute === '/dashboard'}
          <h1 class="text-2xl font-bold">My Dashboard</h1>
        {:else if currentRoute === '/dashboard/files'}
          <h1 class="text-2xl font-bold">Files</h1>
        {:else if currentRoute === '/dashboard/settings'}
          <h1 class="text-2xl font-bold">Account Settings</h1>
        {:else if currentRoute === '/dashboard/support'}
          <h1 class="text-2xl font-bold">Support</h1>
        {/if}
      </div>
      <div class="appbar-right">
        <div class="appbar-actions">
          <button class="theme-toggle" on:click={toggleDarkMode}>
            {#if isDarkMode}
              <svg class="theme-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
              </svg>
            {:else}
              <svg class="theme-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="5"></circle>
                <line x1="12" y1="1" x2="12" y2="3"></line>
                <line x1="12" y1="21" x2="12" y2="23"></line>
                <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                <line x1="1" y1="12" x2="3" y2="12"></line>
                <line x1="21" y1="12" x2="23" y2="12"></line>
                <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
              </svg>
            {/if}
          </button>
  
          {#if isLoggedIn}
            <div class="profile-dropdown">
              <button class="profile-button" on:click={toggleDropdown}>
                <img class="profile-image" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="Profile" />
              </button>
              {#if isDropdownOpen}
                <div class="dropdown-menu">
                  <a href="/account-settings" class="dropdown-item">Account Settings</a>
                  <button class="dropdown-item" on:click={handleLogout}>Logout</button>
                </div>
              {/if}
            </div>
          {:else}
            <a href="/#/signup" class="signup-link">Sign Up</a>
          {/if}
        </div>
      </div>
    </div>
  </AppBar>
  
  

  <div class="content-container" class:dark={isDarkMode}>
    <aside id="sidebar" class="nano" class:open={isSidebarOpen} transition:fly={{ x: -200, duration: 300 }}>
      <div class="nano-content">
        <div class="logo">
          <a href="#home">
              <img class="light-logo" src="/static/build/assets/Tukee-dark.svg" alt="Light Logo">
              <img class="dark-logo" src="/static/build/assets/Tukee-light.svg" alt="Dark Logo">
          </a>
      </div>
        
        <nav>
          <ul class="space-y-2">
            <li>
              <button class="btn variant-filled" on:click={() => navigateTo('/dashboard')}>
                <div class="dash-menu-btn-icon">
                  {#if isDarkMode}
                  <img src={HomeIconlight} alt="Home" width="30" height="30" />
                {:else}
                  <img src={HomeIcon} alt="Home" width="30" height="30" />
                {/if}
              </div>
              Home
            </button>
          </li>
          <li>
            <button class="btn variant-filled" on:click={() => navigateTo('/dashboard/files')}>
              <div class="dash-menu-btn-icon">
                {#if isDarkMode}
                  <img src={FilesIconlight} alt="Files" width="30" height="30" />
                {:else}
                  <img src={FilesIcon} alt="Files" width="30" height="30" />
                {/if}
              </div>
              Files
            </button>
          </li>
          <li>
            <button class="btn variant-filled" on:click={() => navigateTo('/dashboard/settings')}>
              <div class="dash-menu-btn-icon">
                {#if isDarkMode}
                  <img src={SettingsIconlight} alt="Settings" width="30" height="30" />
                {:else}
                  <img src={SettingsIcon} alt="Settings" width="30" height="30" />
                {/if}
              </div>
              Settings
            </button>
          </li>
          <li>
            <button class="btn variant-filled" on:click={() => navigateTo('/dashboard/support')}>
              <div class="dash-menu-btn-icon">
                {#if isDarkMode}
                  <img src={HelpIconlight} alt="Support" width="30" height="30" />
                {:else}
                  <img src={HelpIcon} alt="Support" width="30" height="30" />
                {/if}
              </div>
              Support
              </button>
            </li>
          </ul>
          
          <div class="try-pro-section mt-4">
            <h3 class="text-lg font-bold mb-2">Try Pro</h3>
            <p class="text-sm mb-4">Upgrade for unlimited uploads, smarter AI, and custom data.</p>
            <button class="btn variant-filled" on:click={openPopup} on:keydown={handleKeyDown}>Learn More</button>
          </div>
        </nav>
      </div>
    </aside>
  
    {#if isPopupOpen}
      <button class="popup-overlay" on:click={closePopup} on:keydown={handleKeyDown} aria-label="Close Popup">
        <dialog class="popup" open transition:scale={{ start: 0.8, duration: 300 }}>
          <div class="popup-content">
            <button class="close-btn" on:click={closePopup} on:keydown={handleKeyDown} aria-label="Close">&times;</button>
            <h2 class="text-2xl font-bold mb-6 text-center">Tukee Pro</h2>
            <div class="feature-grid">
              <div class="feature-item">
                <img src={infinityIcon} alt="Unlimited Pro Search" class="feature-icon">
                <h3 class="text-lg font-bold mb-2">Unlimited Data Conversion</h3>
                <p class="mb-2">Perform unlimited searches with advanced features.</p>
              </div>
              <div class="feature-item">
                <img src={customizeIcon} alt="Unlimited File Uploads" class="feature-icon">
                <h3 class="text-lg font-bold mb-2">Advanced Data Cleansing Tools</h3>
                <p class="mb-2">Upload and store unlimited files securely.</p>
              </div>
              <div class="feature-item">
                <img src={dashboardIcon} alt="Upgraded AI Models" class="feature-icon">
                <h3 class="text-lg font-bold mb-2">Data Integration Capabilities
                </h3>
                <p class="mb-2">Access advanced AI models for enhanced performance.</p>
              </div>
              <div class="feature-item">
                <img src={supportIcon} alt="API Credits" class="feature-icon">
                <h3 class="text-lg font-bold mb-2">Priority Support
                </h3>
                <p class="mb-2">Get additional API credits for seamless integration.</p>
              </div>
            </div>
            <div class="pricing-options">
              <div class="pricing-item">
                <h3 class="text-lg font-bold mb-2">Monthly</h3>
                <p class="mb-4">$9 billed per month</p>
                <button class="btn variant-filled" on:click={closePopup} on:keydown={handleKeyDown}>Get Started</button>
              </div>
              <div class="pricing-item">
                <h3 class="text-lg font-bold mb-2">Yearly</h3>
                <p class="mb-4">$99 billed per year</p>
                <button class="btn variant-filled" on:click={closePopup} on:keydown={handleKeyDown}>Get Started</button>
              </div>
            </div>
          </div>
        </dialog>
      </button>
    {/if}

    <main class="main-content p-4 overflow-auto">
      <div class="content-wrapper">
        {#if currentRoute === '/dashboard'}
      <Home {isDarkMode} />
    {:else if currentRoute === '/dashboard/files'}
      <Files {isDarkMode} />
    {:else if currentRoute === '/dashboard/settings'}
      <Settings {isDarkMode} />
    {:else if currentRoute === '/dashboard/support'}
      <Support {isDarkMode} />
    {/if}
      </div>
    </main>
  </div>

  <footer class="footer bg-base-200 text-base-content text-center py-4">
    <p>&copy; 2023 My Dashboard. All rights reserved.</p>
  </footer>
</div>




<style>
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
.appbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px;
}

.appbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.appbar-left {
  display: flex;
  align-items: center;
}

.appbar-right {
  display: flex;
  align-items: center;
}

.appbar-actions {
  display: flex;
  align-items: center;
}

.hamburger-menu {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  margin-right: 16px;
}

.theme-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  cursor: pointer;
  margin-right: 16px;
}

.theme-icon {
  width: 24px;
  height: 24px;
}

.profile-dropdown {
  position: relative;
}

.profile-button {
  display: flex;
  align-items: center;
  background: none;
  border: none;
  cursor: pointer;
}

.profile-image {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  min-width: 150px;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 8px 0;
  z-index: 10;
}

.dropdown-item {
  display: block;
  padding: 8px 16px;
  color: #333;
  text-decoration: none;
  cursor: pointer;
}

.dropdown-item:hover {
  background-color: #f5f5f5;
}

.signup-link {
    padding: 8px 16px;
    background-color: var(--color-turquoise);
    color: var(--color-jet);
    text-decoration: none;
    border-radius: 4px;
}


  .app-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
  }

  .content-container {
    display: flex;
    flex-grow: 1;
  }

  #sidebar {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%!important;
    width: 200px;
    background: var(--color-back);
    transition-duration: .3s;
    z-index: 5;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  }
  .dark #sidebar {
    background: var(--color-Myrtle-Green);
  }
  #sidebar .nano-content {
    padding: 20px;
  }

  .logo {
    max-width: 100%;
    max-height: 100%;
  }

  .main-content {
    flex-grow: 1;
    overflow-y: auto;
  }

  .content-wrapper {
    max-width: 1200px;
    margin: 0 auto;
  }

  button.btn.variant-filled {
    background-color: var(--color-back);
    border: 1px solid var(--color-back);
    width: 8rem;
    border-radius: 13px;
    padding: 0.3rem 0.9rem;
    margin: 0.5rem auto;
    display: flex;
    justify-content: flex-start;
    color: var(--color-jet);
}

button.btn.variant-filled:hover {
background-color: var(--color-border);
}


.dark button.btn.variant-filled {
  background-color: var(--color-Myrtle-Green);
  color: var(--color-silver);
  border: 1px solid var(--color-Myrtle-Green);

}
  .hamburger-menu {
    display: none;
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    margin-right: 10px;
  }
  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9998;
    border: none;
    padding: 0;
    margin: 0;
    cursor: pointer;
  }
  .popup {
    position: fixed;
    top: 50%;
    left: 35%;
    transform: translate(-50%, -50%);
    width: 80%;
    max-width: 600px;
    background-color: var(--color-Myrtle-Green);
    border-radius: 20px;
    text-align: center;
    padding: 0.4rem;
    border: none;
    z-index: 9999;
  }

  .popup::backdrop {
    background-color: rgba(0, 0, 0, 0.5);
  }

  .popup-content {
    background-color: var(--color-back);
    color: var(--color-black);
    padding: 2rem;
    border-radius: 20px;
    max-width: 600px;
    text-align: center;
    position: relative;
  }

  .close-btn {
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 1.5rem;
    background: none;
    border: none;
    color: #3c7e92;
    cursor: pointer;
  }
  li {
    align-items: self-start;
    display: flex;
  }
  .dash-menu-btn-icon{
    width: 30%;
    margin-right: 0.5rem;
  }

  .feature-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
    margin-bottom: 2rem;
  }

  .feature-item {
    text-align: center;
  }

  .feature-icon {
    width: 100%;
    height: 50px;
    margin-bottom: 1rem;
  }

  .pricing-options {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
    justify-items: center;
    align-items: start;
  }

  .pricing-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .pricing-item p {
    margin-bottom: 1rem;
  }

  .pricing-item .btn {
    margin-top: auto;
  }

  .mt-4 {
    margin-top: 20rem;
}


  @media (max-width: 768px) {
    #sidebar {    
    position: fixed;
    height: 100%!important;
    top: 0px;
    left: 0;
    bottom: 0;
    width: 200px;
    transform: translate(-200px);
    transition: transform .3s ease-in-out;
    margin-left: 0px;
}
    #sidebar.open {
      transform: translateX(0);
    }

    .hamburger-menu {
      display: block;
    }

    .content-wrapper {
      max-width: 100%;
      padding: 0 20px;
    }
  }
</style>
