<div class="">
  {#each [1, 1, 1, 1, 1], index}
    <div class={"skeleton mt5 " + (index % 2 != 0 ? "bg-secondary" : "brd")}>
    </div>
  {/each}
</div>
