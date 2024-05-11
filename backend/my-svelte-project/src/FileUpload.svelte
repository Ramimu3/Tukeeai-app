<script lang="ts">
  import { FileDropzone, ProgressBar } from '@skeletonlabs/skeleton';
  import { writable } from 'svelte/store';
  import fileuploadicon from './assets/Dashboardicons/upload-file.svg';
  import fileuploadiconlight from './assets/Dashboardicons/upload-file-light.svg';
  let files: FileList;
  let taskId: string | null = null;
  let progress = writable(0);
  let status = 'Waiting...';
  let outputFile: string | null = null;

  function handleFileSelection(event: Event) {
    const fileList = (event.target as HTMLInputElement).files;
    if (fileList && fileList.length > 0) {
      files = fileList;
    } else {
      files = new FileList();
    }
  }

  async function handleSubmit() {
    if (!files || files.length === 0) {
      alert('Please select a file');
      return;
    }

    const formData = new FormData();
    formData.append('file', files[0]);

    const appElement = document.querySelector('#app') as HTMLElement;
    const csrfToken = appElement.dataset.csrfToken || '';

    try {
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': csrfToken
        }
      });

      if (response.ok) {
        const data = await response.json();
        taskId = data.task_id;
        console.log('Task ID:', taskId);
        initProgressBar();
      } else {
        console.error('File upload failed');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  async function initProgressBar() {
    if (!taskId) return;

    const response = await fetch(`/celery-progress/${taskId}/`, { method: 'GET' });
    if (!response.ok) throw new Error('Failed to fetch task progress');

    const data = await response.json();
    console.log(data);

    status = data.state;
    progress.set((data.progress.current / data.progress.total) * 100);

    if (data.complete) {
      status = "Completed";
      // Redirect to the files page after a short delay
      setTimeout(() => {
        window.location.href = '/#/dashboard/files';
      }, 1000);
    } else if (data.state === 'FAILURE') {
      status = "Error";
    } else {
      setTimeout(initProgressBar, 1000);
    }
  }
</script>
<div class="upload">
<FileDropzone
  name="file-dropzone"
  accept=".pdf,.epub,.mobi,.docx,.doc,.txt"
  bind:files={files}
  on:change={handleFileSelection}
>
  <svelte:fragment slot="lead">
    <i class="fa-solid fa-file-arrow-up"></i>
  </svelte:fragment>
  <svelte:fragment slot="message">
    {#if files && files.length > 0}
      {files[0].name}
    {:else}
      Upload a file or drag and drop
    {/if}
  </svelte:fragment>
  <svelte:fragment slot="meta">
    PDF and EPUB allowed.
  </svelte:fragment>
</FileDropzone>

<button on:click={handleSubmit} class="btn variant-filled">Upload</button>

{#if taskId}
  <div class="progress-container">
    <ProgressBar value={$progress} max={100} />
    <p class="progress-message">Task Status: {status}</p>
  </div>
  {/if}
</div>

  <style>
  .btn{
    margin-top:20px ;
  }

  .btn{
    margin-top: 20px;
    background-color: var(--color-turquoise);
    color: var(--color-jet);
    border-radius: 13px;
    border: var(--color-border);
  }
  @media (max-width: 1000px) {
    .upload {
    align-items: center;
    display: grid;
        }
  }

    .progress-container {
      margin-top: 20px;
    }
  
    .progress-message {
      margin-top: 10px;
    }
    .upload {
    width: clamp(15rem, 0.571rem + 43.81vw, 40rem);    align-items: center;
    display: grid;
    margin: 0 auto;
    }
  </style>
  