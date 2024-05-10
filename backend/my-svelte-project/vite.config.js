import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import copy from 'rollup-plugin-copy';

export default defineConfig({
  plugins: [
    svelte(),
    copy({
      targets: [
        { src: 'src/assets/**/*', dest: 'dist/assets' },
      ],
    }),
  ],
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    rollupOptions: {
      output: {
        entryFileNames: 'bundle.js',
        chunkFileNames: 'bundle-[name].js',
        assetFileNames: 'assets/[name].[ext]',
      },
    },
  },
});
