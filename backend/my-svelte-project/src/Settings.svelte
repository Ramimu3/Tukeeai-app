<script lang="ts">
  let activeTab = 'general';

  function switchTab(tab: string) {
    activeTab = tab;
  }

  interface ImageProps {
    src: string;
    alt: string;
  }
  export let isDarkMode;

</script>

<style>
  main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    max-width: 1190px;
    margin: 0 auto;
  }

  header {
    width: 100%;
    padding: 1.5rem;
  }

  nav {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    margin-top: 1rem;
  }

  button {
    font-size: 0.875rem;
    font-weight: medium;
    padding: 0.5rem 1rem;
    border-radius: 0.375rem;
    margin-right: 1rem;
  }

  .active {
    color: var(--color-jet);
  }

  .dark .active {
    color: var(--color-silver);
  }

  .inactive {
    color: #8eabab;
  }

  .dark .inactive {
    color: #324f4f;
  }

  section {
    width: 100%;
    display: grid;
    padding: 1.5rem;
    grid-template-columns: 2fr 1fr;
  }

  article {
    background-color: var(--color-back);
    border-radius: 20px;
    padding: 1.5rem;
    border-color: var(--color-border);
    margin: 1rem;
    border-width: 2px;
    justify-content: center;
    display: grid;
    align-items: center;
    align-content: center;
  }
.dark article {
  background-color: var(--color-Myrtle-Green);
}
  h2 {
    font-size: 1.25rem;
    font-weight: bold;
    color: var(--color-jet);
    margin-bottom: 1rem;
  }
