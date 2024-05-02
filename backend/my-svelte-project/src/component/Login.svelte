<script>
    import { onMount } from 'svelte';
    let username = '';
    let password = '';
  
    async function loginUser() {
      const response = await fetch('http://localhost:8000/api/token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });
  
      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('access_token', data.access);
        // Optionally store the refresh token as well
        localStorage.setItem('refresh_token', data.refresh);
        console.log('Login successful');
        // Redirect or perform additional actions after login
      } else {
        console.error('Login failed');
      }
    }
  </script>
  
  <form on:submit|preventDefault={loginUser}>
    <input type="text" bind:value={username} placeholder="Username" />
    <input type="password" bind:value={password} placeholder="Password" />
    <button type="submit">Login</button>
  </form>
  