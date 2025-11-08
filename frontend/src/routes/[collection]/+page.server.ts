import authorData from "$lib/data/authors";

export const load = async ({ params }) => {
  const collection = authorData.find((x) => x.href === params.collection);
  const id = collection?.id || 1;

  const books = fetch(
    `https://api.tabsirhadith.com/collections/${id}/books`,
  )
    .then((x) => x.json())
    .then((data) => data.sort((a, b) => a.visible_id - b.visible_id));

  return { books };
};
