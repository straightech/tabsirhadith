import collections from "./collections.json";

let routes = ["/"];

collections.forEach((collection) => {
  const tmp = collection.name;
  routes.push(`/${tmp}`);

  collection.books.forEach((book) => {
    const bookRoute = `/${tmp}/${book.name}`;
    routes.push(bookRoute);

    book.chapters.forEach((chapter) => {
      chapter.hadiths?.forEach((hadith) => {
        if(hadith.id  > 10000 ) {
          // console.log(hadith);
        }
        const hadithRoute = `/${tmp}/hadith/${hadith.id}`;
        routes.push(hadithRoute);
      });
    });
  });
});

const json = 'export default ' + JSON.stringify(routes);

Bun.write("enteries.js", json);
