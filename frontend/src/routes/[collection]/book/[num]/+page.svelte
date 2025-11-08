<script lang="ts">
  let { params, data } = $props();
  import HadithCard from "$lib/ui/hadith.svelte";
</script>

<div class="grid gap20">
  {#each data.chapters as chapter, index}
    <section class="grid gap5">
      <p class="text-xl brd p5 rounded frow">
        <i class="i-lets-icons:book"></i>
        {chapter.name}
      </p>

      {#each chapter.hadiths as hadith}
        <HadithCard data={hadith} />
      {/each}
    </section>
  {/each}
</div>
