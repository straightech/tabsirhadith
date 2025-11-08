<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
  import "virtual:uno.css";
  import "$lib/css/style.css";

  import Navbar from '$lib/ui/navbar.svelte'
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<Navbar/>
{@render children?.()}

