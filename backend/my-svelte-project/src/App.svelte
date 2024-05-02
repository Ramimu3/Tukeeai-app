<script>
  import Router from 'svelte-spa-router';
  import { link, push } from 'svelte-spa-router';
  import { onMount } from 'svelte';
  import Landing from './Landing.svelte';
  import SignIn from './SignIn.svelte';
  import SignUp from './SignUp.svelte';
  import Dashboard from './Dashboard.svelte';
  import UserPayment from './UserPayment.svelte';
  import Success from './Success.svelte';
  import Cancel from './Cancel.svelte';
  import axios from 'axios';
  import './global.css';


  const routes = {
    '/': Landing,
    '/signin': SignIn,
    '/signup': SignUp,
    '/dashboard': Dashboard,
    '/dashboard/files': Dashboard,
    '/dashboard/settings': Dashboard,
    '/dashboard/support': Dashboard,
    '/user-payment': UserPayment,
    '/success': Success,
    '/cancel': Cancel,
  };

  let isLoggedIn = false;
  let userName = '';
  let isDropdownOpen = false;
  let csrfToken = '';

  onMount(async () => {
    // Check if the user is already logged in
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

  async function handleCheckout() {
    try {
    const response = await fetch('http://localhost:8000/stripe/api/create-checkout-session/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (response.ok) {
      const data = await response.json();
      window.location.href = data.checkout_url;
    } else {
      console.error('Error creating checkout session');
    }
  } catch (error) {
    console.error('Error:', error);
  }
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

<main>
  <Router {routes} on:login={handleLogin} />
</main>

