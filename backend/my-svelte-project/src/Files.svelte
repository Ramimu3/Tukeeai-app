<script>
  import { onMount } from 'svelte';
  import csvIconUrl from './assets/csv.svg';
  import csvlight from './assets/csv-light.svg';

  let files = [];
  export let isDarkMode;

  async function fetchFiles() {
    try {
      const response = await fetch('/api/files', {
        method: 'GET',
        credentials: 'include'
      });
      if (!response.ok) {
        throw new Error('Failed to fetch files: ' + response.statusText);
      }
      const data = await response.json();
      files = data;
    } catch (error) {
      console.error('Error fetching files:', error.message);
    }
  }

  onMount(() => {
    fetchFiles();
  });

  function getFileName(filePath) {
    return filePath.split('/').pop();
  }
  
  function truncateFileName(name) {
    const maxLength = 20;
    if (name.length <= maxLength) {
      return name;
    }
    return name.slice(0, maxLength) + '...';
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

<style>
  .file-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    grid-gap: 20px;
    list-style-type: none;
    padding: 0;
    margin-top: 1rem;
    margin-left: 5rem;
    margin-right: 5rem;
  }

  .file-item {
    background-color: var(--color-back);
    border: 2px solid var(--color-border);
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .dark .file-item {
    background-color: var(--color-Myrtle-Green);
  }

  .file-icon-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 10px;
  }

  .file-icon {
    width: 50px;
    height: 50px;
  }

  .file-name {
    word-break: break-word;
    margin-bottom: 10px;
    color: var(--color-jet);
  }

  .dark .file-name {
    color: var(--color-silver);
    background-color: var(--color-Myrtle-Green);
  }

  button.files-button {
    background-color: var(--color-turquoise);
    color: var(--color-black);
  }
</style>

<ul class="file-grid" class:dark={isDarkMode}>
  {#each files as file}
    <li class="file-item">
      <div>
        <div class="file-icon-container">
          {#if isDarkMode}
            <img class="file-icon" src={csvlight} alt="CSV Icon (Light)" />
          {:else}
            <img class="file-icon" src={csvIconUrl} alt="CSV Icon" />
          {/if}
        </div>
        <p class="file-name">{truncateFileName(getFileName(file.name))}</p>
      </div>
      <button type="button" class="files-button" on:click={() => window.location.href = `/api/files/${file.id}`}>
        Download
      </button>
    </li>
  {/each}
</ul>