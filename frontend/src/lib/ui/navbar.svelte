<script lang="ts">
  import { onMount } from "svelte";

  let theme = $state();

  onMount(() => theme = localStorage.theme);

  const toggleTheme = () => {
    theme = theme == "dark" ? "light" : "dark";
    localStorage.theme = theme;
    document.querySelector("html").className = theme;
  };
</script>

<nav class="p2 frow border-b-(1 solid border)">
  <a href="/" class="frow">
    <i class="i-material-symbols:book-ribbon-outline"></i>
    Tabsir Hadith
  </a>

  <button
    class="btn-soft-eqlg rounded-full ml-auto"
    aria-label="toggle dark mode"
    onclick={toggleTheme}
  >
    <div
      class={theme == "dark"
        ? "i-line-md:sun-rising-twotone-loop"
        : "i-line-md:moon-twotone-loop"}
    >
    </div>
  </button>
</nav>
