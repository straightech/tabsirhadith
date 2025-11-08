import collections from "$lib/collections";

export const load = async ({ params }) => {
  let collection = collections.find((x) => x.name === params.collection);
  collection = collection?.books || [];

  let data;

  collection.some((book, i) =>
    book.chapters.some((chapter) => {
      chapter.hadiths.some((x) => {
        if (String(x.id) === params.hadith) {
          data = {
            hadith: x,
            chapter: chapter.name,
            book: { name: book.name, index: i },
          };
          return true;
        }
      });
    }),
  );

  return data;
};