.dark h2 {
  color: var(--color-silver);
}

  .profile-details {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  .profile-row {
    display: flex;
    align-items: center;
    gap: 1.5rem;
  }

  .profile-photo {
    flex-shrink: 0;
  }

  .profile-photo img {
    width: 8rem;
    height: 8rem;
    border-radius: 50%;
    object-fit: cover;
  }

  .photo-actions {
    display: flex;
    gap: 1rem;
  }

  .profile-info {
    display: flex;
    gap: 1.5rem;
    margin-top: 1.5rem;
  }

  .profile-info div {
    flex: 1;
  }

  

  .profile-photo {
    flex-shrink: 0;
  }

  .profile-photo img {
    width: 8rem;
    height: 8rem;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 1rem;
  }

  .photo-actions {
    display: flex;
    align-items: center;
  }

  .photo-actions button {
    margin-bottom: 0.5rem;
  }

  .profile-info {
    flex-grow: 1;
  }

  .profile-info label {
    display: block;
    font-size: 0.875rem;
    font-weight: medium;
    color: #374151;
  }

  .profile-info input {
    padding: 8px;
    width: 300px;
    border: 2px solid var(--color-back);
    border-radius: 7px;
    background-color: var(--color-border);
  }

  .text-gray-700 {
    color: #374151;
  }
.dark .text-gray-700 {
  color: var(--color-silver);
}
  .mb-4 {
    margin-bottom: 1rem;
  }

  .bg-blue-500 {
    background-color: var(--color-turquoise);
    color: #EEFDFF;
  }

  .bg-red-500 {
    background-color: #EEABAB;
    color: #2A3839;
  }

  .px-4 {
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .py-2 {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
  }

  .rounded-md {
    border-radius: 0.375rem;
  }

  .mr-4 {
    margin-right: 1rem;
  }

  .flex {
    display: flex;
  }

  .justify-start {
    justify-content: flex-start;
  }

  .mt-4 {
    margin-top: 1rem;
  }

  .space-y-2 > * + * {
    margin-top: 0.5rem;
  }

  .list-disc {
    list-style-type: disc;
  }

  .list-inside {
    list-style-position: inside;
  }

  .ml-4 {
    margin-left: 1rem;
  }

  .text-blue-500 {
    color: #3b82f6;
  }
</style>

<main class="settings" class:dark={isDarkMode}>
  <header>
    <nav>
      <button
        class:active={activeTab === 'general'}
        class:inactive={activeTab !== 'general'}
        on:click={() => switchTab('general')}
      >
        General Settings
      </button>
      <button
        class:active={activeTab === 'subscription'}
        class:inactive={activeTab !== 'subscription'}
        on:click={() => switchTab('subscription')}
      >
        Subscription
      </button>
    </nav>
  </header>

  <section>
    {#if activeTab === 'general'}
      <!-- General Settings content -->
      <article>
        <h2>Profile Details</h2>
        <div class="profile-details">
          <div class="profile-info">
            <div>
              <label for="username">Username</label>
              <input type="text" id="username" value="John Doe" readonly>
            </div>
            <div>
              <label for="email">Email</label>
              <input type="email" id="email" value="john.doe@gmail.com" readonly>
            </div>
          </div>
          <div class="profile-row">
            <div class="profile-photo">
              <img src="https://via.placeholder.com/150" alt="Profile">
            </div>
            <div class="photo-actions">
              <button class="bg-blue-500 px-4 py-2 rounded-md">Upload Profile Photo</button>
              <button class="bg-red-500 px-4 py-2 rounded-md">Delete</button>
            </div>
          </div>
          <p class="text-gray-700">*Image size should be at least 320px by 320px, and less than 500kb. Allowed files: PNG and JPG.</p>
          
        </div>
      </article>

      <article>
        <h2>Change password</h2>
        <p class="text-gray-700 mb-4">You can update your account password here.</p>
        <button class="bg-blue-500 px-4 py-2 rounded-md">Change Password</button>
      </article>

      <article>
        <h2>Close account</h2>
        <p class="text-gray-700 mb-4">You can permanently delete or temporarily freeze your account.</p>
        <button class="bg-red-500 px-4 py-2 rounded-md">Close Account</button>
      </article>

      <article>
        <h2>Affiliate ID</h2>
        <p class="text-gray-700 mb-4">You can get your affiliate ID here.</p>
        <button class="bg-blue-500 px-4 py-2 rounded-md">Get Affiliate ID</button>
      </article>
    {:else if activeTab === 'subscription'}
      <!-- Subscription content -->
      <article>
        <h2>Subscription Details</h2>
        <div class="space-y-2">
          <p class="text-gray-700"><strong>Active Subscription:</strong> PhonesitesEssential (Monthly)</p>
          <p class="text-gray-700"><strong>Plan:</strong> PhonesitesEssential (Monthly)</p>
          <p class="text-gray-700"><strong>Billing Amount:</strong> $49/month</p>
          <p class="text-gray-700"><strong>Next Bill Date:</strong> April 21st, 2021</p>
          <p class="text-gray-700"><strong>Plan Features:</strong></p>
          <ul class="list-disc list-inside ml-4">
            <li>5 Websites</li>
            <li>25 Pages</li>
            <li>No follow-up Functionality</li>
          </ul>
          <div class="flex justify-start mt-4">
            <button class="bg-red-500 px-4 py-2 rounded-md mr-4">Cancel Subscription</button>
            <button class="bg-blue-500 px-4 py-2 rounded-md">Change Plan</button>
          </div>
        </div>
      </article>

      <article>
        <h2>Payment Method</h2>
        <div class="space-y-2">
          <p class="text-gray-700">Visa ***6921 expiring 12/2021</p>
          <div class="flex justify-start mt-4">
            <button class="bg-red-500 px-4 py-2 rounded-md mr-4">Remove</button>
            <button class="bg-blue-500 px-4 py-2 rounded-md">Edit</button>
          </div>
        </div>
      </article>

      <article>
        <h2>Receipt History</h2>
        <ul class="list-disc list-inside">
          <li class="text-gray-700">Essential (Monthly) - April 21st, 2021 - <a href="#" class="text-blue-500">PDF</a></li>
          <!-- Add more receipt history items as needed -->
        </ul>
      </article>
    {/if}
  </section>
</main>
