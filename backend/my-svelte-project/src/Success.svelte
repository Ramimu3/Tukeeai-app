<!-- Success.svelte -->
<script>
  import { onMount } from 'svelte';

  let sessionId = '';

  onMount(() => {
    const hash = window.location.hash.substring(1);
    const urlParams = new URLSearchParams(hash.split('?')[1]);
    sessionId = urlParams.get('session_id');
  });
</script>

<h1>Payment Successful</h1>
<p>Thank you for your payment!</p>
<p>Session ID: {sessionId}</p>
