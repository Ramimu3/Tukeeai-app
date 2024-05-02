<script>
  import { push } from 'svelte-spa-router';
  import googleLogo from './assets/google.svg';
  import facebookLogo from './assets/facebook.svg';
  import githubLogo from './assets/github.svg';
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();


  let username = '';
  let password = '';
  let errorMessage = '';

  async function handleSignIn() {
    try {
      const response = await fetch(`/api/login?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
        },
      });

      if (response.ok) {
        const data = await response.json();
        if (data.success) {
          // Sign-in successful, emit the login event with the user's name
          const loginEvent = { userName: username };
          dispatch('login', loginEvent);
          // Set a flag in localStorage to indicate successful login
          localStorage.setItem('loginSuccess', 'true');
          // Refresh the page
          window.location.reload();
        } else {
          errorMessage = data.message || 'Sign-in failed. Please try again.';
        }
      } else {
        const errorData = await response.json();
        console.error('Sign-in failed:', errorData);
        errorMessage = errorData.detail || 'Sign-in failed. Please try again.';
      }
    } catch (error) {
      console.error('Error:', error);
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

<div class="container mx-auto px-4 py-8">
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
    <button type="submit" class="bg-primary text-white px-6 py-3 rounded-lg font-bold">Sign In</button>
  </form>
  <p class="mt-4">Don't have an account? <a href="#/signup" class="text-primary">Sign Up</a></p>
</div>
<div class="social-signup">
  <a href="/accounts/google/login/?process=signup" class="btn btn-google">
    <img src="{googleLogo}" alt="Google Logo" class="logo">
  </a>
  <a href="/accounts/github/login/?process=signup" class="btn btn-github">
    <img src="{githubLogo}" alt="GitHub Logo" class="logo">
  </a>
  <a href="/accounts/facebook/login/?process=signup" class="btn btn-facebook">
    <img src="{facebookLogo}" alt="Facebook Logo" class="logo">
  </a>
</div>
<style>
  .social-signup {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
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
  
  