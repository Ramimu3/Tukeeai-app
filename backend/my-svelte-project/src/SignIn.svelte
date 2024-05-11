<script>
  import { push } from 'svelte-spa-router';
  import googleLogo from './assets/google.svg';
  import facebookLogo from './assets/facebook.svg';
  import githubLogo from './assets/github.svg';
  import { createEventDispatcher } from 'svelte';
  import { onMount, onDestroy } from 'svelte';
  import { navigate } from 'svelte-routing';


  const dispatch = createEventDispatcher();
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
  

  let username = '';
  let password = '';
  let errorMessage = '';

  async function handleSignIn() {
  try {
    console.log('Sending sign-in request...'); // Log before sending the request
    const response = await fetch(`/api/login?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
      },
    });

    console.log('Sign-in response received:', response); // Log the response object
    if (response.ok) {
      const data = await response.json();
      console.log('Sign-in response data:', data); // Log the response data
      if (data.success) {
        console.log('Sign-in successful'); // Log success message
        // Sign-in successful, emit the login event with the user's name
        const loginEvent = { userName: username };
        dispatch('login', loginEvent);
        // Set a flag in localStorage to indicate successful login
        localStorage.setItem('loginSuccess', 'true');
        // Navigate to the dashboard page using window.location.href
        console.log('Redirecting to dashboard'); // Log the redirection attempt
        window.location.href = '/#/dashboard';
      } else {
        console.log('Sign-in failed:', data.message); // Log the failure message
        errorMessage = data.message || 'Sign-in failed. Please try again.';
      }
    } else {
      const errorData = await response.json();
      console.error('Sign-in request failed:', errorData); // Log the error data
      errorMessage = errorData.detail || 'Sign-in failed. Please try again.';
    }
  } catch (error) {
    console.error('Error during sign-in:', error); // Log any errors
    errorMessage = 'An error occurred. Please try again later.';
  }
}





  // Helper function to get the CSRF token from the cookie
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

<div class="container">
  <div class="form-container">
    <h2 class="text-2xl font-bold mb-4">Sign In</h2>
    {#if errorMessage}
      <p class="text-red-500 mb-4">{errorMessage}</p>
    {/if}
    <form on:submit|preventDefault={handleSignIn}>
      <div class="mb-4">
        <label for="username" class="block mb-2">Username</label>
        <input type="text" id="username" class="w-full px-3 py-2 border border-gray-300 rounded-lg" bind:value={username} required>
      </div>
      <div class="mb-4">
        <label for="password" class="block mb-2">Password</label>
        <input type="password" id="password" class="w-full px-3 py-2 border border-gray-300 rounded-lg" bind:value={password} required>
      </div>
      <button type="submit" class="sign-in-btn">Sign In</button>
    </form>
    <div class="mt-4 text-center">
      <a href="/accounts/password/reset/" class="text-primary">Forgot Password?</a>
    </div>
    <p class="mt-4 text-center">Don't have an account? <a href="#/signup" class="text-primary">Sign Up</a></p>
<div class="social-signup">
  <a href="/accounts/google/login/?process=signup&next=/#/dashboard" class="btn btn-google">
    <img src="{googleLogo}" alt="Google Logo" class="logo">
  </a>
  <a href="/accounts/github/login/?process=signup&next=/#/dashboard" class="btn btn-github">
    <img src="{githubLogo}" alt="GitHub Logo" class="logo">
  </a>
  <a href="/accounts/facebook/login/?process=signup&next=/#/dashboard" class="btn btn-facebook">
    <img src="{facebookLogo}" alt="Facebook Logo" class="logo">
  </a>
</div>
</div>
</div>

<style>
    .container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    max-width: 100%;
  }

  .form-container {
    width: clamp(18rem, calc(45.3333vw + 6.6667rem), 35rem);
    background-color: var(--color-back);
    padding: 30px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .social-signup {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
  }
  
  .sign-in-btn{
    background-color: var(--color-turquoise);
    transition: 0.3s ease;
  }

  .sign-in-btn:hover{
    background-color: var(--color-turquoise-hover);
  }
  .btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 200px;
    height: 50px;
    border-radius: 5px;
    color: #fff;
    font-size: 16px;
    text-decoration: none;
    transition: background-color 0.3s ease;
  }
  
  .logo {
    width: 20px;
    height: 20px;
    margin-right: 10px;
  }
  
  .btn-google {
    background-color: #fff;
    color: #757575;
    border: 1px solid #ddd;
  }
  
  .btn-google:hover {
    color: #fff;
    border-color: #4285f4;
  }
  
  .btn-github {
    background-color: #fff;
    color: #333;
    border: 1px solid #ddd;
  }
  
  .btn-github:hover {
    color: #fff;
    border-color: #333;
  }
  
  .btn-facebook {
    background-color: #fff;
    color: #3b5998;
    border: 1px solid #ddd;
  }
  
  .btn-facebook:hover {
    color: #fff;
    border-color: #3b5998;
  }
  </style>
  
  