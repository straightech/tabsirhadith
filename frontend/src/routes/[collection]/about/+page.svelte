<script lang="ts">
  import Bukhari from "$lib/about/bukhari.svelte";
  import Tirmidhi from "$lib/about/tirmidhi.svelte";
  import Muslim from "$lib/about/muslim.svelte";
  import Nasai from "$lib/about/nasai.svelte";
  import IbnMajah from "$lib/about/ibnmajah.svelte";
  import Ahmad from "$lib/about/ahmad.svelte";
  import AbuDawud from "$lib/about/abudawud.svelte";

  const Mapcomponents = {
    bukhari: Bukhari,
    tirmidhi: Tirmidhi,
    muslim: Muslim,
    nasai: Nasai,
    ibnmajah: IbnMajah,
    ahmad: Ahmad,
    abudawud: AbuDawud,
  };

  const { params } = $props();

  const About = Mapcomponents[params.collection];
</script>

<About />
