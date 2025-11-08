import collections from "$lib/collections";

export const load = async ({ params }) => {
  let collection = collections.find((x) => x.name === params.collection);
  collection = collection?.books || [];
  let chapters = collection?.find((x) => x.name === params.num).chapters;
  return { chapters };
};
