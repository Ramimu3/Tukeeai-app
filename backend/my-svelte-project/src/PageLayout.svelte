<!-- PageLayout.svelte -->
<script>
    import { onMount, onDestroy } from 'svelte';
  
    let appElement;
    let resizeHandler;
  
    onMount(() => {
      appElement = document.getElementById('app');
  
      if (appElement) {
        const applyStyles = () => {
          appElement.style.margin = '0 auto';
          appElement.style.padding = '2rem';
          appElement.style.textAlign = 'center';
          appElement.style.width = 'clamp(20rem, 293.3333vw + -53.3333rem, 130rem)';
  
          if (window.innerWidth >= 768) {
            appElement.style.marginLeft = '200px';
          } else {
            appElement.style.marginLeft = '0';
          }
        };
  
        const resetStyles = () => {
          appElement.style.margin = '';
          appElement.style.padding = '';
          appElement.style.textAlign = '';
          appElement.style.width = '';
          appElement.style.marginLeft = '';
        };
  
        resizeHandler = () => {
          applyStyles();
        };
  
        applyStyles();
        window.addEventListener('resize', resizeHandler);
      }
  
      return () => {
        if (appElement) {
          window.removeEventListener('resize', resizeHandler);
          resetStyles();
        }
      };
    });
  </script>
  
  <div class="page-layout">
    <slot></slot>
  </div>
  