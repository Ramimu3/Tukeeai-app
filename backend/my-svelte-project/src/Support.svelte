<script>
  import shieldIcon from './assets/shield.svg';
  import bookIcon from './assets/book.svg';
  import flagIcon from './assets/flag.svg';
  import { Accordion, AccordionItem } from '@skeletonlabs/skeleton';
  import lightshield from './assets/shield-light.svg';
  import lightbook from './assets/book-light.svg';
  import lightflag from './assets/flag-light.svg';
  export let isDarkMode;
</script>

<body class="support" class:dark={isDarkMode}>
  <header>
    <h1>Hello, how can we help?</h1>
    <div class="search-container">
      <input type="text" placeholder="Ask a question..." aria-label="Search">
      <button>Search</button>
    </div>
    <p>or choose a category to quickly find the help you need</p>
  </header>

  <section class="categories">
    <div class="category">
      {#if isDarkMode}
        <img src={lightbook} alt="Getting Started Icon">
      {:else}
        <img src={bookIcon} alt="Getting Started Icon">
      {/if}
      <h2>Getting Started</h2>
    </div>
    <div class="category">
      {#if isDarkMode}
        <img src={lightshield} alt="Resources Icon">
      {:else}
        <img src={shieldIcon} alt="Resources Icon">
      {/if}
      <h2>Resources</h2>
    </div>
    <div class="category">
      {#if isDarkMode}
        <img src={lightflag} alt="Trust & Safety Icon">
      {:else}
        <img src={flagIcon} alt="Trust & Safety Icon">
      {/if}
      <h2>Trust & Safety</h2>
    </div>
  </section>

  <section class="popular-articles">
    <h2>Popular Articles</h2>
    <Accordion autocollapse>
      <AccordionItem>
        <span slot="lead">Help Manual for new users</span>
        <div slot="content">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, nisi vel bibendum
            consectetur, nisl nisi aliquam eros, eget tincidunt nisl nunc eget diam. Maecenas sed diam
            eget risus varius blandit sit amet non magna.
          </p>
        </div>
      </AccordionItem>
      <AccordionItem>
        <span slot="lead">Managing Data in knowledge base</span>
        <div slot="content">
          <p>
            Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Donec sollicitudin
            molestie malesuada. Curabitur aliquet quam id dui posuere blandit. Nulla quis lorem ut
            libero malesuada feugiat. Curabitur non nulla sit amet nisl tempus convallis quis ac
            lectus.
          </p>
        </div>
      </AccordionItem>
      <AccordionItem>
        <span slot="lead">Help Manual for new users</span>
        <div slot="content">
          <p>
            Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem. Vestibulum ante ipsum
            primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque, auctor
            sit amet aliquam vel, ullamcorper sit amet ligula. Proin eget tortor risus. Vivamus magna
            justo, lacinia eget consectetur sed, convallis at tellus.
          </p>
        </div>
      </AccordionItem>
    </Accordion>
  </section>
</body>

<style>
  body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 20px;
  display: grid;
}

header {
  text-align: center;
  margin-bottom: 30px;
  width: 75%;
}

h1 {
  font-size: 32px;
  margin-bottom: 10px;
  font-weight: 600;
}

.search-container {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}

input[type="text"] {
  padding: 8px;
    width: 300px;
    border: 2px solid var(--color-border);
    border-radius: 4px;
    background-color: var(--color-back);
}

.dark input[type="text"] {
  background-color: var(--color-border);
  border-color: var(--color-back);
}

button {
  padding: 8px 16px;
    border-radius: 7px;
    margin-left: 10px;
    cursor: pointer;
    background-color: var(--color-turquoise);
    color: var(--color-black);
    border-width: 2px;
    border-color: var(--color-border);
}

p {
  font-size: 14px;
  color: #666;
}

.categories {
  display: flex;
  justify-content: space-between;
  margin-bottom: 30px;
  width: 75%;
}

.category {
  text-align: center;
    padding: 20px;
    background-color: var(--color-back);
    border-radius: 20px;
    flex-basis: 30%;
    border-width: 2px;
    border-color: var(--color-border);
    display: grid;
    justify-content: center;
  }

.dark .category {
    background-color: var(--color-Myrtle-Green);
  }

.category img {
    width: 100%;
    height: 60px;
    margin-bottom: 20px;
}

.category h2 {
  font-size: 18px;
  margin: 0;
}

.popular-articles {
  margin-bottom: 30px;
  width: 75%;
}

.popular-articles h2 {
  font-size: 20px;
  margin-bottom: 10px;
}



  </style>