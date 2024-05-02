<script>
  import { onMount, createEventDispatcher } from 'svelte';
  import axios from 'axios';

  const dispatch = createEventDispatcher();

  let userPayment = null;
  let error = null;

  onMount(async () => {
    try {
      const response = await axios.get('/stripe/api/user-payment/');
      userPayment = response.data;
      console.log('User payment data:', userPayment);
    } catch (err) {
      error = err.message;
      console.error('Error fetching user payment:', err);
    }
  });

  function handleCheckout() {
    dispatch('checkout');
  }
</script>

<div>
  {#if error}
    <p>Error: {error}</p>
  {:else if userPayment}
    <p>User Payment ID: {userPayment.id}</p>
    <p>Stripe Checkout ID: {userPayment.stripe_checkout_id}</p>
    <!-- Display other relevant fields -->
    <button on:click={handleCheckout}>Proceed to Checkout</button>
  {:else}
    <p>Loading user payment...</p>
  {/if}
</div>
