<script lang="ts">
  let { data, params } = $props();
</script>

<section class="grid">
  {#each data.books as book, index}
    <a
      class="{index % 2 == 0 ? 'bg-secondary' : '' } p4"
      href="/{params.collection}/book/{book}"
    >
      {book}
    </a>
  {/each}
</section>
