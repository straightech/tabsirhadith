<script lang="ts">
  import { Input } from "@haze-ui/svelte";

  const leftSide = [
    { en_txt: "Sahih al-Bukhari", ar_txt: "صحيح البخاري", href: "bukhari" },
    { en_txt: "Sahih Muslim", ar_txt: "صحيح مسلم", href: "muslim" },
    { en_txt: "Sunan an-Nasa'i", ar_txt: "سنن النسائي", href: "nasai" },
    { en_txt: "Sunan Abi Dawud", ar_txt: "سنن أبي داود", href: "abudawud" },
    {
      en_txt: "Jami' at-Tirmidhi",
      ar_txt: "جامع الترمذي",
      href: "tirmidhi",
    },
    { en_txt: "Sunan Ibn Majah", ar_txt: "سنن ابن ماجه", href: "ibnmajah" },
    { en_txt: "Muwatta Malik", ar_txt: "موطأ مالك", href: "malik" },
    { en_txt: "Musnad Ahmad", ar_txt: "مسند أحمد", href: "ahmad" },
    { en_txt: "Sunan ad-Darimi", ar_txt: "سنن الدارمي", href: "darimi" },
  ];

  const rightSide = [
    {
      en_txt: "An-Nawawi's 40 Hadith",
      ar_txt: "الأربعون النووية",
      href: "forty",
    },
    {
      en_txt: "Riyad as-Salihin",
      ar_txt: "رياض الصالحين",
      href: "riyadussalihin",
    },
    { en_txt: "Al-Adab Al-Mufrad", ar_txt: "الأدب المفرد", href: "adab" },
    {
      en_txt: "Ash-Shama'il Al-Muhammadiyah",
      ar_txt: "الشمائل المحمدية",
      href: "shamail",
    },
    {
      en_txt: "Mishkat al-Masabih",
      ar_txt: "مشكاة المصابيح",
      href: "mishkat",
    },
    { en_txt: "Bulugh al-Maram", ar_txt: "بلوغ المرام", href: "bulugh" },
    { en_txt: "Collections of Forty", ar_txt: "الأربعينات", href: "forty" },
    { en_txt: "Hisn al-Muslim", ar_txt: "حصن المسلم", href: "hisn" },
  ];
</script>

<div class="bgred flex p3 lg:p10 container ma text-center grid gap10">
  <section class="ma grid gap10">
    <h1>
      The Hadith of the Prophet Muhammad صلى الله عليه و سلم
    </h1>

    <Input class="mx-auto grinput-solid-xl" placeholder="Search..." iconL="i-gg:search" />
  </section>

  <div class="grid lg:grid-cols-2 gap5 ">
    <section class="grid md:grid-cols-2 gap5">
      {#each leftSide as x}
        <a
          class="text-xl grid gap3 brd rounded p6 gap3 hover:brd-primary"
          href="/{x.href}"
        >
          <i class="i-uil:book-open mx-auto text-6xl bg-emerald"></i>
          <span class='grid gap3 bg-secondary p3 rounded justify-center'>
            <span class='whitespace-nowrap'>{x.en_txt}</span>
            <span>{x.ar_txt}</span>
          </span>
        </a>
      {/each}
    </section>

    <section class="grid-(~ cols-2) gap5 h-fit">
      {#each rightSide as x}
        <a class="text-xl brd rounded gap3 grid p6 hover:brd-primary" href="/{x.href}">
          <i class="i-ph:book-bookmark text-6xl mx-auto"></i>
          <span class="grid bg-secondary p3 rounded">
            <span>{x.en_txt}</span>
            <span>{x.ar_txt}</span>
          </span>
        </a>
      {/each}
    </section>
  </div>
</div>
