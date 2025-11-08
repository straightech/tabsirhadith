<script lang="ts">
  let { children } = $props();
</script>

<main class='max-w-[1200px] mx-auto my-20'>
  {@render children?.()}
</main>
