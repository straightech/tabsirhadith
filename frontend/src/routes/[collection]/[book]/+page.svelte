<script lang="ts">

  let { params, data } = $props();
  const { chapters } = data;
  import Loader from "$lib/ui/loaders/chapters.svelte";
</script>

<div class="grid gap20 max-w-[1000px] mx-auto p3 lg:p10">
  {#await chapters}
    <Loader />
  {:then chapters}
    {#each chapters as chapter}
      <section class="grid gap3 lg:gap5">
        <p class="text-xl brd p5 rounded frow">
          <i class="i-lets-icons:book"></i>
          {chapter.name}
        </p>

        {#each chapter.hadiths as hadith}
          <div
            class="grid lg:grid-cols-[1fr_auto_1fr] gap5 bg-secondary p5 rounded leading-loose"
          >
            <div class="grid gap3 h-fit">
              {@html hadith.english_text}
            </div>
            <div class="brd"></div>
            <div class="arabic_txt">{@html hadith.arabic_text}</div>
            <button
              aria-labelledby="bookmark"
              class="btn-secondary-eqmd bg-border hover:bg-border/80 rounded-full w-fit"
            >
              <i class="i-mingcute:bookmark-line"></i>
            </button>
          </div>
        {/each}
      </section>
    {/each}
  {/await}
</div>
