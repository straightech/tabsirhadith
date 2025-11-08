<section class="grid gap5">
  <div class="p5 brd rounded flex">
    <span class="skeleton"></span>
  </div>

  {#each [1, 1, 1, 1, 1]}
    <div class="bg-secondary p4 rounded grid grid-cols-[1fr_auto_1fr] gap3">
      <div class="grid gap3">
        <p class="skeleton bg-mutedfg h-1"></p>
        <p class="skeleton bg-mutedfg h-3"></p>
        <p class="skeleton bg-mutedfg"></p>
      </div>

      <div class="brd"></div>
      <div class="grid gap3">
        <p class="skeleton bg-mutedfg h-2"></p>
        <p class="skeleton bg-mutedfg h-2"></p>
        <p class="skeleton bg-mutedfg"></p>
      </div>
    </div>
  {/each}
</section>
