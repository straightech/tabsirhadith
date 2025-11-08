import collections from "$lib/collections";

interface Props {
  collection: any[];
  params: { collection: string };
}

export const load = ({ params }: Props) => {
  let collection = collections.find((x) => x.name === params.collection);
  collection = collection?.books || []

  const books = collection.map(x => x.name);
  return { books };
};
