export const load = async ({ params }) => {
  const id = params.book;
  const url = `https://api.tabsirhadith.com/books/${id}/chapters`;
  const chapters = fetch(url).then((x) => x.json());
  return { chapters };
};
