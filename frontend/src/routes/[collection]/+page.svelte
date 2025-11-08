<script lang="ts">
  import Loader from "$lib/ui/loaders/books.svelte";
  import authorData from "$lib/data/authors";

  let { data, params } = $props();
  const { books } = data;

  let author = authorData.find((x) => x.href === params.collection) ||
    authorData[0];
</script>

<main class="max-w-[1000px] mx-auto grid gap10 p10">
  <section class="brd p5 rounded flex flex-col gap3">
    <h1 class="font-medium frow justify-between text-primary">
      <span> {author.en_txt} </span>
      <span> {author.ar_txt} </span>
    </h1>
    <p>{author.intro}</p>
    <a
      class="text-primary underline ml-auto"
      href="/{params.collection}/about"
    >Read more</a>
  </section>

  {#await books}
    <Loader />
  {:then books}
    <section class="grid">
      {#each books as book, index}
        <a
          class="{index % 2 === 0 ? 'bg-secondary' : ''} p4 rounded"
          href="/{params.collection}/{book.id}"
        >
          {index + 1 + ".  "} {book.name}
        </a>
      {/each}
    </section>
  {:catch error}
    <p>Error loading books: {error.message}</p>
  {/await}
</main>
