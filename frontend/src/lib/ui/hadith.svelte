<script lang="ts">
  let { data } = $props();
</script>

<div
  class="grid lg:grid-cols-[1fr_auto_1fr] gap5 bg-secondary p5 rounded leading-loose"
>
  <div class="grid gap3 h-fit">
    {@html data.english_text}
  </div>
  <div class="brd"></div>
  <div class="arabic_txt">{@html data.arabic_text}</div>
  <button
    aria-labelledby="bookmark"
    class="btn-secondary-eqmd bg-border hover:bg-border/80 rounded-full w-fit"
  >
    <i class="i-mingcute:bookmark-line"></i>
  </button>
</div>
