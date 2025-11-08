<script lang="ts">
  import HadithCard from "$lib/ui/hadith.svelte";
  const { params, data } = $props();

  const { hadith } = data;
</script>

<main class="max-w-screen-lg mx-auto">
  <section class="text-xl p5 rounded frow">
    <i class="i-pepicons-pop:book"></i>
    Book Name here
  </section>

  <section class="text-xl brd p5 rounded frow mb5">
    <i class="i-lets-icons:book"></i>
    {@html data.chapter}
  </section>

  <HadithCard data={hadith} />
</main>
